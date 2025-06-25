import pandas as pd
import json
from scraper.utils import normalize_timestamp, safe_get

def parse_redfin_json(raw_json):
    try:
        if raw_json.startswith('{}&&'):
            raw_json = raw_json[4:]

        data = json.loads(raw_json)
        homes = data.get("payload", {}).get("homes", [])

        listings = []
        for home in homes:
            listings.append({
                "Address": safe_get(home, ["streetLine"]),
                "City": safe_get(home, ["city"]),
                "Price": safe_get(home, ["price", "value"]),
                "Beds": safe_get(home, ["beds"]),
                "Baths": safe_get(home, ["baths"]),
                "SqFt": safe_get(home, ["sqFt", "value"]),
                "Lot Size": safe_get(home, ["lotSize", "value"]),
                "Year Built": safe_get(home, ["yearBuilt", "value"], fallback=home.get("yearBuilt")),
                "Sold Date": normalize_timestamp(home.get("soldDate")),
                "Listing Status": safe_get(home, ["mlsStatus"]),
                "URL": f"https://www.redfin.com{home.get('url', '')}"
            })

        return pd.DataFrame(listings)

    except json.JSONDecodeError as err:
        raise ValueError(f"Failed to parse Redfin data: {err}")