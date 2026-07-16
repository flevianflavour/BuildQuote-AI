"""
BuildQuote AI

Plumbing Estimator

Calculates:

• Water Pipes
• Waste Pipes
• Toilets
• Wash Basins
• Kitchen Sink
• Shower Mixers
• Floor Traps
• Labour
"""

from costing.county_prices import pricing


DEFAULT_RATES = {

    "Water_Pipe": 250,
    "Waste_Pipe": 450,
    "Toilet": 12000,
    "Wash_Basin": 6500,
    "Kitchen_Sink": 8500,
    "Shower_Mixer": 5500,
    "Floor_Trap": 850,
    "Plumber_Day": 2500

}


def get_rate(county_rates, key, default):

    value = county_rates.get(key)

    if value is None:
        return default

    try:
        return float(value)
    except:
        return default


def estimate_plumbing(

    county,
    bedrooms=3

):

    county_rates = pricing.get_rates(county)

    # ------------------------------------
    # Estimated Quantities
    # ------------------------------------

    if bedrooms == 1:

        water_pipe = 60
        waste_pipe = 35
        toilets = 1
        basins = 1
        showers = 1

    elif bedrooms == 2:

        water_pipe = 90
        waste_pipe = 55
        toilets = 2
        basins = 2
        showers = 2

    elif bedrooms == 3:

        water_pipe = 120
        waste_pipe = 70
        toilets = 3
        basins = 3
        showers = 3

    elif bedrooms == 4:

        water_pipe = 150
        waste_pipe = 90
        toilets = 4
        basins = 4
        showers = 4

    else:

        water_pipe = 200
        waste_pipe = 120
        toilets = 5
        basins = 5
        showers = 5

    kitchen_sink = 1

    floor_traps = toilets + showers

    plumber_days = round((water_pipe + waste_pipe) / 40, 1)

    # ------------------------------------
    # County Rates
    # ------------------------------------

    water_pipe_rate = get_rate(
        county_rates,
        "Water_Pipe",
        DEFAULT_RATES["Water_Pipe"]
    )

    waste_pipe_rate = get_rate(
        county_rates,
        "Waste_Pipe",
        DEFAULT_RATES["Waste_Pipe"]
    )

    toilet_rate = get_rate(
        county_rates,
        "Toilet",
        DEFAULT_RATES["Toilet"]
    )

    basin_rate = get_rate(
        county_rates,
        "Wash_Basin",
        DEFAULT_RATES["Wash_Basin"]
    )

    sink_rate = get_rate(
        county_rates,
        "Kitchen_Sink",
        DEFAULT_RATES["Kitchen_Sink"]
    )

    shower_rate = get_rate(
        county_rates,
        "Shower_Mixer",
        DEFAULT_RATES["Shower_Mixer"]
    )

    trap_rate = get_rate(
        county_rates,
        "Floor_Trap",
        DEFAULT_RATES["Floor_Trap"]
    )

    plumber_rate = get_rate(
        county_rates,
        "Plumber_Day",
        DEFAULT_RATES["Plumber_Day"]
    )    # ------------------------------------
    # Costs
    # ------------------------------------

    water_pipe_cost = water_pipe * water_pipe_rate

    waste_pipe_cost = waste_pipe * waste_pipe_rate

    toilet_cost = toilets * toilet_rate

    basin_cost = basins * basin_rate

    sink_cost = kitchen_sink * sink_rate

    shower_cost = showers * shower_rate

    trap_cost = floor_traps * trap_rate

    labour_cost = plumber_days * plumber_rate

    # ------------------------------------
    # BOQ
    # ------------------------------------

    boq = [

        {
            "description": "Water Pipes",
            "quantity": water_pipe,
            "unit": "Metres",
            "rate": water_pipe_rate,
            "amount": round(water_pipe_cost, 2)
        },

        {
            "description": "Waste Pipes",
            "quantity": waste_pipe,
            "unit": "Metres",
            "rate": waste_pipe_rate,
            "amount": round(waste_pipe_cost, 2)
        },

        {
            "description": "Toilets",
            "quantity": toilets,
            "unit": "Pieces",
            "rate": toilet_rate,
            "amount": round(toilet_cost, 2)
        },

        {
            "description": "Wash Basins",
            "quantity": basins,
            "unit": "Pieces",
            "rate": basin_rate,
            "amount": round(basin_cost, 2)
        },

        {
            "description": "Kitchen Sink",
            "quantity": kitchen_sink,
            "unit": "Piece",
            "rate": sink_rate,
            "amount": round(sink_cost, 2)
        },

        {
            "description": "Shower Mixers",
            "quantity": showers,
            "unit": "Pieces",
            "rate": shower_rate,
            "amount": round(shower_cost, 2)
        },

        {
            "description": "Floor Traps",
            "quantity": floor_traps,
            "unit": "Pieces",
            "rate": trap_rate,
            "amount": round(trap_cost, 2)
        },

        {
            "description": "Plumbing Labour",
            "quantity": plumber_days,
            "unit": "Days",
            "rate": plumber_rate,
            "amount": round(labour_cost, 2)
        }

    ]

    # ------------------------------------
    # Totals
    # ------------------------------------

    subtotal = sum(item["amount"] for item in boq)

    vat = round(subtotal * 0.16, 2)

    total = round(subtotal + vat, 2)

    # ------------------------------------
    # Return
    # ------------------------------------

    return {

        "section": "Plumbing",

        "materials": {

            "water_pipe": water_pipe,
            "waste_pipe": waste_pipe,
            "toilets": toilets,
            "wash_basins": basins,
            "kitchen_sink": kitchen_sink,
            "shower_mixers": showers,
            "floor_traps": floor_traps,

            "water_pipe_cost": round(water_pipe_cost, 2),
            "waste_pipe_cost": round(waste_pipe_cost, 2),
            "toilet_cost": round(toilet_cost, 2),
            "basin_cost": round(basin_cost, 2),
            "sink_cost": round(sink_cost, 2),
            "shower_cost": round(shower_cost, 2),
            "trap_cost": round(trap_cost, 2)

        },

        "labour": {

            "plumber_days": plumber_days,
            "cost": round(labour_cost, 2)

        },

        "boq": boq,

        "subtotal": round(subtotal, 2),

        "vat": vat,

        "total": total

    }


# ------------------------------------
# Test
# ------------------------------------

if __name__ == "__main__":

    from pprint import pprint

    pprint(

        estimate_plumbing(

            county="Mombasa",

            bedrooms=3

        )

    )