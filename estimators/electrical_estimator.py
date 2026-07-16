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
"""

from costing.county_prices import pricing


DEFAULT_RATES = {

    "Cable": 180,
    "Conduit": 120,
    "Socket": 450,
    "Switch": 350,
    "Light": 800,
    "Distribution_Board": 8500,
    "Electrician_Day": 2500

}


def get_rate(county_rates, key, default):

    value = county_rates.get(key)

    if value is None:
        return default

    try:
        return float(value)
    except:
        return default


def estimate_electrical(

    county,
    bedrooms=3

):

    county_rates = pricing.get_rates(county)

    # ------------------------------------
    # Estimated Quantities
    # ------------------------------------

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

    electrician_days = round(cable_length / 50, 1)

    # ------------------------------------
    # Rates
    # ------------------------------------

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
    )    # ------------------------------------
    # Costs
    # ------------------------------------

    cable_cost = cable_length * cable_rate

    conduit_cost = conduit_length * conduit_rate

    socket_cost = sockets * socket_rate

    switch_cost = switches * switch_rate

    light_cost = light_points * light_rate

    db_cost = distribution_board * db_rate

    labour_cost = electrician_days * electrician_rate

    # ------------------------------------
    # BOQ
    # ------------------------------------

    boq = [

        {
            "description": "Electrical Cable",
            "quantity": cable_length,
            "unit": "Metres",
            "rate": cable_rate,
            "amount": round(cable_cost, 2)
        },

        {
            "description": "PVC Conduit",
            "quantity": conduit_length,
            "unit": "Metres",
            "rate": conduit_rate,
            "amount": round(conduit_cost, 2)
        },

        {
            "description": "Sockets",
            "quantity": sockets,
            "unit": "Pieces",
            "rate": socket_rate,
            "amount": round(socket_cost, 2)
        },

        {
            "description": "Switches",
            "quantity": switches,
            "unit": "Pieces",
            "rate": switch_rate,
            "amount": round(switch_cost, 2)
        },

        {
            "description": "Light Fittings",
            "quantity": light_points,
            "unit": "Pieces",
            "rate": light_rate,
            "amount": round(light_cost, 2)
        },

        {
            "description": "Distribution Board",
            "quantity": distribution_board,
            "unit": "Piece",
            "rate": db_rate,
            "amount": round(db_cost, 2)
        },

        {
            "description": "Electrical Labour",
            "quantity": electrician_days,
            "unit": "Days",
            "rate": electrician_rate,
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

        "section": "Electrical",

        "materials": {

            "cable_length": cable_length,
            "conduit_length": conduit_length,
            "sockets": sockets,
            "switches": switches,
            "light_points": light_points,
            "distribution_board": distribution_board,

            "cable_cost": round(cable_cost, 2),
            "conduit_cost": round(conduit_cost, 2),
            "socket_cost": round(socket_cost, 2),
            "switch_cost": round(switch_cost, 2),
            "light_cost": round(light_cost, 2),
            "distribution_board_cost": round(db_cost, 2),

        },

        "labour": {

            "electrician_days": electrician_days,
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

        estimate_electrical(

            county="Mombasa",

            bedrooms=3

        )

    )