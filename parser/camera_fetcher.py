import os
import time
import requests
import json
from dateutil import parser, tz
from datetime import datetime, timedelta

# -------------------------------------------------------------------
# Configuration / Constants
# -------------------------------------------------------------------

ALERT_WILDFIRE_API_URL = "https://data.alertwildfire.org/api/firecams/v0"
#ALERT_WILDFIRE_API_KEY = os.environ.get("ALERT_WILDFIRE_API_KEY")

ALERT_CALIFORNIA_API_URL = "https://data.alertcalifornia.org/api/firecams/v0"
#ALERT_CALIFORNIA_API_KEY = os.environ.get("ALERT_CALIFORNIA_API_KEY")

# Which California cameras from Alert Wildfire do we allow? 
# (If they are not in this set, we skip them, because 
#  the Alert Wildfire CA feeds often aren’t fully functional.)
CALIFORNIA_CAMERAS_TO_KEEP = {
    "Axis-AlderHill",
    "Axis-Alpine",
    "Axis-ArmstrongLookout1",
    "Axis-ArmstrongLookout2",
    "Axis-Babbitt",
    "Axis-BaldCA",
    "Axis-BaldCA2",
    "Axis-BigHill",
    "Axis-Bunker",
    "Axis-Emerald",
    "Axis-CTC",
    "Axis-FallenLeaf",
    "Axis-FortSage",
    "Axis-GoldCountry",
    "Axis-HawkinsPeak",
    "Axis-Heavenly2",
    "Axis-Homewood1",
    "Axis-Homewood2",
    "Axis-KennedyMine",
    "Axis-Leek",
    "Axis-Martis",
    "Axis-MohawkEsmeralda",
    "Axis-Montezuma",
    "Axis-MtDanaher",
    "Axis-MtZion1",
    "Axis-MtZion2",
    "Axis-NorthMok",
    "Axis-Pepperwood1",
    "Axis-QueenBee",
    "Axis-RedCorral",
    "Axis-RedCorral2",
    "Axis-Rockland",
    "Axis-Rockpile",
    "Axis-Sagehen5",
    "Axis-Sierra",
    "Axis-TahoeDonner",
    "Axis-TVHill",
    "Axis-WestPoint",
    "Axis-Winters1",
    "Axis-Winters2",
    "Axis-Konocti",
    "Axis-StHelenaNorth",
    "Axis-PrattMtn2",
    "Axis-PrattMtn1",
    "Axis-PierceMtn2",
    "Axis-PierceMtn1",
}

FOUR_HOURS_AGO = datetime.utcnow() - timedelta(hours=4)

# In-memory cache (optional, if you want to cache results)
CAMERA_CACHE = None
CACHE_TIME   = 0
CACHE_MAX_AGE_MILLIS = 24 * 60 * 60 * 1000  # 24 hours in ms

# -------------------------------------------------------------------
# Helper Functions
# -------------------------------------------------------------------

def valid_cache() -> bool:
    """Return True if our global CAMERA_CACHE is still fresh."""
    return CAMERA_CACHE is not None and (time.time_ns() // 1_000_000 - CACHE_TIME) < CACHE_MAX_AGE_MILLIS

def reset_cache(cameras_geojson):
    """Store cameras_geojson in global cache with current timestamp."""
    global CAMERA_CACHE, CACHE_TIME
    CAMERA_CACHE = cameras_geojson
    CACHE_TIME   = time.time_ns() // 1_000_000

def build_feature(api_name: str, camera_data: dict) -> dict:
    """
    Convert a single camera record from the API into a GeoJSON Feature.
    camera_data keys typically: name, site, position, image, update_time.
    """
    name         = camera_data.get("name")
    site         = camera_data.get("site", {})
    position     = camera_data.get("position", {})
    image        = camera_data.get("image", {})
    update_time  = camera_data.get("update_time")

    # Build the feature
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [site.get("longitude"), site.get("latitude")]
        },
        "properties": {
            "api-name":    api_name,
            "latitude":    site.get("latitude"),
            "longitude":   site.get("longitude"),
            "name":        name,
            "pan":         position.get("pan"),
            "tilt":        position.get("tilt"),
            "state":       site.get("state"),
            "update-time": update_time,
            "image-url":   image.get("url")
        }
    }
    return feature

def is_active_recently(update_time_str: str) -> bool:
    """
    Returns True if the camera has updated within the last 4 hours.
    The API might provide time without time zone or with. 
    We'll parse it in a best-effort manner and compare.
    """
    if not update_time_str:
        return False
    # Attempt parse. If the string lacks a timezone, assume UTC.
    try:
        dt = parser.isoparse(update_time_str)
        # If no tzinfo, assume UTC
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=tz.UTC)
        # Compare to 4 hours ago
        return dt > FOUR_HOURS_AGO.replace(tzinfo=tz.UTC)
    except (parser.ParserError, ValueError):
        # If we can't parse, treat as inactive
        return False

