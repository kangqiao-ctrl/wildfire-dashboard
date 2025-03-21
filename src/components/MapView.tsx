import React, { useRef, useEffect, useState } from 'react';
import mapboxgl, { Map, GeoJSONSource, MapMouseEvent } from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import './MapView.css';

// If you see TS error about 'workerClass', 
// you may need: (window as any).workerClass = mapboxgl.Worker;

// Interface for the camera data that doesn't have GeoJSON format
interface CameraData {
  name: string;
  thumbnail_url: string;
}

function MapView() {
  const mapContainerRef = useRef<HTMLDivElement | null>(null);
  const mapRef = useRef<Map | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    // Get Mapbox access token from environment variable
    const accessToken = import.meta.env.VITE_MAPBOX_ACCESS_TOKEN;
    
    if (!accessToken) {
      setError('Mapbox access token is missing. Please set VITE_MAPBOX_ACCESS_TOKEN in your environment variables.');
      return;
    }
    
    // Set the Mapbox access token
    mapboxgl.accessToken = accessToken;

    if (mapRef.current) {
      // If map is already initialized, do nothing
      return;
    }

    // Initialize map only once
    try {
      mapRef.current = new mapboxgl.Map({
        container: mapContainerRef.current as HTMLDivElement,
        style: 'mapbox://styles/mapbox/outdoors-v12', // Use outdoors style for wildfire monitoring
        center: [-119.4179, 36.7783], // California approximate center
        zoom: 5,
      });

      // Add navigation controls (zoom in/out)
      mapRef.current.addControl(new mapboxgl.NavigationControl(), 'top-right');

      const map = mapRef.current;

      map.on('load', async () => {
        try {
          setLoading(true);
          
          // Load all data from the public/data folder
          await Promise.all([
            loadCameraFeeds(map),
            loadLightningData(map),
            loadRiskZones(map),
            loadTrafficData(map),
            loadSocialPosts(map)
          ]);
          
          setLoading(false);
        } catch (err) {
          console.error('Error loading data:', err);
          setError('Failed to load map data. Please check the console for details.');
          setLoading(false);
        }
      });
    } catch (err) {
      console.error('Error initializing map:', err);
      setError('Failed to initialize map. Please check the console for details.');
      setLoading(false);
    }

    return () => {
      // Cleanup on component unmount
      if (mapRef.current) {
        mapRef.current.remove();
        mapRef.current = null;
      }
    };
  }, []);

  // Function to load camera feeds data
  const loadCameraFeeds = async (map: Map) => {
    const response = await fetch('/data/cameraFeeds.json');
    if (!response.ok) {
      throw new Error('Failed to load camera feeds data');
    }
    
    const data = await response.json();
    
    // Add data source
    map.addSource('cameraFeeds', {
      type: 'geojson',
      data
    });

    // Add circle layer for cameras
    map.addLayer({
      id: 'cameraFeedsLayer',
      type: 'circle',
      source: 'cameraFeeds',
      paint: {
        'circle-color': [
          'match',
          ['get', 'status'],
          'active', '#4CAF50',  // Green for active
          'maintenance', '#FFC107', // Yellow for maintenance
          '#FF5252'  // Red default
        ],
        'circle-radius': 8,
        'circle-stroke-width': 1,
        'circle-stroke-color': '#333'
      }
    });

    // Add popup on click
    addPopupToLayer(map, 'cameraFeedsLayer', (properties) => `
      <h4>${properties.title}</h4>
      <p>${properties.description}</p>
      <p>Status: ${properties.status}</p>
      <p>Type: ${properties.type}</p>
    `);

    // Add hover effect
    addHoverEffect(map, 'cameraFeedsLayer');
  };

  // Function to load lightning strike data
  const loadLightningData = async (map: Map) => {
    const response = await fetch('/data/lightning.json');
    if (!response.ok) {
      throw new Error('Failed to load lightning data');
    }
    
    const data = await response.json();
    
    // Add data source
    map.addSource('lightning', {
      type: 'geojson',
      data
    });

    // Add symbol layer for lightning
    map.addLayer({
      id: 'lightningLayer',
      type: 'symbol',
      source: 'lightning',
      layout: {
        'icon-image': 'lightning-11', // Default Mapbox icon
        'icon-size': 1.5,
        'icon-allow-overlap': true
      }
    });

    // Add pulse circle for emphasis
    map.addLayer({
      id: 'lightningPulseLayer',
      type: 'circle',
      source: 'lightning',
      paint: {
        'circle-radius': [
          'match',
          ['get', 'intensity'],
          'high', 25,
          'medium', 20,
          'low', 15,
          15
        ],
        'circle-color': [
          'match',
          ['get', 'intensity'],
          'high', 'rgba(255, 82, 82, 0.4)',
          'medium', 'rgba(255, 193, 7, 0.4)',
          'low', 'rgba(33, 150, 243, 0.4)',
          'rgba(0, 0, 0, 0.4)'
        ],
        'circle-opacity': 0.6,
        'circle-stroke-width': 0
      }
    });

    // Add popup on click
    addPopupToLayer(map, 'lightningLayer', (properties) => `
      <h4>${properties.title}</h4>
      <p>${properties.description}</p>
      <p>Intensity: ${properties.intensity}</p>
      <p>Time: ${new Date(properties.timestamp).toLocaleString()}</p>
    `);

    // Add hover effect
    addHoverEffect(map, 'lightningLayer');
  };

  // Function to load risk zone data
  const loadRiskZones = async (map: Map) => {
    const response = await fetch('/data/risk.json');
    if (!response.ok) {
      throw new Error('Failed to load risk zone data');
    }
    
    const data = await response.json();
    
    // Add data source
    map.addSource('riskZones', {
      type: 'geojson',
      data
    });

    // Add fill layer for risk zones
    map.addLayer({
      id: 'riskZonesLayer',
      type: 'fill',
      source: 'riskZones',
      paint: {
        'fill-color': [
          'match',
          ['get', 'riskLevel'],
          'high', 'rgba(255, 82, 82, 0.5)',
          'medium', 'rgba(255, 193, 7, 0.5)',
          'low', 'rgba(33, 150, 243, 0.5)',
          'rgba(0, 0, 0, 0.5)'
        ],
        'fill-outline-color': '#000'
      }
    });

    // Add popup on click
    map.on('click', 'riskZonesLayer', (e: MapMouseEvent) => {
      if (!e.features || e.features.length === 0) return;
      
      const feature = e.features[0];
      const props = feature.properties as Record<string, string>;
      
      new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML(`
          <h4>${props.title}</h4>
          <p>${props.description}</p>
          <p>Risk Level: ${props.riskLevel}</p>
          <p>Category: ${props.category}</p>
        `)
        .addTo(map);
    });

    // Add hover effect
    addHoverEffect(map, 'riskZonesLayer');
  };

  // Function to load traffic data
  const loadTrafficData = async (map: Map) => {
    const response = await fetch('/data/traffic.json');
    if (!response.ok) {
      return; // Optional data, don't throw error
    }
    
    try {
      const data = await response.json();
      
      // Add data source
      map.addSource('traffic', {
        type: 'geojson',
        data
      });

      // Add line layer for traffic
      map.addLayer({
        id: 'trafficLayer',
        type: 'line',
        source: 'traffic',
        layout: {
          'line-join': 'round',
          'line-cap': 'round'
        },
        paint: {
          'line-color': [
            'match',
            ['get', 'congestion'],
            'high', '#FF5252',
            'medium', '#FFC107',
            'low', '#4CAF50',
            '#4CAF50'
          ],
          'line-width': 4
        }
      });

      // Add popup on click
      addPopupToLayer(map, 'trafficLayer', (properties) => `
        <h4>${properties.title}</h4>
        <p>${properties.description}</p>
        <p>Congestion: ${properties.congestion}</p>
      `);
    } catch (err) {
      console.warn('Error loading traffic data:', err);
    }
  };

  // Function to load social media posts
  const loadSocialPosts = async (map: Map) => {
    const response = await fetch('/data/socialPosts.json');
    if (!response.ok) {
      return; // Optional data, don't throw error
    }
    
    try {
      const data = await response.json();
      
      // Add data source
      map.addSource('socialPosts', {
        type: 'geojson',
        data
      });

      // Add symbol layer for social posts
      map.addLayer({
        id: 'socialPostsLayer',
        type: 'symbol',
        source: 'socialPosts',
        layout: {
          'icon-image': 'marker-15',
          'icon-size': 1.2,
          'icon-allow-overlap': true,
          'text-field': ['get', 'platform'],
          'text-font': ['Open Sans Semibold', 'Arial Unicode MS Bold'],
          'text-offset': [0, 1.25],
          'text-anchor': 'top'
        },
        paint: {
          'text-color': '#333',
          'text-halo-color': '#fff',
          'text-halo-width': 1
        }
      });

      // Add popup on click
      addPopupToLayer(map, 'socialPostsLayer', (properties) => `
        <h4>${properties.platform} Post</h4>
        <p>${properties.message}</p>
        <p>User: ${properties.user}</p>
        <p>Posted: ${new Date(properties.timestamp).toLocaleString()}</p>
      `);

      // Add hover effect
      addHoverEffect(map, 'socialPostsLayer');
    } catch (err) {
      console.warn('Error loading social posts:', err);
    }
  };

  // Helper function to add popups to a layer
  const addPopupToLayer = (map: Map, layerId: string, contentFn: (props: Record<string, string>) => string) => {
    map.on('click', layerId, (e: MapMouseEvent) => {
      if (!e.features || e.features.length === 0) return;
      
      const feature = e.features[0];
      const coordinates = (feature.geometry as any).coordinates.slice();
      const properties = feature.properties as Record<string, string>;
      
      // Ensure that if the map is zoomed out such that multiple
      // copies of the feature are visible, the popup appears
      // over the copy being pointed to.
      while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
        coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
      }
      
      new mapboxgl.Popup()
        .setLngLat(coordinates)
        .setHTML(contentFn(properties))
        .addTo(map);
    });
  };

  // Helper function to add hover effects to a layer
  const addHoverEffect = (map: Map, layerId: string) => {
    // Change cursor to pointer when hovering over the layer
    map.on('mouseenter', layerId, () => {
      map.getCanvas().style.cursor = 'pointer';
    });
    
    // Reset cursor when mouse leaves the layer
    map.on('mouseleave', layerId, () => {
      map.getCanvas().style.cursor = '';
    });
  };

  if (error) {
    return <div className="error-message">{error}</div>;
  }

  return (
    <div className="map-container-wrapper">
      {loading && <div className="loading-indicator">Loading map data...</div>}
      <div className="map-container" ref={mapContainerRef} />
      <div className="map-legend">
        <h4>Map Legend</h4>
        <div className="legend-item">
          <span className="circle-icon green"></span> Active Camera
        </div>
        <div className="legend-item">
          <span className="circle-icon yellow"></span> Camera in Maintenance
        </div>
        <div className="legend-item">
          <span className="circle-icon red"></span> Risk Zone
        </div>
        <div className="legend-item">
          <span className="lightning-icon"></span> Lightning Strike
        </div>
      </div>
    </div>
  );
}

export default MapView;
