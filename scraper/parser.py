import pandas as pd
import json

def parse_redfin_json(raw_json):
    try:
        if raw_json.startswith('{}&&'):
            raw_json = raw_json[4:]

        data = json.loads(raw_json)
        homes = data.get("payload", {}).get("homes", [])

        listings = []
        for home in homes:
            listings.append({
                "Address": home.get("streetLine", "N/A") if isinstance(home.get("streetLine"), str) else home.get("streetLine", {}).get("value", "N/A"),
                "City": home.get("city", "N/A"),
                "Price": home.get("price", {}).get("value", "N/A"),
                "Beds": home.get("beds", "N/A"),
                "Baths": home.get("baths", "N/A"),
                "SqFt": home.get("sqFt", {}).get("value", "N/A"),
                "Lot Size": home.get("lotSize", {}).get("value", "N/A"),
                "Year Built": home.get("yearBuilt", "N/A") if isinstance(home.get("yearBuilt"), int) else home.get("yearBuilt", {}).get("value", "N/A"),
                "Sold Date": home.get("soldDate", "N/A"),
                "Listing Status": home.get("mlsStatus", "N/A"),
                "URL": f"https://www.redfin.com{home.get('url', '')}"
            })

        return pd.DataFrame(listings)

    except json.JSONDecodeError as err:
        print(f"Failed to decode JSON: {err}")
        return pd.DataFrame()
