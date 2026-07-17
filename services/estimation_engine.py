"""
BuildQuote AI

Estimation Engine v4

Controls

- Foundation
- Openings
- Walling
- Mortar
- Concrete

Returns data ready for:

✔ Dashboard
✔ BOQ
✔ PDF
✔ Excel
"""

from estimators.foundation_estimator import estimate_foundation
from estimators.openings import OpeningsEstimator
from estimators.mortar import MortarEstimator
from estimators.concrete import ConcreteCalculator

from services.house_service import HouseService
from services.material_service import MaterialService


class EstimationEngine:

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def __init__(
        self,
        county,
        length,
        width,
        height,
        house_type,
        wall_material,
        bedrooms=3,
    ):

        self.county = county
        self.length = length
        self.width = width
        self.height = height
        self.bedrooms = bedrooms

        self.house = HouseService(house_type)
        self.material = MaterialService(wall_material)

    # ==========================================================
    # FOUNDATION
    # ==========================================================

    def foundation(self):

        return estimate_foundation(
            county=self.county,
            length=self.length,
            width=self.width,
        )

    # ==========================================================
    # OPENINGS
    # ==========================================================

    def openings(self):

        opening = OpeningsEstimator(

            main_doors=self.house.main_doors(),

            internal_doors=self.house.internal_doors(),

            bathroom_doors=self.house.bathroom_doors(),

            windows=self.house.windows(),

            toilet_windows=self.house.toilet_windows()

        )

        return {

            "section": "Openings",

            "summary": opening.summary(),

            "total_opening_area": round(
                opening.total_area(),
                2,
            )

        }

    # ==========================================================
    # WALLING
    # ==========================================================

    def walling(self):

        opening = OpeningsEstimator(

            main_doors=self.house.main_doors(),

            internal_doors=self.house.internal_doors(),

            bathroom_doors=self.house.bathroom_doors(),

            windows=self.house.windows(),

            toilet_windows=self.house.toilet_windows()

        )

        wall_area = (

            2 *

            (self.length + self.width)

            *

            self.height

        )

        opening_area = opening.total_area()

        net_wall_area = max(

            wall_area - opening_area,

            0

        )

        coverage = self.material.coverage()

        blocks = round(

            net_wall_area * coverage

        )

        materials = {

            "Wall Material": self.material.name(),

            "Blocks": blocks,

        }

        labour = {

            "Mason Days": round(

                blocks / 100,

                1

            )

        }

        boq = [

            {

                "description": self.material.name(),

                "quantity": blocks,

                "unit": "Pieces",

                "amount": 0,

            }

        ]

        return {

            "section": "Walling",

            "wall_area": round(wall_area, 2),

            "opening_area": round(opening_area, 2),

            "net_wall_area": round(net_wall_area, 2),

            "required_quantity": blocks,

            "materials": materials,

            "labour": labour,

            "boq": boq,

            "subtotal": 0,

        }    # ==========================================================
    # MORTAR
    # ==========================================================

    def mortar(self):

        walling = self.walling()

        mortar = MortarEstimator(

            walling["required_quantity"],

            self.material.mortar_ratio()

        )

        result = mortar.summary()

        result.setdefault("materials", {})

        result.setdefault("labour", {})

        result.setdefault("boq", [])

        result.setdefault("subtotal", 0)

        return result

    # ==========================================================
    # CONCRETE
    # ==========================================================

    def concrete(self):

        foundation = self.foundation()

        volume = (

            foundation.get(

                "quantities",

                {}

            ).get(

                "concrete",

                0

            )

        )

        calculator = ConcreteCalculator(

            volume

        )

        result = calculator.summary()

        result.setdefault("materials", {})

        result.setdefault("labour", {})

        result.setdefault("boq", [])

        result.setdefault("subtotal", 0)

        return result

    # ==========================================================
    # MASTER BOQ
    # ==========================================================

    def generate_boq(self):

        foundation = self.foundation()

        openings = self.openings()

        walling = self.walling()

        mortar = self.mortar()

        concrete = self.concrete()

        sections = {

            "Foundation": foundation,

            "Openings": openings,

            "Walling": walling,

            "Mortar": mortar,

            "Concrete": concrete,

        }

        boq = []

        materials = {}

        labour = {}

        subtotal = 0

        for section_name, section in sections.items():

            if not isinstance(section, dict):

                continue

            section_boq = section.get("boq", [])

            if isinstance(section_boq, list):

                boq.extend(section_boq)

            materials[section_name] = section.get(

                "materials",

                {}

            )

            labour[section_name] = section.get(

                "labour",

                {}

            )

            if "subtotal" in section:

                subtotal += float(

                    section.get(

                        "subtotal",

                        0

                    )

                )

            elif "total" in section:

                subtotal += float(

                    section.get(

                        "total",

                        0

                    )

                )        # --------------------------------------------------
        # VAT
        # --------------------------------------------------

                vat = round(
            subtotal * 0.16,
            2
        )

        grand_total = round(
            subtotal + vat,
            2
        )

        # ==========================================================
        # BUILDING STATISTICS
        # ==========================================================

        floor_area = round(
            self.length * self.width,
            2
        )

        perimeter = round(
            2 * (self.length + self.width),
            2
        )

        wall_area = round(
            perimeter * self.height,
            2
        )

        foundation = self.foundation()

        foundation_area = round(
            self.length * self.width,
            2
        )

        excavation_volume = foundation.get(
            "quantities",
            {}
        ).get(
            "excavation",
            0
        )

        concrete_volume = foundation.get(
            "quantities",
            {}
        ).get(
            "concrete",
            0
        )

        # ==========================================================
        # RETURN
        # ==========================================================

        return {

            "project": {

                "County": self.county,

                "Length": self.length,

                "Width": self.width,

                "Wall Height": self.height,

                "Perimeter": perimeter,

                "Floor Area": floor_area,

                "Wall Area": wall_area,

                "Foundation Area": foundation_area,

                "Excavation Volume": excavation_volume,

                "Concrete Volume": concrete_volume,

                "House Type": self.house.house_type,

                "Wall Material": self.material.name(),

                "Bedrooms": self.bedrooms,

            },

            "sections": sections,

            "boq": boq,

            "materials": materials,

            "labour": labour,

            "subtotal": round(subtotal, 2),

            "vat": vat,

            "grand_total": grand_total,

        }