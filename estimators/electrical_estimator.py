"""
BuildQuote AI

Electrical Estimator

Calculates:

• Electrical Cable
• PVC Conduit
• Sockets
• Switches
• Light Points
• Distribution Board
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


    "Cable":180,

    "Conduit":120,

    "Socket":450,

    "Switch":350,

    "Light":800,

    "Distribution_Board":8500,

    "Electrician_Day":2500

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
# ELECTRICAL ESTIMATOR
# ==================================================

def estimate_electrical(

    county,

    bedrooms=3

):


    # ==================================================
    # COUNTY RATES
    # ==================================================

    if pricing:

        county_rates = pricing.get_rates(county)

    else:

        county_rates = {}




    # ==================================================
    # QUANTITIES
    # ==================================================

    if bedrooms == 1:


        cable_length = 120

        conduit_length = 120

        sockets = 10

        switches = 8

        light_points = 8



    elif bedrooms == 2:


        cable_length = 170

        conduit_length = 170

        sockets = 16

        switches = 12

        light_points = 12



    elif bedrooms == 3:


        cable_length = 240

        conduit_length = 240

        sockets = 22

        switches = 18

        light_points = 18



    elif bedrooms == 4:


        cable_length = 300

        conduit_length = 300

        sockets = 28

        switches = 22

        light_points = 24



    else:


        cable_length = 380

        conduit_length = 380

        sockets = 36

        switches = 28

        light_points = 30




    distribution_board = 1



    electrician_days = round(

        cable_length / 50,

        1

    )





    # ==================================================
    # RATES
    # ==================================================

    cable_rate = get_rate(

        county_rates,

        "Cable",

        DEFAULT_RATES["Cable"]

    )


    conduit_rate = get_rate(

        county_rates,

        "Conduit",

        DEFAULT_RATES["Conduit"]

    )


    socket_rate = get_rate(

        county_rates,

        "Socket",

        DEFAULT_RATES["Socket"]

    )


    switch_rate = get_rate(

        county_rates,

        "Switch",

        DEFAULT_RATES["Switch"]

    )


    light_rate = get_rate(

        county_rates,

        "Light",

        DEFAULT_RATES["Light"]

    )


    db_rate = get_rate(

        county_rates,

        "Distribution_Board",

        DEFAULT_RATES["Distribution_Board"]

    )


    electrician_rate = get_rate(

        county_rates,

        "Electrician_Day",

        DEFAULT_RATES["Electrician_Day"]

    )





    # ==================================================
    # COSTS
    # ==================================================

    cable_cost = cable_length * cable_rate


    conduit_cost = conduit_length * conduit_rate


    socket_cost = sockets * socket_rate


    switch_cost = switches * switch_rate


    light_cost = light_points * light_rate


    db_cost = distribution_board * db_rate


    labour_cost = electrician_days * electrician_rate



    material_cost = (

        cable_cost

        +

        conduit_cost

        +

        socket_cost

        +

        switch_cost

        +

        light_cost

        +

        db_cost

    )





    # ==================================================
    # BOQ
    # ==================================================

    boq = [


        {

            "description":"Electrical Cable",

            "quantity":cable_length,

            "unit":"Metres",

            "rate":cable_rate,

            "amount":round(cable_cost,2)

        },


        {

            "description":"PVC Conduit",

            "quantity":conduit_length,

            "unit":"Metres",

            "rate":conduit_rate,

            "amount":round(conduit_cost,2)

        },


        {

            "description":"Sockets",

            "quantity":sockets,

            "unit":"Pieces",

            "rate":socket_rate,

            "amount":round(socket_cost,2)

        },


        {

            "description":"Switches",

            "quantity":switches,

            "unit":"Pieces",

            "rate":switch_rate,

            "amount":round(switch_cost,2)

        },


        {

            "description":"Light Fittings",

            "quantity":light_points,

            "unit":"Pieces",

            "rate":light_rate,

            "amount":round(light_cost,2)

        },


        {

            "description":"Distribution Board",

            "quantity":distribution_board,

            "unit":"Piece",

            "rate":db_rate,

            "amount":round(db_cost,2)

        },


        {

            "description":"Electrical Labour",

            "quantity":electrician_days,

            "unit":"Days",

            "rate":electrician_rate,

            "amount":round(labour_cost,2)

        }

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
    # RETURN
    # ==================================================

    return {


        "section":"Electrical",



        "house_size":{


            "bedrooms":bedrooms

        },



        "materials":{


            "cable_length":cable_length,


            "conduit_length":conduit_length,


            "sockets":sockets,


            "switches":switches,


            "light_points":light_points,


            "distribution_board":distribution_board,


            "cost":round(material_cost,2)

        },



        "labour":{


            "electrician_days":electrician_days,


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
# ENGINE CLASS
# ==================================================

class ElectricalEstimator:


    def estimate(

        self,

        county,

        bedrooms=3

    ):


        return estimate_electrical(

            county=county,

            bedrooms=bedrooms

        )





# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":


    from pprint import pprint



    pprint(

        estimate_electrical(

            county="Mombasa",

            bedrooms=3

        )

    )