"""
BuildQuote AI

Cost Engine

Handles:
- BOQ aggregation
- Materials summary
- Labour summary
- VAT
- Total project cost
"""


class CostEngine:


    def __init__(self):

        self.sections = []



    # ==========================================
    # ADD ESTIMATION SECTION
    # ==========================================

    def add_section(self, name, estimate):

        self.sections.append({

            "name": name,

            "estimate": estimate

        })



    # ==========================================
    # BILL OF QUANTITIES
    # ==========================================

    def boq(self):

        boq = []


        for section in self.sections:


            boq.extend(

                section["estimate"].get(

                    "boq",

                    []

                )

            )


        return boq



    # ==========================================
    # SUBTOTAL
    # ==========================================

    def subtotal(self):

        total = 0


        for section in self.sections:


            total += section["estimate"].get(

                "subtotal",

                0

            )


        return round(total, 2)



    # ==========================================
    # VAT
    # ==========================================

    def vat(self):

        return round(

            self.subtotal() * 0.16,

            2

        )



    # ==========================================
    # GRAND TOTAL
    # ==========================================

    def grand_total(self):

        return round(

            self.subtotal()

            +

            self.vat(),

            2

        )



    # ==========================================
    # COMPLETE SUMMARY
    # ==========================================

    def summary(self):


        materials = {}

        labour = {}



        for section in self.sections:


            estimate = section["estimate"]


            section_name = section["name"]



            # -------------------------------
            # MATERIALS BY SECTION
            # -------------------------------

            if "materials" in estimate:


                materials[section_name] = (

                    estimate["materials"]

                )



            # -------------------------------
            # LABOUR BY SECTION
            # -------------------------------

            if "labour" in estimate:


                labour[section_name] = (

                    estimate["labour"]

                )



        return {


            "Sections":

                self.sections,



            "BOQ":

                self.boq(),



            "Materials":

                materials,



            "Labour":

                labour,



            "Subtotal":

                self.subtotal(),



            "VAT":

                self.vat(),



            "Grand Total":

                self.grand_total()

        }