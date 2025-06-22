import requests

def fetch_redfin_gis_data():
    api_url = (
        "https://www.redfin.com/stingray/api/gis?"
        "al=1&include_nearby_homes=true&market=socal&mpt=99&num_homes=350"
        "&ord=redfin-recommended-asc&page_number=1&region_id=16904&region_type=6"
        "&sold_within_days=90&start=0&status=9&uipt=1,2,3,4,5,6,7,8&v=8&zoomLevel=8"
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
        ),
        "Referer": "https://www.redfin.com/city/16904/CA/San-Diego/filter/include=sold-3mo",
        "Accept": "*/*"
    }

    try:
        res = requests.get(api_url, headers=headers)
        res.raise_for_status()
        print("Fetched Redfin GIS data successfully.")
        print(res.text[:300])
        return res.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
