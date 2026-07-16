"""
BuildQuote AI
Foundation Estimator v3

Professional foundation BOQ estimator.

Calculates:
- Excavation
- Hardcore Filling
- Blinding Concrete
- Reinforced Concrete
- Backfilling
- Damp Proof Course (DPC)
- Anti-Termite Treatment

Uses county-specific rates where available.
Falls back to default rates when a county rate is missing.
"""

import pandas as pd
from costing.county_prices import pricing


# ==================================================
# DEFAULT RATES (KES)
# ==================================================

DEFAULT_RATES = {
    "Excavation": 950,
    "Hardcore": 3400,
    "Blinding": 14500,
    "Concrete": 16000,
    "Backfilling": 700,
    "DPC_m": 350,
    "Anti_Termite_m2": 120,
}


# ==================================================
# GET COUNTY RATE
# ==================================================

def get_rate(county_rates, key):
    """
    Return county rate if available,
    otherwise use default.
    """

    value = county_rates.get(key)

    if pd.isna(value) or value == "":
        return DEFAULT_RATES[key]

    return float(value)


# ==================================================
# FOUNDATION ESTIMATOR
# ==================================================

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

    perimeter = 2 * (length + width)

    building_area = length * width

    excavation_volume = perimeter * trench_width * trench_depth

    hardcore_volume = perimeter * trench_width * hardcore_thickness

    blinding_volume = perimeter * trench_width * blinding_thickness

    concrete_volume = perimeter * trench_width * concrete_thickness

    backfill_volume = max(
        excavation_volume
        - hardcore_volume
        - blinding_volume
        - concrete_volume,
        0,
    )

    dpc_length = perimeter

    anti_termite_area = building_area

    boq = [

        {
            "description": "Excavation",
            "quantity": round(excavation_volume, 2),
            "unit": "m³",
            "rate": get_rate(county_rates, "Excavation"),
            "amount": round(
                excavation_volume *
                get_rate(county_rates, "Excavation"),
                2,
            ),
        },

        {
            "description": "Hardcore Filling",
            "quantity": round(hardcore_volume, 2),
            "unit": "m³",
            "rate": get_rate(county_rates, "Hardcore"),
            "amount": round(
                hardcore_volume *
                get_rate(county_rates, "Hardcore"),
                2,
            ),
        },

        {
            "description": "Blinding Concrete",
            "quantity": round(blinding_volume, 2),
            "unit": "m³",
            "rate": get_rate(county_rates, "Blinding"),
            "amount": round(
                blinding_volume *
                get_rate(county_rates, "Blinding"),
                2,
            ),
        },

        {
            "description": "Foundation Concrete",
            "quantity": round(concrete_volume, 2),
            "unit": "m³",
            "rate": get_rate(county_rates, "Concrete"),
            "amount": round(
                concrete_volume *
                get_rate(county_rates, "Concrete"),
                2,
            ),
        },

        {
            "description": "Backfilling",
            "quantity": round(backfill_volume, 2),
            "unit": "m³",
            "rate": get_rate(county_rates, "Backfilling"),
            "amount": round(
                backfill_volume *
                get_rate(county_rates, "Backfilling"),
                2,
            ),
        },

        {
            "description": "Damp Proof Course (DPC)",
            "quantity": round(dpc_length, 2),
            "unit": "m",
            "rate": get_rate(county_rates, "DPC_m"),
            "amount": round(
                dpc_length *
                get_rate(county_rates, "DPC_m"),
                2,
            ),
        },

        {
            "description": "Anti-Termite Treatment",
            "quantity": round(anti_termite_area, 2),
            "unit": "m²",
            "rate": get_rate(county_rates, "Anti_Termite_m2"),
            "amount": round(
                anti_termite_area *
                get_rate(county_rates, "Anti_Termite_m2"),
                2,
            ),
        },

    ]

    subtotal = sum(item["amount"] for item in boq)

    vat = subtotal * 0.16

    total = subtotal + vat

    return {
        "county": county,
        "perimeter": round(perimeter, 2),
        "building_area": round(building_area, 2),
        "boq": boq,
        "subtotal": round(subtotal, 2),
        "vat": round(vat, 2),
        "total": round(total, 2),
    }


# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    from pprint import pprint

    pprint(
        estimate_foundation(
            county="Mombasa",
            length=10,
            width=12,
        )
    )