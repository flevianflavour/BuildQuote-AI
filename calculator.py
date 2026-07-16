"""
BuildQuote AI

Main Calculation Engine
"""

from estimators.foundation_estimator import estimate_foundation
from estimators.walling_estimator import estimate_walling
from estimators.roof_estimator import estimate_roof
from estimators.finishes_estimator import estimate_finishes
from estimators.electrical_estimator import estimate_electrical
from estimators.plumbing_estimator import estimate_plumbing
from estimators.doors_windows_estimator import estimate_doors_windows

from costing.cost_engine import CostEngine


# ==================================================
# HOUSE TYPE TO BEDROOM MAPPING
# ==================================================

HOUSE_BEDROOM_MAP = {

    "Bedsitter": 1,
    "1 Bedroom": 1,
    "2 Bedroom": 2,
    "3 Bedroom": 3,
    "4 Bedroom": 4,
    "Maisonette": 4,
    "Villa": 5,

}


def generate_estimate(
    county,
    project_type,
    length,
    width,
    wall_height,

    house_type="3 Bedroom",

    block_type="Machine Cut Stone",

    roof_type="Mabati",

    bedrooms=None,

    doors=2,

    windows=4,
):


    # ==================================================
    # DETERMINE BEDROOM COUNT
    # ==================================================

    if bedrooms is None:

        bedrooms = HOUSE_BEDROOM_MAP.get(
            house_type,
            3
        )


    # ==================================================
    # FOUNDATION
    # ==================================================

    foundation = estimate_foundation(

        county=county,

        length=length,

        width=width,

    )


    # ==================================================
    # WALLING
    # ==================================================

    walling = estimate_walling(

        county=county,

        length=length,

        width=width,

        wall_height=wall_height,

        doors=doors,

        windows=windows,

        block_type=block_type,

    )


    # ==================================================
    # ROOF
    # ==================================================

    roof = estimate_roof(

        county=county,

        length=length,

        width=width,

        roof_type=roof_type,

    )


    # ==================================================
    # FINISHES
    # ==================================================

    finishes = estimate_finishes(

        county=county,

        length=length,

        width=width,

        wall_height=wall_height,

    )


    # ==================================================
    # ELECTRICAL
    # ==================================================

    electrical = estimate_electrical(

        county=county,

        bedrooms=bedrooms,

    )


    # ==================================================
    # PLUMBING
    # ==================================================

    plumbing = estimate_plumbing(

        county=county,

        bedrooms=bedrooms,

    )


    # ==================================================
    # DOORS AND WINDOWS
    # ==================================================

    doors_windows = estimate_doors_windows(

        county=county,

        bedrooms=bedrooms,

    )


    # ==================================================
    # COST ENGINE
    # ==================================================

    engine = CostEngine()


    engine.add_section(
        "Foundation",
        foundation
    )

    engine.add_section(
        "Walling",
        walling
    )

    engine.add_section(
        "Roof",
        roof
    )

    engine.add_section(
        "Finishes",
        finishes
    )

    engine.add_section(
        "Electrical",
        electrical
    )

    engine.add_section(
        "Plumbing",
        plumbing
    )

    engine.add_section(
        "Doors & Windows",
        doors_windows
    )


    report = engine.summary()


    # ==================================================
    # BOQ
    # ==================================================

    estimate = {}


    for item in report["BOQ"]:

        estimate[item["description"]] = (

            estimate.get(
                item["description"],
                0
            )

            +

            item["amount"]

        )


    # ==================================================
    # MATERIALS
    # ==================================================

    materials = {

        "foundation":
            foundation.get("materials", {}),

        "walling":
            walling.get("materials", {}),

        "roof":
            roof.get("materials", {}),

        "finishes":
            finishes.get("materials", {}),

        "electrical":
            electrical.get("materials", {}),

        "plumbing":
            plumbing.get("materials", {}),

        "doors_windows":
            doors_windows.get("materials", {}),

    }


    # ==================================================
    # LABOUR
    # ==================================================

    labour = {

        "foundation":
            foundation.get("labour", {}),

        "walling":
            walling.get("labour", {}),

        "roof":
            roof.get("labour", {}),

        "finishes":
            finishes.get("labour", {}),

        "electrical":
            electrical.get("labour", {}),

        "plumbing":
            plumbing.get("labour", {}),

        "doors_windows":
            doors_windows.get("labour", {}),

    }


    # ==================================================
    # RETURN COMPLETE ESTIMATE
    # ==================================================

    return {


        "project": {

            "Project Type":
                project_type,

            "House Type":
                house_type,

            "County":
                county,

            "Length":
                length,

            "Width":
                width,

            "Wall Height":
                wall_height,

            "Block Type":
                block_type,

            "Roof Type":
                roof_type,

            "Bedrooms":
                bedrooms,

            "Doors":
                doors,

            "Windows":
                windows,

        },


        "foundation": foundation,

        "walling": walling,

        "roof": roof,

        "finishes": finishes,

        "electrical": electrical,

        "plumbing": plumbing,

        "doors_windows": doors_windows,


        "estimate": estimate,


        "boq":
            report["BOQ"],


        "materials":
            materials,


        "labour":
            labour,


        "subtotal":
            report["Subtotal"],


        "vat":
            report["VAT"],


        "grand_total":
            report["Grand Total"],

    }



# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    from pprint import pprint


    pprint(

        generate_estimate(

            county="Mombasa",

            project_type="Residential",

            house_type="3 Bedroom",

            length=10,

            width=12,

            wall_height=3,

            block_type="Machine Cut Stone",

            roof_type="Mabati",

        )

    )