"""
BuildQuote AI
Foundation Estimator v2

Uses county pricing when available.
Falls back to default rates if a county rate is missing.
"""

import math
import pandas as pd
from costing.county_prices import pricing


# --------------------------------------------------
# DEFAULT RATES
# Used only if county CSV has no value.
# --------------------------------------------------

DEFAULT_RATES = {

    "Excavation": 950,
    "Hardcore": 3400,
    "Blinding": 14500,
    "Concrete": 16000,
    "Backfilling": 700,
    "DPC": 350,
    "Anti_Termite": 120

}


# --------------------------------------------------
# GET RATE
# --------------------------------------------------

def get_rate(county_rates, key, default):

    value = county_rates.get(key)

    if pd.isna(value):
        return default

    if value == "":
        return default

    return float(value)


# --------------------------------------------------
# FOUNDATION ESTIMATOR
# --------------------------------------------------

def estimate_foundation(

    county,

    length,

    width,

    trench_width=0.60,

    trench_depth=1.20,

    hardcore_thickness=0.15,

    blinding_thickness=0.05,

    concrete_thickness=0.25,

):

    county_rates = pricing.get_rates(county)

    excavation_rate = get_rate(
        county_rates,
        "Excavation",
        DEFAULT_RATES["Excavation"]
    )

    hardcore_rate = get_rate(
        county_rates,
        "Hardcore",
        DEFAULT_RATES["Hardcore"]
    )

    blinding_rate = get_rate(
        county_rates,
        "Blinding",
        DEFAULT_RATES["Blinding"]
    )

    concrete_rate = get_rate(
        county_rates,
        "Concrete",
        DEFAULT_RATES["Concrete"]
    )

    backfill_rate = get_rate(
        county_rates,
        "Backfilling",
        DEFAULT_RATES["Backfilling"]
    )

    dpc_rate = get_rate(
        county_rates,
        "DPC_m",
        DEFAULT_RATES["DPC"]
    )

    anti_termite_rate = get_rate(
        county_rates,
        "Anti_Termite_m2",
        DEFAULT_RATES["Anti_Termite"]
    )

    # ----------------------------------------

    perimeter = 2 * (length + width)

    building_area = length * width

    excavation_volume = (
        perimeter *
        trench_width *
        trench_depth
    )

    hardcore_volume = (
        perimeter *
        trench_width *
        hardcore_thickness
    )

    blinding_volume = (
        perimeter *
        trench_width *
        blinding_thickness
    )

    concrete_volume = (
        perimeter *
        trench_width *
        concrete_thickness
    )

    backfill_volume = max(
        excavation_volume
        - hardcore_volume
        - blinding_volume
        - concrete_volume,
        0
    )

    dpc_length = perimeter

    anti_termite_area = building_area

    boq = [

        {
            "description": "Excavation",
            "quantity": round(excavation_volume,2),
            "unit": "m³",
            "rate": excavation_rate,
            "amount": round(excavation_volume * excavation_rate,2)
        },

        {
            "description": "Hardcore Filling",
            "quantity": round(hardcore_volume,2),
            "unit": "m³",
            "rate": hardcore_rate,
            "amount": round(hardcore_volume * hardcore_rate,2)
        },

        {
            "description": "Blinding Concrete",
            "quantity": round(blinding_volume,2),
            "unit": "m³",
            "rate": blinding_rate,
            "amount": round(blinding_volume * blinding_rate,2)
        },

        {
            "description": "Foundation Concrete",
            "quantity": round(concrete_volume,2),
            "unit": "m³",
            "rate": concrete_rate,
            "amount": round(concrete_volume * concrete_rate,2)
        },

        {
            "description": "Backfilling",
            "quantity": round(backfill_volume,2),
            "unit": "m³",
            "rate": backfill_rate,
            "amount": round(backfill_volume * backfill_rate,2)
        },

        {
            "description": "Damp Proof Course",
            "quantity": round(dpc_length,2),
            "unit": "m",
            "rate": dpc_rate,
            "amount": round(dpc_length * dpc_rate,2)
        },

        {
            "description": "Anti-Termite Treatment",
            "quantity": round(anti_termite_area,2),
            "unit": "m²",
            "rate": anti_termite_rate,
            "amount": round(
                anti_termite_area * anti_termite_rate,
                2
            )
        }

    ]

    subtotal = sum(item["amount"] for item in boq)

    vat = subtotal * 0.16

    total = subtotal + vat

    return {

        "county": county,

        "perimeter": round(perimeter,2),

        "building_area": round(building_area,2),

        "boq": boq,

        "subtotal": round(subtotal,2),

        "vat": round(vat,2),

        "total": round(total,2)

    }


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":

    result = estimate_foundation(

        county="Mombasa",

        length=10,

        width=12

    )

    from pprint import pprint

    pprint(result)