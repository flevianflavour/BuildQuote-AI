"""
BuildQuote AI

Walling Estimator

Calculates:
• Wall Area
• Opening Deductions
• Materials
• Labour
• BOQ
• VAT
"""

# ==================================================
# IMPORTS
# ==================================================

try:
    from services.material_engine import material_engine

except ImportError:
    from services.material_service import MaterialService

    material_engine = MaterialService()


try:
    from costing.county_prices import pricing

except ImportError:
    pricing = None


import pandas as pd


# ==================================================
# DEFAULT RATES (KENYA)
# ==================================================

DEFAULT_RATES = {

    "Machine_Cut_Stone": 75,

    "Quarry_Stone": 55,

    "Cement": 850,

    "Sand": 2500,

    "Mason_Day": 1800,

    "Labourer_Day": 1200,

}


# ==================================================
# RATE HELPER
# ==================================================

def get_rate(county_rates, key, default):

    if not county_rates:

        return default


    value = county_rates.get(key)


    if value is None:

        return default


    try:

        if pd.isna(value):

            return default

    except Exception:

        pass


    return float(value)



# ==================================================
# WALLING ESTIMATION FUNCTION
# ==================================================

def estimate_walling(

    county,

    length,

    width,

    wall_height,

    doors=2,

    windows=4,

    block_type="Machine Cut Stone",

):


    # ==================================================
    # WALL AREA
    # ==================================================

    perimeter = 2 * (length + width)


    gross_wall_area = perimeter * wall_height


    door_area = doors * 2.1 * 0.9


    window_area = windows * 1.2 * 1.2


    opening_area = door_area + window_area


    net_wall_area = max(

        gross_wall_area - opening_area,

        0

    )



    # ==================================================
    # MATERIAL REQUIREMENTS
    # ==================================================

    materials = material_engine.wall_materials(

        net_wall_area,

        block_type,

    )



    # ==================================================
    # COUNTY PRICES
    # ==================================================

    if pricing:

        county_rates = pricing.get_rates(county)

    else:

        county_rates = {}



    if block_type == "Machine Cut Stone":

        block_rate = get_rate(

            county_rates,

            "Machine_Cut_Stone",

            DEFAULT_RATES["Machine_Cut_Stone"]

        )

    else:

        block_rate = get_rate(

            county_rates,

            "Quarry_Stone",

            DEFAULT_RATES["Quarry_Stone"]

        )



    cement_rate = get_rate(

        county_rates,

        "Cement",

        DEFAULT_RATES["Cement"]

    )



    sand_rate = get_rate(

        county_rates,

        "Sand",

        DEFAULT_RATES["Sand"]

    )



    mason_rate = get_rate(

        county_rates,

        "Mason_Day",

        DEFAULT_RATES["Mason_Day"]

    )



    labourer_rate = get_rate(

        county_rates,

        "Labourer_Day",

        DEFAULT_RATES["Labourer_Day"]

    )



    # ==================================================
    # MATERIAL COSTS
    # ==================================================

    block_cost = (

        materials["blocks"]

        *

        block_rate

    )


    cement_cost = (

        materials["cement_bags"]

        *

        cement_rate

    )


    sand_cost = (

        materials["sand_m3"]

        *

        sand_rate

    )


    material_total = (

        block_cost

        +

        cement_cost

        +

        sand_cost

    )



    # ==================================================
    # LABOUR COST
    # ==================================================

    mason_days = round(

        net_wall_area / 15,

        1

    )


    labourer_days = round(

        net_wall_area / 20,

        1

    )


    mason_cost = mason_days * mason_rate


    labourer_cost = labourer_days * labourer_rate


    labour_total = (

        mason_cost

        +

        labourer_cost

    )



    # ==================================================
    # BOQ
    # ==================================================

    boq = [


        {

            "description": block_type,

            "quantity": materials["blocks"],

            "unit": "Pieces",

            "rate": block_rate,

            "amount": round(block_cost,2),

        },


        {

            "description": "Cement",

            "quantity": materials["cement_bags"],

            "unit": "Bags",

            "rate": cement_rate,

            "amount": round(cement_cost,2),

        },


        {

            "description": "Sand",

            "quantity": materials["sand_m3"],

            "unit": "m³",

            "rate": sand_rate,

            "amount": round(sand_cost,2),

        },


        {

            "description": "Mason Labour",

            "quantity": mason_days,

            "unit": "Days",

            "rate": mason_rate,

            "amount": round(mason_cost,2),

        },


        {

            "description": "Labourer",

            "quantity": labourer_days,

            "unit": "Days",

            "rate": labourer_rate,

            "amount": round(labourer_cost,2),

        },


    ]



    # ==================================================
    # TOTALS
    # ==================================================

    subtotal = sum(

        item["amount"]

        for item in boq

    )


    vat = subtotal * 0.16


    total = subtotal + vat



    # ==================================================
    # RETURN RESULT
    # ==================================================

    return {


        "section": "Walling",



        "dimensions": {


            "length": length,

            "width": width,

            "height": wall_height,

        },



        "areas": {


            "gross_wall_area": round(gross_wall_area,2),

            "opening_area": round(opening_area,2),

            "net_wall_area": round(net_wall_area,2),

        },



        "materials": {


            "block_type": block_type,


            "blocks": materials["blocks"],


            "cement_bags": materials["cement_bags"],


            "sand_m3": materials["sand_m3"],


            "block_cost": round(block_cost,2),


            "cement_cost": round(cement_cost,2),


            "sand_cost": round(sand_cost,2),


            "total": round(material_total,2),

        },



        "labour": {


            "mason_days": mason_days,


            "labourer_days": labourer_days,


            "mason_cost": round(mason_cost,2),


            "labourer_cost": round(labourer_cost,2),


            "total": round(labour_total,2),

        },



        "boq": boq,



        "material_total": round(material_total,2),


        "labour_total": round(labour_total,2),


        "subtotal": round(subtotal,2),


        "vat": round(vat,2),


        "total": round(total,2),


        "grand_total": round(total,2),

    }



# ==================================================
# CLASS WRAPPER FOR ENGINE
# ==================================================

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



# ==================================================
# TEST
# ==================================================

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