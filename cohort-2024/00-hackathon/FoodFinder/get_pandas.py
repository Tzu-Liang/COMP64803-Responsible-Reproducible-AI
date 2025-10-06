import pandas as pd
import json


def json_to_pandas_row(json_data):
    """
    Transforms a JSON object (dictionary) into a Pandas DataFrame row.

    Args:
        json_data (dict): The JSON object to transform.

    Returns:
        pandas.DataFrame: A DataFrame with a single row representing the JSON data.
    """

    # Flatten nested dictionaries and lists as needed.
    # You can customize this part based on how you want to represent the data in columns.
    data_row = {
        "id": json_data.get("id"),
        "types": ", ".join(json_data.get("types", [])), # Join list to string
        "formattedAddress": json_data.get("formattedAddress"),
        "latitude": json_data.get("location", {}).get("latitude"), # Access nested keys safely
        "longitude": json_data.get("location", {}).get("longitude"),
        "rating": json_data.get("rating"),
        "businessStatus": json_data.get("businessStatus"),
        "userRatingCount": json_data.get("userRatingCount"),
        "displayName_text": json_data.get("displayName", {}).get("text"), # Nested displayName
        "displayName_languageCode": json_data.get("displayName", {}).get("languageCode"),
        "takeout": json_data.get("takeout"),
        "delivery": json_data.get("delivery"),
        "dineIn": json_data.get("dineIn"),
        "openNow": json_data.get("currentOpeningHours", {}).get("openNow"), # Nested currentOpeningHours
        "weekdayDescriptions": "\n".join(json_data.get("currentOpeningHours", {}).get("weekdayDescriptions", [])), # Join weekday descriptions with newlines
        "acceptsCreditCards": json_data.get("paymentOptions", {}).get("acceptsCreditCards"), # Nested paymentOptions
        "acceptsDebitCards": json_data.get("paymentOptions", {}).get("acceptsDebitCards"),
        "acceptsCashOnly": json_data.get("paymentOptions", {}).get("acceptsCashOnly"),
        "acceptsNfc": json_data.get("paymentOptions", {}).get("acceptsNfc"),
        "freeParkingLot": json_data.get("parkingOptions", {}).get("freeParkingLot"), # Nested parkingOptions
        "freeStreetParking": json_data.get("parkingOptions", {}).get("freeStreetParking"),
        "spicyLevel": json_data.get("spicy_level"),
        "priceLevel": json_data.get("price_level")
    }

    return pd.DataFrame([data_row]) # Create DataFrame from the single row dictionary

json_file_path = "all_places_response.json"
generated_content = "processed_places_response.json"
with open(json_file_path, 'r') as f:
    places = json.load(f)
places = [place for place in places if place.get("businessStatus") == "OPERATIONAL"]
with open(generated_content, 'r') as f:
    extracted_attributes = json.load(f)
    extracted_attributes = {item['id']: item for item in extracted_attributes}

if places:
    # Initialize an empty DataFrame with the first row
    assert len(places) == len(extracted_attributes), "The number of places and extracted attributes do not match."
    df = json_to_pandas_row(places[0]|extracted_attributes[places[0]['id']])
    
    # Append remaining rows
    for place in places[1:]:
        
        df = pd.concat([df, json_to_pandas_row(place|extracted_attributes[place['id']])], ignore_index=True)
    
    print(df)
else:
    print("The JSON list is empty.")