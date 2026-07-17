"""
BuildQuote AI

Doors & Windows Estimator

Calculates:

• External Doors
• Internal Doors
• Windows
• Frames
• Locks
• Labour
• BOQ
"""


# ==================================================
# IMPORTS
# ==================================================

try:

    from costing.county_prices import pricing

except ImportError:

    pricing = None





# ==================================================
# DEFAULT RATES
# ==================================================

DEFAULT_RATES = {


    "External_Door":25000,

    "Internal_Door":12000,

    "Window":15000,

    "Frame":4500,

    "Door_Lock":2500,

    "Carpenter_Day":2200

}





# ==================================================
# RATE HANDLER
# ==================================================

def get_rate(county_rates,key,default):


    if not county_rates:

        return default



    value = county_rates.get(key)



    if value is None:

        return default



    try:

        return float(value)

    except:

        return default





# ==================================================
# MAIN ESTIMATOR
# ==================================================

def estimate_doors_windows(

    county,

    bedrooms=3

):


    # ----------------------------------------------
    # County Rates
    # ----------------------------------------------

    if pricing:

        county_rates = pricing.get_rates(county)

    else:

        county_rates = {}




    # ----------------------------------------------
    # Quantities
    # ----------------------------------------------

    if bedrooms == 1:


        external_doors = 1

        internal_doors = 4

        windows = 8



    elif bedrooms == 2:


        external_doors = 2

        internal_doors = 6

        windows = 12



    elif bedrooms == 3:


        external_doors = 2

        internal_doors = 8

        windows = 16



    elif bedrooms == 4:


        external_doors = 2

        internal_doors = 10

        windows = 20



    else:


        external_doors = 3

        internal_doors = 12

        windows = 24





    frames = (

        external_doors

        +

        internal_doors

    )



    locks = frames



    carpenter_days = round(

        (frames + windows) / 4,

        1

    )





    # ----------------------------------------------
    # Rates
    # ----------------------------------------------

    external_rate = get_rate(

        county_rates,

        "External_Door",

        DEFAULT_RATES["External_Door"]

    )


    internal_rate = get_rate(

        county_rates,

        "Internal_Door",

        DEFAULT_RATES["Internal_Door"]

    )


    window_rate = get_rate(

        county_rates,

        "Window",

        DEFAULT_RATES["Window"]

    )


    frame_rate = get_rate(

        county_rates,

        "Frame",

        DEFAULT_RATES["Frame"]

    )


    lock_rate = get_rate(

        county_rates,

        "Door_Lock",

        DEFAULT_RATES["Door_Lock"]

    )


    carpenter_rate = get_rate(

        county_rates,

        "Carpenter_Day",

        DEFAULT_RATES["Carpenter_Day"]

    )





    # ----------------------------------------------
    # Costs
    # ----------------------------------------------

    external_cost = external_doors * external_rate

    internal_cost = internal_doors * internal_rate

    window_cost = windows * window_rate

    frame_cost = frames * frame_rate

    lock_cost = locks * lock_rate


    labour_cost = (

        carpenter_days

        *

        carpenter_rate

    )



    material_cost = (

        external_cost

        +

        internal_cost

        +

        window_cost

        +

        frame_cost

        +

        lock_cost

    )





    # ----------------------------------------------
    # BOQ
    # ----------------------------------------------

    boq = [


        {

            "description":"External Doors",

            "quantity":external_doors,

            "unit":"Pieces",

            "rate":external_rate,

            "amount":round(external_cost,2)

        },


        {

            "description":"Internal Doors",

            "quantity":internal_doors,

            "unit":"Pieces",

            "rate":internal_rate,

            "amount":round(internal_cost,2)

        },


        {

            "description":"Windows",

            "quantity":windows,

            "unit":"Pieces",

            "rate":window_rate,

            "amount":round(window_cost,2)

        },


        {

            "description":"Door Frames",

            "quantity":frames,

            "unit":"Pieces",

            "rate":frame_rate,

            "amount":round(frame_cost,2)

        },


        {

            "description":"Door Locks",

            "quantity":locks,

            "unit":"Pieces",

            "rate":lock_rate,

            "amount":round(lock_cost,2)

        },


        {

            "description":"Installation Labour",

            "quantity":carpenter_days,

            "unit":"Days",

            "rate":carpenter_rate,

            "amount":round(labour_cost,2)

        }

    ]





    # ----------------------------------------------
    # Totals
    # ----------------------------------------------

    subtotal = sum(

        item["amount"]

        for item in boq

    )


    vat = subtotal * 0.16


    total = subtotal + vat





    return {


        "section":"Doors & Windows",



        "materials":{


            "external_doors":external_doors,


            "internal_doors":internal_doors,


            "windows":windows,


            "frames":frames,


            "locks":locks,


            "cost":round(material_cost,2)

        },



        "labour":{


            "carpenter_days":carpenter_days,


            "cost":round(labour_cost,2)

        },



        "boq":boq,



        "material_total":round(material_cost,2),



        "labour_total":round(labour_cost,2),



        "subtotal":round(subtotal,2),



        "vat":round(vat,2),



        "total":round(total,2),



        "grand_total":round(total,2)

    }





# ==================================================
# CLASS FOR ENGINE
# ==================================================

class DoorsWindowsEstimator:


    def estimate(

        self,

        county,

        bedrooms=3

    ):


        return estimate_doors_windows(

            county,

            bedrooms

        )





# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":


    from pprint import pprint



    pprint(

        estimate_doors_windows(

            county="Mombasa",

            bedrooms=3

        )

    )