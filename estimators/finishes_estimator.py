"""
BuildQuote AI

Finishes Estimator
"""

from costing.county_prices import pricing
import math


DEFAULT_RATES = {

    "Plaster": 450,
    "Paint": 350,
    "Floor_Tile": 1800,
    "Ceiling_Board": 950,
    "Brandering": 350,
    "Fundi_Day": 2200

}


def get_rate(county_rates, key, default):

    value = county_rates.get(key)

    if value is None:
        return default

    try:

        if math.isnan(float(value)):
            return default

    except:

        pass

    return float(value)


def estimate_finishes(

    county,
    length,
    width,
    wall_height

):

    county_rates = pricing.get_rates(county)

    perimeter = 2 * (length + width)

    wall_area = perimeter * wall_height

    floor_area = length * width

    ceiling_area = floor_area

    internal_plaster = wall_area

    external_plaster = wall_area

    putty = wall_area

    paint = wall_area * 2

    screed = floor_area

    tiles = floor_area

    ceiling_boards = math.ceil(ceiling_area / 2.88)

    brandering = round(ceiling_area * 1.25, 2)

    ceiling_paint = ceiling_area

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

    labour_rate = get_rate(
        county_rates,
        "Fundi_Day",
        DEFAULT_RATES["Fundi_Day"]
    )

    plaster_cost = (internal_plaster + external_plaster) * plaster_rate

    paint_cost = paint * paint_rate

    tile_cost = tiles * tile_rate

    ceiling_cost = ceiling_boards * ceiling_rate

    brandering_cost = brandering * brandering_rate

    labour_days = round((wall_area + floor_area) / 18, 1)

    labour_cost = labour_days * labour_rate

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
            "rate":120,
            "amount":round(putty*120,2)
        },

        {
            "description":"Wall Paint",
            "quantity":round(paint,2),
            "unit":"m²",
            "rate":paint_rate,
            "amount":round(paint_cost,2)
        },

        {
            "description":"Floor Screed",
            "quantity":round(screed,2),
            "unit":"m²",
            "rate":280,
            "amount":round(screed*280,2)
        },

        {
            "description":"Floor Tiles",
            "quantity":round(tiles,2),
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

    subtotal = sum(item["amount"] for item in boq)

    vat = subtotal * 0.16

    total = subtotal + vat

    return {

        "section":"Finishes",

        "wall_area":round(wall_area,2),

        "floor_area":round(floor_area,2),

        "ceiling_area":round(ceiling_area,2),

        "materials":{

            "plaster_area":internal_plaster + external_plaster,

            "paint_area":paint,

            "tiles":tiles,

            "ceiling_boards":ceiling_boards,

            "brandering":brandering

        },

        "labour":{

            "days":labour_days,

            "cost":round(labour_cost,2)

        },

        "boq":boq,

        "subtotal":round(subtotal,2),

        "vat":round(vat,2),

        "total":round(total,2)

    }


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