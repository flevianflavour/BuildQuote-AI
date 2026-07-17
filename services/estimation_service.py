"""
BuildQuote AI

Main Estimation Service
"""

from services.estimation_engine import EstimationEngine
from estimators.doors_windows import estimate_doors_windows


class EstimationService:

    def estimate(self, project):

        # ==================================================
        # BEDROOMS
        # ==================================================

        bedrooms = {

            "Bedsitter": 1,

            "1 Bedroom": 1,

            "2 Bedroom": 2,

            "3 Bedroom": 3,

            "4 Bedroom": 4,

            "Maisonette": 4,

            "Villa": 5

        }.get(project.house_type, 3)

        # ==================================================
        # ESTIMATION ENGINE
        # ==================================================

        engine = EstimationEngine(

            county=project.county,

            length=project.length,

            width=project.width,

            height=project.height,

            house_type=project.house_type,

            wall_material=project.wall_material,

            bedrooms=bedrooms

        )

        estimate = engine.generate_boq()

        # ==================================================
        # SECTIONS
        # ==================================================

        sections = estimate["sections"]

        # ==================================================
        # DOORS & WINDOWS
        # ==================================================

        doors_windows = estimate_doors_windows(

            county=project.county,

            bedrooms=bedrooms

        )

        sections["Doors & Windows"] = doors_windows

        # ==================================================
        # UPDATE MATERIALS
        # ==================================================

        materials = estimate["materials"]

        materials["Doors & Windows"] = doors_windows.get(

            "materials",

            {}

        )

        # ==================================================
        # UPDATE LABOUR
        # ==================================================

        labour = estimate["labour"]

        labour["Doors & Windows"] = doors_windows.get(

            "labour",

            {}

        )

        # ==================================================
        # UPDATE BOQ
        # ==================================================

        boq = estimate["boq"]

        if "boq" in doors_windows:

            boq.extend(

                doors_windows["boq"]

            )

        # ==================================================
        # RECALCULATE TOTALS
        # ==================================================

        subtotal = estimate["subtotal"]

        subtotal += doors_windows.get(

            "subtotal",

            doors_windows.get(

                "total",

                0

            )

        )

        vat = round(

            subtotal * 0.16,

            2

        )

        grand_total = round(

            subtotal + vat,

            2

        )

        # ==================================================
        # PROJECT INFORMATION
        # ==================================================

        project_info = {

            "County": project.county,

            "Project Type": project.project_type,

            "House Type": project.house_type,

            "Length": project.length,

            "Width": project.width,

            "Wall Height": project.height,

            "Block Type": project.wall_material,

            "Roof Type": project.roof_type,

            "Bedrooms": bedrooms

        }

        # ==================================================
        # RETURN
        # ==================================================

        return {

            "project": project_info,

            "sections": sections,

            "boq": boq,

            "materials": materials,

            "labour": labour,

            "subtotal": round(subtotal, 2),

            "vat": vat,

            "grand_total": round(grand_total, 2)

        }