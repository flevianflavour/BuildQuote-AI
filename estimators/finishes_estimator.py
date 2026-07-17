"""
BuildQuote AI

Finishes Estimator

Calculates:

• Plaster
• Paint
• Tiles
• Ceiling
• Brandering
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


import math



# ==================================================
# DEFAULT RATES
# ==================================================

DEFAULT_RATES = {

    "Plaster": 450,

    "Paint": 350,

    "Floor_Tile": 1800,

    "Ceiling_Board": 950,

    "Brandering": 350,

    "Wall_Putty": 120,

    "Floor_Screed": 280,

    "Fundi_Day": 2200

}




# ==================================================
# RATE HANDLER
# ==================================================

def get_rate(county_rates, key, default):


    if not county_rates:

        return default


    value = county_rates.get(key)


    if value is None:

        return default


    try:

        if math.isnan(float(value)):

            return default

    except:

        pass


    return float(value)




# ==================================================
# FINISHES ESTIMATOR
# ==================================================

def estimate_finishes(

    county,

    length,

    width,

    wall_height

):


    # ==================================================
    # COUNTY RATES
    # ==================================================

    if pricing:

        county_rates = pricing.get_rates(county)

    else:

        county_rates = {}




    # ==================================================
    # AREAS
    # ==================================================

    perimeter = 2 * (length + width)


    wall_area = perimeter * wall_height


    floor_area = length * width


    ceiling_area = floor_area



    internal_plaster = wall_area


    external_plaster = wall_area


    putty = wall_area



    paint_area = wall_area * 2


    screed_area = floor_area


    tile_area = floor_area



    ceiling_boards = math.ceil(

        ceiling_area / 2.88

    )


    brandering = round(

        ceiling_area * 1.25,

        2

    )



    ceiling_paint = ceiling_area




    # ==================================================
    # RATES
    # ==================================================

    plaster_rate = get_rate(

        county_rates,

        "Plaster",

        DEFAULT_RATES["Plaster"]

    )



    paint_rate = get_rate(

        county_rates,

        "Paint",

        DEFAULT_RATES["Paint"]

    )



    tile_rate = get_rate(

        county_rates,

        "Floor_Tile",

        DEFAULT_RATES["Floor_Tile"]

    )



    ceiling_rate = get_rate(

        county_rates,

        "Ceiling_Board",

        DEFAULT_RATES["Ceiling_Board"]

    )



    brandering_rate = get_rate(

        county_rates,

        "Brandering",

        DEFAULT_RATES["Brandering"]

    )



    putty_rate = get_rate(

        county_rates,

        "Wall_Putty",

        DEFAULT_RATES["Wall_Putty"]

    )



    screed_rate = get_rate(

        county_rates,

        "Floor_Screed",

        DEFAULT_RATES["Floor_Screed"]

    )



    labour_rate = get_rate(

        county_rates,

        "Fundi_Day",

        DEFAULT_RATES["Fundi_Day"]

    )




    # ==================================================
    # COSTING
    # ==================================================

    plaster_cost = (

        internal_plaster

        +

        external_plaster

    ) * plaster_rate



    putty_cost = putty * putty_rate



    paint_cost = paint_area * paint_rate



    screed_cost = screed_area * screed_rate



    tile_cost = tile_area * tile_rate



    ceiling_cost = ceiling_boards * ceiling_rate



    brandering_cost = brandering * brandering_rate



    labour_days = round(

        (wall_area + floor_area) / 18,

        1

    )



    labour_cost = labour_days * labour_rate




    material_cost = (

        plaster_cost

        +

        putty_cost

        +

        paint_cost

        +

        screed_cost

        +

        tile_cost

        +

        ceiling_cost

        +

        brandering_cost

    )




    # ==================================================
    # BOQ
    # ==================================================

    boq = [


        {

            "description":"Internal Plaster",

            "quantity":round(internal_plaster,2),

            "unit":"m²",

            "rate":plaster_rate,

            "amount":round(internal_plaster*plaster_rate,2)

        },


        {

            "description":"External Plaster",

            "quantity":round(external_plaster,2),

            "unit":"m²",

            "rate":plaster_rate,

            "amount":round(external_plaster*plaster_rate,2)

        },


        {

            "description":"Wall Putty",

            "quantity":round(putty,2),

            "unit":"m²",

            "rate":putty_rate,

            "amount":round(putty*putty_rate,2)

        },


        {

            "description":"Wall Paint",

            "quantity":round(paint_area,2),

            "unit":"m²",

            "rate":paint_rate,

            "amount":round(paint_cost,2)

        },


        {

            "description":"Floor Screed",

            "quantity":round(screed_area,2),

            "unit":"m²",

            "rate":screed_rate,

            "amount":round(screed_cost,2)

        },


        {

            "description":"Floor Tiles",

            "quantity":round(tile_area,2),

            "unit":"m²",

            "rate":tile_rate,

            "amount":round(tile_cost,2)

        },


        {

            "description":"Ceiling Boards",

            "quantity":ceiling_boards,

            "unit":"Pieces",

            "rate":ceiling_rate,

            "amount":round(ceiling_cost,2)

        },


        {

            "description":"Brandering",

            "quantity":brandering,

            "unit":"Metres",

            "rate":brandering_rate,

            "amount":round(brandering_cost,2)

        },


        {

            "description":"Ceiling Paint",

            "quantity":round(ceiling_paint,2),

            "unit":"m²",

            "rate":paint_rate,

            "amount":round(ceiling_paint*paint_rate,2)

        },


        {

            "description":"Finishes Labour",

            "quantity":labour_days,

            "unit":"Days",

            "rate":labour_rate,

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


        "section":"Finishes",



        "dimensions":{

            "length":length,

            "width":width,

            "height":wall_height

        },



        "areas":{

            "wall_area":round(wall_area,2),

            "floor_area":round(floor_area,2),

            "ceiling_area":round(ceiling_area,2)

        },



        "materials":{

            "plaster_area":round(

                internal_plaster + external_plaster,

                2

            ),

            "paint_area":round(paint_area,2),

            "tiles":round(tile_area,2),

            "ceiling_boards":ceiling_boards,

            "brandering":brandering,

            "cost":round(material_cost,2)

        },



        "labour":{

            "days":labour_days,

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

class FinishesEstimator:


    def estimate(

        self,

        county,

        length,

        width,

        wall_height

    ):


        return estimate_finishes(

            county=county,

            length=length,

            width=width,

            wall_height=wall_height

        )





# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":


    from pprint import pprint


    pprint(

        estimate_finishes(

            county="Mombasa",

            length=10,

            width=12,

            wall_height=3

        )

    )