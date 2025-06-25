import requests
from config.constants import BASE_URL, DEFAULT_HEADERS

def fetch_redfin_data(city, status, beds, max_price=None):
    if status not in {"sold", "active"}:
        raise ValueError("Status must be either 'sold' or 'active'")
    #parameters
    params = {
        "al": 1,
        "market": "socal",
        "status": 9 if status == "sold" else 1,
        "uipt": "1,2,3,4,5,6,7,8",
        "num_homes": 350,
        "include_nearby_homes": "true",
        "mpt": 99,
        "ord": "redfin-recommended-asc",
        "page_number": 1,
        "region_id": 16904, 
        "region_type": 6,
        "start": 0,
        "v": 8,
        "zoomLevel": 8
    }

    try:
        response = requests.get(BASE_URL, headers=DEFAULT_HEADERS, params=params)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch Redfin data for {city}: {e}")