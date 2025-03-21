import React, { useRef, useEffect, useState } from 'react';
import mapboxgl, { Map, MapMouseEvent } from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import './MapView.css';
import { Feature, Point } from 'geojson';

// If you see TS error about 'workerClass', 
// you may need: (window as any).workerClass = mapboxgl.Worker;

// Interface for the camera data stored in local state:
interface CameraData {
  id: string;
  name: string;
  thumbnail_url: string;
  coordinates: number[] | null;
}

// Helper to sanitize any HTML string
function sanitizeHTML(str: string) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

const MapView: React.FC = () => {
  const mapContainerRef = useRef<HTMLDivElement | null>(null);
  const mapRef = useRef<Map | null>(null);

  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  // Track which layers are currently visible
  const [layerVisibility, setLayerVisibility] = useState({
    webcams: true,
    counties: true,
  });

  // List of cameras for potential side-panel usage
  const [cameras, setCameras] = useState<CameraData[]>([]);

  useEffect(() => {
    // Pull access token from environment
    const accessToken = import.meta.env.VITE_MAPBOX_ACCESS_TOKEN;
    if (!accessToken) {
      setError(
        'Mapbox access token is missing. Please set VITE_MAPBOX_ACCESS_TOKEN in your environment variables.'
      );
      return;
    }
    mapboxgl.accessToken = accessToken;

    // Prevent re-initializing the map
    if (mapRef.current) return;

    try {
      // Initialize the map
    mapRef.current = new mapboxgl.Map({
      container: mapContainerRef.current as HTMLDivElement,
        style: 'mapbox://styles/mapbox/outdoors-v12', // A style for wildfire monitoring
        center: [-119.4179, 36.7783], // Approx center of CA
      zoom: 5,
    });

      // Add navigation controls
      mapRef.current.addControl(new mapboxgl.NavigationControl(), 'top-right');

      // On map load, fetch all data
      mapRef.current.on('load', async () => {
        try {
          setLoading(true);
    const map = mapRef.current;

          // Make sure map still exists
          if (!map) return;

          // 1) Load CA Counties (underneath)
          await loadCACounties(map);

          // 2) Load webcam points
          const webcamsData = await loadWebcams(map);
          if (webcamsData && webcamsData.features) {
            const _webcams = webcamsData.features.map((feature: Feature, i: number) => {
              const props = feature.properties || {};
              const geom = feature.geometry?.type === 'Point' ? feature.geometry.coordinates : null;
              return {
                id: props.id ?? `webcam_${i}`,
                name: props.name || 'Unnamed Camera',
                thumbnail_url: props.thumbnail_url || '',
                coordinates: geom,
              };
            });
            setCameras((prev) => {
              // Avoid duplicates by ID
              const existingIds = new Set(prev.map((c) => c.id));
              const newItems = _webcams.filter((c: CameraData) => !existingIds.has(c.id));
              return [...prev, ...newItems];
            });
          }

          // 3) Load other data in parallel
          await Promise.all([
            loadCameraFeeds(map),
            loadLightningData(map),
            loadRiskZones(map),
            loadTrafficData(map),
            loadSocialPosts(map),
          ]);

          setLoading(false);
        } catch (err) {
          console.error('Error loading map data:', err);
          setError('Failed to load map data. See console for details.');
          setLoading(false);
        }
      });
    } catch (err) {
      console.error('Error initializing map:', err);
      setError('Failed to initialize map. See console for details.');
      setLoading(false);
    }

    return () => {
      // Cleanup on unmount
      if (mapRef.current) {
        mapRef.current.remove(); // This should remove layers, sources, and event listeners
        mapRef.current = null;
      }
    };
  }, []);

  // -----------
  // LOADERS
  // -----------

  // 1) Load CA County boundaries
  const loadCACounties = async (map: Map) => {
    try {
      const response = await fetch('/data/california_counties.geojson');
      if (!response.ok) {
        console.error(`Failed to load counties: ${response.status} ${response.statusText}`);
        throw new Error('Failed to load California counties data');
      }
      const data = await response.json();

      map.addSource('ca-counties', {
        type: 'geojson',
        data: data,
        maxzoom: 12,
        buffer: 128,
        tolerance: 0.375,
      });

      // Add a fill layer for counties
      map.addLayer({
        id: 'countiesLayer',
        type: 'fill',
        source: 'ca-counties',
        paint: {
          'fill-color': 'rgba(200, 200, 200, 0.1)',
          'fill-outline-color': '#585858',
        },
      });
    } catch (err) {
      console.error('Error loading counties data:', err);
      // Continue with other data instead of failing completely
    }
  };

  // 2) Load webcams layer
  const loadWebcams = async (map: Map) => {
    try {
      const response = await fetch('/data/webcams.geojson');
      if (!response.ok) {
        console.error(`Failed to load webcams: ${response.status} ${response.statusText}`);
        throw new Error('Failed to load webcams data');
      }
      const data = await response.json();

      // Add source
      map.addSource('webcams', { type: 'geojson', data });

      // Add layer
      map.addLayer({
        id: 'webcamsLayer',
        type: 'circle',
        source: 'webcams',
        paint: {
          'circle-color': '#FF6B6B',
          'circle-radius': 6,
          'circle-stroke-width': 1,
          'circle-stroke-color': '#333',
        },
      });

      // Popup on click
      map.on('click', 'webcamsLayer', (e) => {
        if (!e.features || e.features.length === 0) return;
        const feature = e.features[0] as Feature<Point>;
        const coords = feature.geometry.coordinates.slice();
        const props = feature.properties || {};

        // Create popup
        new mapboxgl.Popup()
          .setLngLat(coords as [number, number])
          .setHTML(`
            <h4>${sanitizeHTML(props.name || 'Unnamed')}</h4>
            ${
              props.thumbnail_url
                ? `<img src="${sanitizeHTML(props.thumbnail_url)}" style="width:100%;max-width:200px;" alt="Camera"/>`
                : ''
            }
            <p>${sanitizeHTML(props.description || '')}</p>
          `)
          .addTo(map);
      });

      // Hover effect
      map.on('mouseenter', 'webcamsLayer', () => {
        map.getCanvas().style.cursor = 'pointer';
      });
      map.on('mouseleave', 'webcamsLayer', () => {
        map.getCanvas().style.cursor = '';
      });

      return data;
    } catch (err) {
      console.error('Error loading webcams data:', err);
      // Return empty data instead of failing
      return { type: 'FeatureCollection', features: [] };
    }
  };

  // 3) Camera Feeds
  const loadCameraFeeds = async (map: Map) => {
    const response = await fetch('/data/cameraFeeds.json');
    if (!response.ok) {
      throw new Error('Failed to load camera feeds data');
    }
    const data = await response.json();

    map.addSource('cameraFeeds', { type: 'geojson', data });

    map.addLayer({
      id: 'cameraFeedsLayer',
      type: 'circle',
      source: 'cameraFeeds',
      paint: {
        'circle-color': [
          'match',
          ['get', 'status'],
          'active',
          '#4CAF50', // green
          'maintenance',
          '#FFC107', // yellow
          '#FF5252', // red default
        ],
        'circle-radius': 8,
        'circle-stroke-width': 1,
        'circle-stroke-color': '#333',
      },
    });

    // Add popup
    addPopupToLayer(
      map,
      'cameraFeedsLayer',
      (properties) => `
        <h4>${sanitizeHTML(properties.title || 'Camera')}</h4>
        <p>${sanitizeHTML(properties.description || '')}</p>
        <p>Status: ${sanitizeHTML(properties.status || 'Unknown')}</p>
        <p>Type: ${sanitizeHTML(properties.type || 'Not specified')}</p>
      `
    );

    // Hover effect
    addHoverEffect(map, 'cameraFeedsLayer');
  };

  // 4) Lightning
  const loadLightningData = async (map: Map) => {
    const response = await fetch('/data/lightning.json');
    if (!response.ok) {
      throw new Error('Failed to load lightning data');
    }
    const data = await response.json();

    map.addSource('lightning', { type: 'geojson', data });

    map.addLayer({
      id: 'lightningLayer',
      type: 'symbol',
      source: 'lightning',
      layout: {
        'icon-image': 'lightning-11',
        'icon-size': 1.5,
        'icon-allow-overlap': true,
      },
    });

    map.addLayer({
      id: 'lightningPulseLayer',
      type: 'circle',
      source: 'lightning',
      paint: {
        'circle-radius': [
          'match',
          ['get', 'intensity'],
          'high',
          25,
          'medium',
          20,
          'low',
          15,
          15,
        ],
        'circle-color': [
          'match',
          ['get', 'intensity'],
          'high',
          'rgba(255, 82, 82, 0.4)',
          'medium',
          'rgba(255, 193, 7, 0.4)',
          'low',
          'rgba(33, 150, 243, 0.4)',
          'rgba(0, 0, 0, 0.4)',
        ],
        'circle-opacity': 0.6,
        'circle-stroke-width': 0,
      },
    });

    addPopupToLayer(
      map,
      'lightningLayer',
      (props) => `
        <h4>${sanitizeHTML(props.title || 'Lightning Strike')}</h4>
        <p>${sanitizeHTML(props.description || '')}</p>
        <p>Intensity: ${sanitizeHTML(props.intensity || 'Unknown')}</p>
        <p>Time: ${props.timestamp ? new Date(props.timestamp).toLocaleString() : 'Unknown'}</p>
      `
    );

    addHoverEffect(map, 'lightningLayer');
  };

  // 5) Risk Zones
  const loadRiskZones = async (map: Map) => {
    const response = await fetch('/data/risk.json');
    if (!response.ok) {
      throw new Error('Failed to load risk zone data');
    }
    const data = await response.json();

    map.addSource('riskZones', { type: 'geojson', data });

    map.addLayer({
      id: 'riskZonesLayer',
      type: 'fill',
      source: 'riskZones',
      paint: {
        'fill-color': [
          'match',
          ['get', 'riskLevel'],
          'high',
          'rgba(255, 82, 82, 0.5)',
          'medium',
          'rgba(255, 193, 7, 0.5)',
          'low',
          'rgba(33, 150, 243, 0.5)',
          'rgba(0, 0, 0, 0.5)',
        ],
        'fill-outline-color': '#000',
      },
    });

    // On click
    map.on('click', 'riskZonesLayer', (e) => {
      if (!e.features || e.features.length === 0) return;
      const feature = e.features[0];
      const props = feature.properties || {};
      new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML(`
          <h4>${sanitizeHTML(props.title || 'Risk Zone')}</h4>
          <p>${sanitizeHTML(props.description || '')}</p>
          <p>Risk Level: ${sanitizeHTML(props.riskLevel || 'Unknown')}</p>
          <p>Category: ${sanitizeHTML(props.category || 'Not categorized')}</p>
        `)
        .addTo(map);
    });

    addHoverEffect(map, 'riskZonesLayer');
  };

  // 6) Traffic
  const loadTrafficData = async (map: Map) => {
    try {
      const response = await fetch('/data/traffic.json');
      if (!response.ok) {
        // optional data
        return;
      }
      
      const data = await response.json();

      map.addSource('traffic', { type: 'geojson', data });

      map.addLayer({
        id: 'trafficLayer',
        type: 'line',
        source: 'traffic',
        layout: {
          'line-join': 'round',
          'line-cap': 'round',
        },
        paint: {
          'line-color': [
            'match',
            ['get', 'congestion'],
            'high',
            '#FF5252',
            'medium',
            '#FFC107',
            'low',
            '#4CAF50',
            '#4CAF50',
          ],
          'line-width': 4,
        },
      });

      addPopupToLayer(
        map,
        'trafficLayer',
        (props) => `
          <h4>${sanitizeHTML(props.title || 'Traffic')}</h4>
          <p>${sanitizeHTML(props.description || '')}</p>
          <p>Congestion: ${sanitizeHTML(props.congestion || 'Low')}</p>
        `
      );
    } catch (err) {
      console.warn('Error loading traffic data:', err);
    }
  };

  // 7) Social
  const loadSocialPosts = async (map: Map) => {
    try {
      const response = await fetch('/data/socialPosts.json');
      if (!response.ok) {
        // optional data
        return;
      }
      
      const data = await response.json();

      map.addSource('socialPosts', { type: 'geojson', data });

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
          'text-anchor': 'top',
        },
        paint: {
          'text-color': '#333',
          'text-halo-color': '#fff',
          'text-halo-width': 1,
        },
      });

      addPopupToLayer(
        map,
        'socialPostsLayer',
        (props) => `
          <h4>${sanitizeHTML(props.platform || 'Social')} Post</h4>
          <p>${sanitizeHTML(props.message || '')}</p>
          <p>User: ${sanitizeHTML(props.user || 'Anonymous')}</p>
          <p>Posted: ${props.timestamp ? new Date(props.timestamp).toLocaleString() : 'Unknown'}</p>
        `
      );

      addHoverEffect(map, 'socialPostsLayer');
    } catch (err) {
      console.warn('Error loading social posts:', err);
    }
  };

  // ----------------------------------------------
  // SHARED UTILITY FOR POPUPS & HOVER
  // ----------------------------------------------
  const addPopupToLayer = (
    map: Map,
    layerId: string,
    contentFn: (props: Record<string, any>) => string
  ) => {
    map.on('click', layerId, (e: MapMouseEvent) => {
      if (!e.features || e.features.length === 0) return;
      const feature = e.features[0] as Feature<Point>;
      const coordinates = feature.geometry?.coordinates?.slice() || [0, 0];
      const props = (feature.properties || {}) as Record<string, any>;

      // If the map is zoomed out, ensure correct popup location
      while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
        coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
      }

      new mapboxgl.Popup()
        .setLngLat(coordinates as [number, number])
        .setHTML(contentFn(props))
        .addTo(map);
    });
  };

  const addHoverEffect = (map: Map, layerId: string) => {
    map.on('mouseenter', layerId, () => {
      map.getCanvas().style.cursor = 'pointer';
    });
    map.on('mouseleave', layerId, () => {
      map.getCanvas().style.cursor = '';
    });
  };

  // ----------------------------------------------
  // TOGGLE LAYERS
  // ----------------------------------------------
  const toggleLayer = (layerId: 'webcams' | 'counties') => {
    if (!mapRef.current) return;
    const map = mapRef.current;

    const newVisibility = !layerVisibility[layerId];
    setLayerVisibility((prev) => ({ ...prev, [layerId]: newVisibility }));

    // Convert boolean -> 'visible' / 'none'
    const visibilityValue = newVisibility ? 'visible' : 'none';

    // Our actual Mapbox layer IDs:
    //  - 'webcams' => 'webcamsLayer'
    //  - 'counties' => 'countiesLayer'
    let actualLayerId = '';
    if (layerId === 'webcams') actualLayerId = 'webcamsLayer';
    else if (layerId === 'counties') actualLayerId = 'countiesLayer';

    if (map.getLayer(actualLayerId)) {
      map.setLayoutProperty(actualLayerId, 'visibility', visibilityValue);
    }
  };

  // ----------------------------------------------
  // RENDER
  // ----------------------------------------------
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
      <div className="map-controls">
        <div className="layer-control">
          <label>
            <input
              type="checkbox"
              checked={layerVisibility.counties}
              onChange={() => toggleLayer('counties')}
            />
            County Boundaries
          </label>
        </div>
        <div className="layer-control">
          <label>
            <input
              type="checkbox"
              checked={layerVisibility.webcams}
              onChange={() => toggleLayer('webcams')}
            />
            Webcams
          </label>
        </div>
      </div>
    </div>
  );
};

export default MapView;