def is_ok_for_alert_wildfire_ca(feature: dict) -> bool:
    """
    For Alert Wildfire cameras in CA, only allow if they are in the 
    'CALIFORNIA_CAMERAS_TO_KEEP' set. If not in CA, it’s fine. 
    """
    props = feature.get("properties", {})
    name  = props.get("name")
    state = props.get("state")
    # If it's not CA, keep it
    if state != "CA":
        return True
    # If state == "CA", keep only if name is in whitelist
    return (name in CALIFORNIA_CAMERAS_TO_KEEP)

def feature_collection(features: list) -> dict:
    """Wrap the list of Feature dicts into a FeatureCollection."""
    return {
        "type": "FeatureCollection",
        "features": features
    }

def fetch_cameras(api_url: str, api_key: str = None) -> list:
    """
    Generic helper to fetch all cameras from a given endpoint.
    Returns list of camera objects (dict).
    """
    headers = {"X-Api-Key": api_key} if api_key else {}
    url = f"{api_url}/cameras"
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()  # returns a list of dict

# -------------------------------------------------------------------
# Main public function
# -------------------------------------------------------------------

def get_cameras() -> dict:
    """
    Builds a GeoJSON FeatureCollection of active cameras from:
    - Alert Wildfire (non-CA or whitelisted CA) 
    - AlertCalifornia
    That have updated in the last 4 hours.
    Results are cached in memory for up to 24 hours.
    """
    global CAMERA_CACHE

    if valid_cache():
        return CAMERA_CACHE

    # 1) Fetch raw camera arrays
    wildfire_raw   = fetch_cameras(ALERT_WILDFIRE_API_URL)
    california_raw = fetch_cameras(ALERT_CALIFORNIA_API_URL)

    # 2) Convert to GeoJSON Features
    wildfire_feats = [build_feature("alert-wildfire",   c) for c in wildfire_raw]
    cali_feats     = [build_feature("alert-california", c) for c in california_raw]

    # 3) Filter out old or disallowed cameras
    #    - If it's an alert-wildfire camera in CA but not whitelisted -> remove
    #    - If older than 4 hours -> remove
    combined = []
    for feat in wildfire_feats:
        if not is_ok_for_alert_wildfire_ca(feat):
            continue
        ts = feat["properties"].get("update-time")
        if is_active_recently(ts):
            combined.append(feat)

    for feat in cali_feats:
        ts = feat["properties"].get("update-time")
        if is_active_recently(ts):
            combined.append(feat)

    # 4) Build final FeatureCollection
    fc = feature_collection(combined)

    # 5) Cache
    reset_cache(fc)
    return fc


def get_current_image(camera_name: str, api_name: str) -> bytes:
    """
    Equivalent to `get-current-image` from Clojure.
    Downloads the latest image for a specific camera from either:
      - alert-wildfire 
      - alert-california
    Returns the raw JPEG bytes.
    """
    if api_name not in ["alert-wildfire", "alert-california"]:
        raise ValueError("Invalid api_name, must be 'alert-wildfire' or 'alert-california'")

    api_url  = ALERT_WILDFIRE_API_URL   if api_name == "alert-wildfire" else ALERT_CALIFORNIA_API_URL
    #api_key  = ALERT_WILDFIRE_API_KEY  if api_name == "alert-wildfire" else ALERT_CALIFORNIA_API_KEY

    headers  = {"X-Api-Key": api_key} if api_key else {}
    endpoint = f"{api_url}/currentimage?name={camera_name}"
    r = requests.get(endpoint, headers=headers, timeout=30)
    r.raise_for_status()
    return r.content  # raw bytes, e.g. JPEG


if __name__ == "__main__":
    """
    Example usage:
      1) Make sure ALERT_WILDFIRE_API_KEY and ALERT_CALIFORNIA_API_KEY 
         are set in your environment (if needed).
      2) python cameras.py
    """
    # Retrieve the combined cameras
    cameras_fc = get_cameras()
    print(f"Found {len(cameras_fc['features'])} cameras after filtering.")
    # Print some example info
    # e.g. show the first camera's name, lat/lon
    if cameras_fc["features"]:
        first_feat = cameras_fc["features"][0]
        props = first_feat["properties"]
        print("First camera name:", props["name"])
        print("Coordinates:", first_feat["geometry"]["coordinates"])

    # For demonstration of `get_current_image`:
    # Suppose we want the raw image bytes for "Axis-Almaden1" from alert-california
    # (Be sure the camera name actually matches one in the dataset.)
    # raw_jpeg = get_current_image("Axis-Almaden1", "alert-california")
    # with open("snapshot.jpg", "wb") as f:
    #     f.write(raw_jpeg)
    # print("Wrote snapshot.jpg")
