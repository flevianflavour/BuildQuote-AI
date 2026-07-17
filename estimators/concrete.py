class ConcreteCalculator:

    def __init__(
        self,
        volume,
        mix_ratio="1:2:3"
    ):

        self.volume = volume
        self.mix_ratio = mix_ratio

    # ==================================================
    # MATERIAL CALCULATIONS
    # ==================================================

    def cement_bags(self):

        return round(self.volume * 8)

    def sand_wheelbarrows(self):

        return round(self.cement_bags() * 2)

    def ballast_wheelbarrows(self):

        return round(self.cement_bags() * 3)

    def water_litres(self):

        return round(self.cement_bags() * 30)

    # ==================================================
    # MATERIALS
    # ==================================================

    def materials(self):

        return {

            "Concrete Volume (m³)": round(self.volume, 2),

            "Cement Bags": self.cement_bags(),

            "Sand Wheelbarrows": self.sand_wheelbarrows(),

            "Ballast Wheelbarrows": self.ballast_wheelbarrows(),

            "Water (Litres)": self.water_litres(),

        }

    # ==================================================
    # SUMMARY
    # ==================================================

    def summary(self):

        return {

            "materials": self.materials(),

            "mix_ratio": self.mix_ratio,

            "Concrete Volume": {

                "quantity": round(self.volume, 2),

                "unit": "m³"

            },

            "Cement": {

                "quantity": self.cement_bags(),

                "unit": "Bags"

            },

            "Sand": {

                "quantity": self.sand_wheelbarrows(),

                "unit": "Wheelbarrows"

            },

            "Ballast": {

                "quantity": self.ballast_wheelbarrows(),

                "unit": "Wheelbarrows"

            },

            "Water": {

                "quantity": self.water_litres(),

                "unit": "Litres"

            },

            "Mix Ratio": {

                "quantity": self.mix_ratio,

                "unit": ""

            }

        }