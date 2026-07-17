"""
BuildQuote AI

Cost Engine

Combines estimator outputs into one BOQ,
materials, labour and cost summary.
"""


class CostEngine:

    def __init__(self):
        self.sections = []

    # ===================================================
    # ADD SECTION
    # ===================================================

    def add_section(self, name, estimate):

        if not estimate:
            return

        self.sections.append({
            "name": name,
            "estimate": estimate
        })

    # ===================================================
    # BOQ
    # ===================================================

    def boq(self):

        boq = []

        for section in self.sections:

            estimate = section["estimate"]

            items = estimate.get("boq", [])

            if isinstance(items, list):
                boq.extend(items)

        return boq

    # ===================================================
    # MATERIAL SUMMARY
    # ===================================================

    def materials(self):

        results = {}

        for section in self.sections:

            results[section["name"]] = section["estimate"].get(
                "materials",
                {}
            )

        return results

    # ===================================================
    # LABOUR SUMMARY
    # ===================================================

    def labour(self):

        results = {}

        for section in self.sections:

            results[section["name"]] = section["estimate"].get(
                "labour",
                {}
            )

        return results

    # ===================================================
    # MATERIAL COST
    # ===================================================

    def material_cost(self):

        total = 0

        for section in self.sections:

            estimate = section["estimate"]

            if "subtotal" in estimate:
                total += float(estimate["subtotal"])

            elif "total" in estimate:
                total += float(estimate["total"])

        return round(total, 2)

    # ===================================================
    # LABOUR COST
    # ===================================================

    def labour_cost(self):

        total = 0

        for section in self.sections:

            labour = section["estimate"].get(
                "labour",
                {}
            )

            if isinstance(labour, dict):

                for value in labour.values():

                    if isinstance(value, (int, float)):
                        total += value

        return round(total, 2)

    # ===================================================
    # EQUIPMENT COST
    # ===================================================

    def equipment_cost(self):

        total = 0

        for section in self.sections:

            estimate = section["estimate"]

            equipment = estimate.get(
                "equipment_cost",
                0
            )

            if isinstance(equipment, (int, float)):
                total += equipment

        return round(total, 2)

    # ===================================================
    # SUBTOTAL
    # ===================================================

    def subtotal(self):

        return round(

            self.material_cost()

            +

            self.labour_cost()

            +

            self.equipment_cost(),

            2

        )

    # ===================================================
    # VAT
    # ===================================================

    def vat(self):

        return round(
            self.subtotal() * 0.16,
            2
        )

    # ===================================================
    # GRAND TOTAL
    # ===================================================

    def grand_total(self):

        return round(
            self.subtotal() + self.vat(),
            2
        )

        # ===================================================
    # SUMMARY
    # ===================================================

    def summary(self):

        material_cost = 0
        labour_cost = 0
        equipment_cost = 0

        for section in self.sections:

            estimate = section["estimate"]

            if not isinstance(estimate, dict):
                continue

            if "subtotal" in estimate:
                material_cost += float(estimate.get("subtotal", 0))
            elif "total" in estimate:
                material_cost += float(estimate.get("total", 0))

            labour = estimate.get("labour", {})

            if isinstance(labour, dict):
                for value in labour.values():
                    if isinstance(value, (int, float)):
                        labour_cost += value

        return {

            "Sections": self.sections,

            "BOQ": self.boq(),

            "Materials": self.materials(),

            "Labour": self.labour(),

            "Subtotal": self.subtotal(),

            "VAT": self.vat(),

            "Grand Total": self.grand_total(),

            "material_cost": round(material_cost, 2),

            "labour_cost": round(labour_cost, 2),

            "equipment_cost": round(equipment_cost, 2),

        }