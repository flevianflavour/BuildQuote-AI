"""
BuildQuote AI

Roof Estimator

Calculates:

• Roof Area
• Timber
• Rafters
• Purlins
• Iron Sheets
• Ridge Caps
• Roofing Nails
• Concrete Roof Volume
• Labour
• BOQ
"""


from costing.county_prices import pricing
import pandas as pd



# ========================================
# DEFAULT RATES
# ========================================

DEFAULT_RATES = {

    "Timber": 65000,

    "Mabati": 950,

    "Tile": 1800,

    "Decra": 2500,

    "Concrete": 3500,

    "Ridge_Cap": 850,

    "Roof_Nails": 350,

    "Carpenter_Day": 2200,

    "Fundi_Day": 1800

}



# ========================================
# ROOF FACTORS
# ========================================

ROOF_FACTORS = {


    "Mabati": {

        "coverage": 2.8,

        "timber_factor": 0.03

    },


    "Tile Roof": {

        "coverage": 2.2,

        "timber_factor": 0.04

    },


    "Decra Roof": {

        "coverage": 2.5,

        "timber_factor": 0.035

    },


    "Concrete Roof": {

        "coverage": 1,

        "timber_factor": 0

    }


}



# ========================================
# RATE HANDLER
# ========================================

def get_rate(county_rates, key, default):

    value = county_rates.get(key)

    if value is None or pd.isna(value):

        return default

    return float(value)




# ========================================
# ROOF ESTIMATOR
# ========================================

def estimate_roof(

    county,

    length,

    width,

    roof_type="Mabati"

):


    roof_config = ROOF_FACTORS.get(

        roof_type,

        ROOF_FACTORS["Mabati"]

    )



    # Roof area including overhang

    roof_area = length * width * 1.15



    # Timber

    timber = round(

        roof_area * roof_config["timber_factor"],

        2

    )



    rafters = round(

        roof_area / 1.2

    )



    purlins = round(

        roof_area / 2

    )




    # Roofing material

    if roof_type == "Concrete Roof":

        iron_sheets = 0

    else:

        iron_sheets = round(

            roof_area / roof_config["coverage"]

        )




    ridge_caps = round(

        length / 3

    )



    nails = round(

        roof_area * 0.08,

        1

    )



    carpenter_days = round(

        roof_area / 25,

        1

    )



    fundi_days = round(

        roof_area / 20,

        1

    )




    # Concrete roof volume

    if roof_type == "Concrete Roof":

        concrete_volume = round(

            roof_area * 0.12,

            2

        )

    else:

        concrete_volume = 0




    # ====================================
    # COUNTY PRICES
    # ====================================

    county_rates = pricing.get_rates(county)




    timber_rate = get_rate(

        county_rates,

        "Timber",

        DEFAULT_RATES["Timber"]

    )




    if roof_type == "Tile Roof":

        roof_rate = get_rate(

            county_rates,

            "Tile",

            DEFAULT_RATES["Tile"]

        )


    elif roof_type == "Decra Roof":

        roof_rate = get_rate(

            county_rates,

            "Decra",

            DEFAULT_RATES["Decra"]

        )


    elif roof_type == "Concrete Roof":

        roof_rate = get_rate(

            county_rates,

            "Concrete",

            DEFAULT_RATES["Concrete"]

        )


    else:

        roof_rate = get_rate(

            county_rates,

            "Mabati",

            DEFAULT_RATES["Mabati"]

        )




    ridge_rate = get_rate(

        county_rates,

        "Ridge_Cap",

        DEFAULT_RATES["Ridge_Cap"]

    )



    nail_rate = get_rate(

        county_rates,

        "Roof_Nails",

        DEFAULT_RATES["Roof_Nails"]

    )



    carpenter_rate = get_rate(

        county_rates,

        "Carpenter_Day",

        DEFAULT_RATES["Carpenter_Day"]

    )



    fundi_rate = get_rate(

        county_rates,

        "Fundi_Day",

        DEFAULT_RATES["Fundi_Day"]

    )




    # ====================================
    # COST CALCULATIONS
    # ====================================


    timber_cost = timber * timber_rate



    if roof_type == "Concrete Roof":

        roof_material_cost = (

            concrete_volume * roof_rate

        )

    else:

        roof_material_cost = (

            iron_sheets * roof_rate

        )



    ridge_cost = ridge_caps * ridge_rate



    nail_cost = nails * nail_rate



    labour_cost = (

        carpenter_days * carpenter_rate

        +

        fundi_days * fundi_rate

    )




    # ====================================
    # BOQ
    # ====================================


    boq = []



    if roof_type == "Concrete Roof":


        boq.append({

            "description": "Concrete Roof",

            "quantity": concrete_volume,

            "unit": "m³",

            "rate": roof_rate,

            "amount": round(
                roof_material_cost,
                2
            )

        })


    else:


        boq.append({

            "description": f"{roof_type} Sheets",

            "quantity": iron_sheets,

            "unit": "Sheets",

            "rate": roof_rate,

            "amount": round(
                roof_material_cost,
                2
            )

        })




    boq.extend([


        {

            "description": "Roof Timber",

            "quantity": timber,

            "unit": "m³",

            "rate": timber_rate,

            "amount": round(
                timber_cost,
                2
            )

        },


        {

            "description": "Ridge Caps",

            "quantity": ridge_caps,

            "unit": "Pieces",

            "rate": ridge_rate,

            "amount": round(
                ridge_cost,
                2
            )

        },


        {

            "description": "Roof Nails",

            "quantity": nails,

            "unit": "Kg",

            "rate": nail_rate,

            "amount": round(
                nail_cost,
                2
            )

        },


        {

            "description": "Roof Labour",

            "quantity": carpenter_days + fundi_days,

            "unit": "Days",

            "rate": 0,

            "amount": round(
                labour_cost,
                2
            )

        }


    ])




    subtotal = sum(

        item["amount"]

        for item in boq

    )


    vat = subtotal * 0.16


    total = subtotal + vat




    material_cost = (

        timber_cost

        +

        roof_material_cost

        +

        ridge_cost

        +

        nail_cost

    )




    # ====================================
    # RETURN
    # ====================================


    return {


        "section": "Roof",


        "roof_type": roof_type,


        "roof_area": round(

            roof_area,

            2

        ),


        "materials": {


            "timber_m3": timber,

            "rafters": rafters,

            "purlins": purlins,

            "iron_sheets": iron_sheets,

            "concrete_volume_m3": concrete_volume,

            "ridge_caps": ridge_caps,

            "roof_nails_kg": nails

        },


        "labour": {


            "carpenter_days": carpenter_days,

            "fundi_days": fundi_days,

            "cost": round(

                labour_cost,

                2

            )

        },



        "cost_summary": {


            "material_cost": round(

                material_cost,

                2

            ),


            "labour_cost": round(

                labour_cost,

                2

            ),


            "total_cost": round(

                total,

                2

            )

        },



        "boq": boq,


        "subtotal": round(

            subtotal,

            2

        ),


        "vat": round(

            vat,

            2

        ),


        "total": round(

            total,

            2

        )

    }




# ========================================
# TEST
# ========================================

if __name__ == "__main__":


    from pprint import pprint



    pprint(

        estimate_roof(

            county="Mombasa",

            length=10,

            width=12,

            roof_type="Mabati"

        )

    )