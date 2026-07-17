"""
BuildQuote AI

Main Calculation Engine

Connects:
Project
    │
Estimators
    │
Cost Engine
    │
BOQ + Dashboard + PDF
"""

from estimators.foundation_estimator import estimate_foundation
from estimators.walling_estimator import estimate_walling
from estimators.roof_estimator import estimate_roof
from estimators.finishes_estimator import estimate_finishes
from estimators.electrical_estimator import estimate_electrical
from estimators.plumbing_estimator import estimate_plumbing
from estimators.doors_windows import estimate_doors_windows

from costing.cost_engine import CostEngine


# ==================================================
# HOUSE TYPE MAPPING
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


# ==================================================
# MAIN ESTIMATION FUNCTION
# ==================================================

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

    if bedrooms is None:
        bedrooms = HOUSE_BEDROOM_MAP.get(
            house_type,
            3
        )

    # ------------------------------------------
    # ESTIMATORS
    # ------------------------------------------

    foundation = estimate_foundation(
        county=county,
        length=length,
        width=width
    )

    walling = estimate_walling(
        county=county,
        length=length,
        width=width,
        wall_height=wall_height,
        doors=doors,
        windows=windows,
        block_type=block_type
    )

    roof = estimate_roof(
        county=county,
        length=length,
        width=width,
        roof_type=roof_type
    )

    finishes = estimate_finishes(
        county=county,
        length=length,
        width=width,
        wall_height=wall_height
    )

    electrical = estimate_electrical(
        county=county,
        bedrooms=bedrooms
    )

    plumbing = estimate_plumbing(
        county=county,
        bedrooms=bedrooms
    )

    doors_windows = estimate_doors_windows(
        county=county,
        bedrooms=bedrooms
    )

    # ------------------------------------------
    # COST ENGINE
    # ------------------------------------------

    engine = CostEngine()

    engine.add_section("Foundation", foundation)
    engine.add_section("Walling", walling)
    engine.add_section("Roof", roof)
    engine.add_section("Finishes", finishes)
    engine.add_section("Electrical", electrical)
    engine.add_section("Plumbing", plumbing)
    engine.add_section("Doors & Windows", doors_windows)

    report = engine.summary()   # ==================================================
    # PROJECT DETAILS
    # ==================================================

    project = {

        "County": county,

        "Project Type": project_type,

        "House Type": house_type,

        "Length": length,

        "Width": width,

        "Wall Height": wall_height,

        "Block Type": block_type,

        "Roof Type": roof_type,

        "Bedrooms": bedrooms,

        "Doors": doors,

        "Windows": windows

    }


    # ==================================================
    # BOQ COST SUMMARY
    # ==================================================

    cost_summary = {}

    for item in report.get("BOQ", []):

        description = item.get(
            "description",
            "Item"
        )

        amount = float(
            item.get(
                "amount",
                0
            )
        )

        cost_summary[description] = (
            cost_summary.get(description, 0)
            + amount
        )


    # ==================================================
    # MATERIAL SUMMARY
    # ==================================================

    materials = report.get(
        "Materials",
        {}
    )


    # ==================================================
    # LABOUR SUMMARY
    # ==================================================

    labour = report.get(
        "Labour",
        {}
    )


    # ==================================================
    # SECTION TOTALS
    # ==================================================

    section_totals = {}

    for section in report.get("Sections", []):

        name = section.get(
            "name",
            "Unknown"
        )

        estimate = section.get(
            "estimate",
            {}
        )

        if not isinstance(
            estimate,
            dict
        ):
            continue

        section_totals[name] = estimate.get(
            "total",
            estimate.get(
                "subtotal",
                0
            )
        )


       # ==================================================
    # COST BREAKDOWN
    # ==================================================

    subtotal = report.get(
        "Subtotal",
        0
    )

    vat = report.get(
        "VAT",
        0
    )

    grand_total = report.get(
        "Grand Total",
        subtotal + vat
    )

    # ------------------------------------------
    # Material / Labour / Equipment Costs
    # ------------------------------------------

    material_cost = 0
    labour_cost = 0
    equipment_cost = 0

    for section in report.get("Sections", []):

        estimate = section.get("estimate", {})

        if not isinstance(estimate, dict):
            continue

        material_cost += float(
            estimate.get(
                "material_total",
                estimate.get("subtotal", 0)
            )
        )

        labour_cost += float(
            estimate.get(
                "labour_total",
                0
            )
        )

        equipment_cost += float(
            estimate.get(
                "equipment_total",
                0
            )
        )

    # ==================================================
    # FINAL RETURN
    # ==================================================

    return {

        # ------------------------------------------
        # PROJECT
        # ------------------------------------------

        "project": project,

        # ------------------------------------------
        # INDIVIDUAL ESTIMATORS
        # ------------------------------------------

        "foundation": foundation,

        "walling": walling,

        "roof": roof,

        "finishes": finishes,

        "electrical": electrical,

        "plumbing": plumbing,

        "doors_windows": doors_windows,

        # ------------------------------------------
        # BOQ
        # ------------------------------------------

        "boq": report.get(
            "BOQ",
            []
        ),

        # ------------------------------------------
        # COST SUMMARY
        # ------------------------------------------

        "estimate": cost_summary,

        "section_totals": section_totals,

        # ------------------------------------------
        # MATERIALS & LABOUR
        # ------------------------------------------

        "materials": materials,

        "labour": labour,

        # ------------------------------------------
        # REPORT COSTS
        # ------------------------------------------

        "material_cost": round(material_cost, 2),

        "labour_cost": round(labour_cost, 2),

        "equipment_cost": round(equipment_cost, 2),

        "subtotal": round(subtotal, 2),

        "vat": round(vat, 2),

        "grand_total": round(grand_total, 2),

    }