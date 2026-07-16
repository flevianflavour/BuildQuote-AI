class MortarEstimator:

    CEMENT_BAG_VOLUME = 0.035  # m³ per 50kg bag

    def __init__(
        self,
        wall_material_quantity,
        mortar_ratio
    ):

        self.wall_material_quantity = wall_material_quantity
        self.mortar_ratio = mortar_ratio

    # --------------------------------
    # Total mortar volume
    # --------------------------------

    def mortar_volume(self):

        return round(
            self.wall_material_quantity * 0.002,
            3
        )

    # --------------------------------
    # Cement and sand volumes
    # --------------------------------

    def cement_sand(self):

        volume = self.mortar_volume()

        ratios = {
            "1:4": (1, 4),
            "1:5": (1, 5),
            "1:6": (1, 6)
        }

        if self.mortar_ratio not in ratios:
            raise ValueError(
                f"Unsupported mortar ratio: {self.mortar_ratio}"
            )

        cement_parts, sand_parts = ratios[self.mortar_ratio]
        total_parts = cement_parts + sand_parts

        cement_volume = volume * cement_parts / total_parts
        sand_volume = volume * sand_parts / total_parts

        cement_bags = round(
            cement_volume / self.CEMENT_BAG_VOLUME
        )

        return {
            "cement_volume": round(cement_volume, 3),
            "sand_volume": round(sand_volume, 3),
            "cement_bags": cement_bags
        }

    # --------------------------------
    # BOQ Output
    # --------------------------------

    def summary(self):

        materials = self.cement_sand()

        return {

            "Mortar Volume": {
                "unit": "m³",
                "quantity": self.mortar_volume()
            },

            "Cement": {
                "unit": "Bags",
                "quantity": materials["cement_bags"]
            },

            "Sand": {
                "unit": "m³",
                "quantity": materials["sand_volume"]
            },

            "Ratio": self.mortar_ratio

        }