"""
BuildQuote AI

Roof Service

Handles roofing standards and specifications.
"""

from config.kenya_standards import ROOFING



class RoofService:



    def __init__(self, roof):

        if roof not in ROOFING:

            raise ValueError(
                f"Roof type '{roof}' not found in Kenya standards."
            )


        self.roof = roof

        self.data = ROOFING[roof]



    # ------------------------------------
    # Timber Requirement
    # ------------------------------------

    def timber(self):

        return self.data.get(

            "timber_per_m2",

            0

        )



    # ------------------------------------
    # Ridge Cap Price
    # ------------------------------------

    def ridge_price(self):

        return self.data.get(

            "ridge_price",

            0

        )



    # ------------------------------------
    # Roofing Coverage
    # ------------------------------------

    def coverage(self):

        return self.data.get(

            "coverage",

            0

        )



    # ------------------------------------
    # Roof Material Price
    # ------------------------------------

    def material_price(self):

        return self.data.get(

            "price",

            0

        )



    # ------------------------------------
    # Roof Unit
    # ------------------------------------

    def unit(self):

        return self.data.get(

            "unit",

            "m²"

        )



    # ------------------------------------
    # Roof Summary
    # ------------------------------------

    def summary(self):

        return {

            "Roof Type":
                self.roof,


            "Coverage":
                self.coverage(),


            "Timber Requirement":
                self.timber(),


            "Material Price":
                self.material_price(),


            "Ridge Price":
                self.ridge_price(),


            "Unit":
                self.unit()

        }