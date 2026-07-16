class ConcreteCalculator:

    def __init__(

        self,

        volume,

        mix_ratio="1:2:3"

    ):

        self.volume = volume

        self.mix_ratio = mix_ratio

    # -----------------------------------
    # Cement
    # -----------------------------------

    def cement_bags(self):

        # Kenyan approximation:
        # 1 m³ of 1:2:3 concrete
        # ≈ 8 bags of cement

        return round(self.volume * 8)

    # -----------------------------------
    # Sand
    # -----------------------------------

    def sand_wheelbarrows(self):

        # 2 wheelbarrows per cement bag

        return self.cement_bags() * 2

    # -----------------------------------
    # Ballast
    # -----------------------------------

    def ballast_wheelbarrows(self):

        # 3 wheelbarrows per cement bag

        return self.cement_bags() * 3

    # -----------------------------------
    # Water
    # -----------------------------------

    def water_litres(self):

        # Approximately 30 litres per bag

        return self.cement_bags() * 30

    # -----------------------------------
    # Summary
    # -----------------------------------

    def summary(self):

        return {

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