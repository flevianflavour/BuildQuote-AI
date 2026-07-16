class MaterialService:

    MATERIALS = {

        "Machine Cut Stone": {
            "coverage": 12.5,
            "mortar_ratio": "1:4",
            "price": 85,
            "unit": "Pieces"
        },

        "Coral Blocks": {
            "coverage": 10,
            "mortar_ratio": "1:5",
            "price": 65,
            "unit": "Blocks"
        },

        "Concrete Blocks": {
            "coverage": 12.5,
            "mortar_ratio": "1:5",
            "price": 80,
            "unit": "Blocks"
        },

        "Clay Bricks": {
            "coverage": 60,
            "mortar_ratio": "1:6",
            "price": 25,
            "unit": "Bricks"
        }

    }

    def __init__(self, material_name):

        if material_name not in self.MATERIALS:
            raise ValueError(
                f"Material '{material_name}' not found."
            )

        self.material_name = material_name
        self.material = self.MATERIALS[material_name]

    # -----------------------------
    # Generic accessor
    # -----------------------------

    def get(self, key):
        return self.material[key]

    # -----------------------------
    # Modern API
    # -----------------------------

    def name(self):
        return self.material_name

    def coverage(self):
        return self.get("coverage")

    def mortar_ratio(self):
        return self.get("mortar_ratio")

    def price(self):
        return self.get("price")

    def unit(self):
        return self.get("unit")

    # -----------------------------
    # Backward compatibility
    # -----------------------------

    def get_name(self):
        return self.name()

    def get_coverage(self):
        return self.coverage()

    def get_mortar_ratio(self):
        return self.mortar_ratio()

    def get_price(self):
        return self.price()

    def get_unit(self):
        return self.unit()

    # -----------------------------
    # Summary
    # -----------------------------

    def summary(self):

        return {
            "Material": self.name(),
            "Coverage": self.coverage(),
            "Mortar Ratio": self.mortar_ratio(),
            "Unit Price": self.price(),
            "Unit": self.unit()
        }