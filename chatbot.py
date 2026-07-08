LOCATIONS = [
    "Chennai",
    "Mumbai",
    "Kochi",
    "Goa",
    "Visakhapatnam",
    "Puducherry",
    "Mangalore",
    "Kanyakumari",
    "Tuticorin",
    "Paradip",
    "Puri",
    "Kollam",
    "Alappuzha",
    "Karwar",
    "Veraval"
]


def process_query(query):

    q = query.lower()

    result = {
    "intent": None,
    "parameter": None,
    "location": None,
    "locations": []
    }

    if "sst" in q or "temperature" in q:
        result["parameter"] = "SST"

    elif "salinity" in q:
        result["parameter"] = "Salinity"

    elif "wave" in q:
        result["parameter"] = "WaveHeight"

    if "compare" in q:
        result["intent"] = "compare"

    elif "highest" in q:
        result["intent"] = "highest"

    elif "average" in q:
        result["intent"] = "average"

    elif "show" in q:
        if result["parameter"] is None:
            result["intent"] = "data"
        else:
            result["intent"] = None

    elif "data" in q:
        result["intent"] = "data"

    elif "help" in q:
        result["intent"] = "help"

    for city in LOCATIONS:
    if city.lower() in q:
        result["locations"].append(city)

    if len(result["locations"]) == 1:
        result["location"] = result["locations"][0]

    if result["location"] is not None and result["intent"] is None:
        result["intent"] = "data"

    return result