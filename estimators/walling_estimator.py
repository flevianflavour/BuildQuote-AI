"""
BuildQuote AI

Walling Estimator

Calculates:
• Wall Area
• Opening Deductions
• Materials
• Labour
• BOQ
"""

from services.material_engine import material_engine
from costing.county_prices import pricing
import pandas as pd


DEFAULT_RATES = {
    "Machine_Cut_Stone": 75,
    "Quarry_Stone": 55,
    "Cement": 850,
    "Sand": 2500,
    "Mason_Day": 1800,
    "Labourer_Day": 1200,
}


def get_rate(county_rates, key, default):

    value = county_rates.get(key)

    if pd.isna(value):
        return default

    return float(value)


def estimate_walling(
    county,
    length,
    width,
    wall_height,
    doors=2,
    windows=4,
    block_type="Machine Cut Stone",
):

    # ======================================
    # WALL AREA
    # ======================================

    perimeter = 2 * (length + width)

    gross_wall_area = perimeter * wall_height

    door_area = doors * 2.1 * 0.9

    window_area = windows * 1.2 * 1.2

    opening_area = door_area + window_area

    net_wall_area = gross_wall_area - opening_area

    # ======================================
    # MATERIAL QUANTITIES
    # ======================================

    materials = material_engine.wall_materials(
        net_wall_area,
        block_type,
    )

    # ======================================
    # COUNTY RATES
    # ======================================

    county_rates = pricing.get_rates(county)

    if block_type == "Machine Cut Stone":

        block_rate = get_rate(
            county_rates,
            "Machine_Cut_Stone",
            DEFAULT_RATES["Machine_Cut_Stone"],
        )

    else:

        block_rate = get_rate(
            county_rates,
            "Quarry_Stone",
            DEFAULT_RATES["Quarry_Stone"],
        )

    cement_rate = get_rate(
        county_rates,
        "Cement",
        DEFAULT_RATES["Cement"],
    )

    sand_rate = get_rate(
        county_rates,
        "Sand",
        DEFAULT_RATES["Sand"],
    )

    mason_rate = get_rate(
        county_rates,
        "Mason_Day",
        DEFAULT_RATES["Mason_Day"],
    )

    labourer_rate = get_rate(
        county_rates,
        "Labourer_Day",
        DEFAULT_RATES["Labourer_Day"],
    )

    # ======================================
    # COSTS
    # ======================================

    block_cost = materials["blocks"] * block_rate

    cement_cost = materials["cement_bags"] * cement_rate

    sand_cost = materials["sand_m3"] * sand_rate

    mason_days = round(net_wall_area / 15, 1)

    labourer_days = round(net_wall_area / 20, 1)

    labour_cost = (
        mason_days * mason_rate
        + labourer_days * labourer_rate
    )

    # ======================================
    # BOQ
    # ======================================

    boq = [

        {
            "description": block_type,
            "quantity": materials["blocks"],
            "unit": "Pieces",
            "rate": block_rate,
            "amount": round(block_cost, 2),
        },

        {
            "description": "Cement",
            "quantity": materials["cement_bags"],
            "unit": "Bags",
            "rate": cement_rate,
            "amount": round(cement_cost, 2),
        },

        {
            "description": "Sand",
            "quantity": materials["sand_m3"],
            "unit": "m³",
            "rate": sand_rate,
            "amount": round(sand_cost, 2),
        },

        {
            "description": "Walling Labour",
            "quantity": mason_days + labourer_days,
            "unit": "Days",
            "rate": mason_rate,
            "amount": round(labour_cost, 2),
        },

    ]

    subtotal = sum(item["amount"] for item in boq)

    vat = subtotal * 0.16

    total = subtotal + vat

    return {

        "section": "Walling",

        "gross_wall_area": round(gross_wall_area, 2),

        "opening_area": round(opening_area, 2),

        "net_wall_area": round(net_wall_area, 2),

        "materials": {

            "blocks": materials["blocks"],

            "cement_bags": materials["cement_bags"],

            "sand_m3": materials["sand_m3"],

            "block_cost": round(block_cost, 2),

            "cement_cost": round(cement_cost, 2),

            "sand_cost": round(sand_cost, 2),

        },

        "labour": {

            "mason_days": mason_days,

            "labourer_days": labourer_days,

            "cost": round(labour_cost, 2),

        },

        "boq": boq,

        "subtotal": round(subtotal, 2),

        "vat": round(vat, 2),

        "total": round(total, 2),

    }


class WallingEstimator:

    def estimate(
        self,
        county,
        length,
        width,
        wall_height,
        doors=2,
        windows=4,
        block_type="Machine Cut Stone",
    ):

        return estimate_walling(
            county=county,
            length=length,
            width=width,
            wall_height=wall_height,
            doors=doors,
            windows=windows,
            block_type=block_type,
        )


if __name__ == "__main__":

    from pprint import pprint

    pprint(
        estimate_walling(
            county="Mombasa",
            length=10,
            width=12,
            wall_height=3,
        )
    )