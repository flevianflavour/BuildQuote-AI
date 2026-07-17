"""
BuildQuote AI

Material Service v3

Controls selected construction materials.

Used by:

Project
   ↓
EstimationEngine
   ↓
MaterialEngine
   ↓
BOQ
"""





class MaterialService:



    MATERIALS = {


        "Machine Cut Stone": {


            "coverage":12.5,


            "mortar_ratio":"1:4",


            "price":85,


            "unit":"Pieces",


            "wastage":0.05


        },



        "Coral Blocks": {


            "coverage":10,


            "mortar_ratio":"1:5",


            "price":65,


            "unit":"Blocks",


            "wastage":0.05


        },



        "Concrete Blocks": {


            "coverage":12.5,


            "mortar_ratio":"1:5",


            "price":80,


            "unit":"Blocks",


            "wastage":0.05


        },



        "Clay Bricks": {


            "coverage":60,


            "mortar_ratio":"1:6",


            "price":25,


            "unit":"Bricks",


            "wastage":0.07


        }

    }





    # =====================================
    # INITIALIZE
    # =====================================


    def __init__(

        self,

        material_name="Machine Cut Stone"

    ):



        if material_name not in self.MATERIALS:


            material_name = "Machine Cut Stone"



        self.material_name = material_name


        self.material = self.MATERIALS[material_name]







    # =====================================
    # ACCESSOR
    # =====================================


    def get(

        self,

        key,

        default=None

    ):


        return self.material.get(

            key,

            default

        )







    # =====================================
    # MODERN API
    # =====================================


    def name(self):

        return self.material_name




    def coverage(self):

        return self.get(

            "coverage"

        )




    def mortar_ratio(self):

        return self.get(

            "mortar_ratio"

        )




    def price(self):

        return self.get(

            "price"

        )




    def unit(self):

        return self.get(

            "unit"

        )




    def wastage(self):

        return self.get(

            "wastage",

            0.05

        )








    # =====================================
    # BACKWARD COMPATIBILITY
    # =====================================


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


def wall_materials(self, wall_area, block_type="Machine Cut Stone"):

    material = self.MATERIALS.get(
        block_type,
        self.MATERIALS["Machine Cut Stone"]
    )

    coverage = material["coverage"]

    wastage = material.get("wastage", 0.05)

    blocks = round((wall_area * coverage) * (1 + wastage))

    cement_bags = round(wall_area * 0.32)

    sand_m3 = round(wall_area * 0.05, 2)

    return {
        "blocks": blocks,
        "cement_bags": cement_bags,
        "sand_m3": sand_m3,
    }




    # =====================================
    # SUMMARY
    # =====================================


    def summary(self):


        return {


            "Material":

            self.name(),



            "Coverage":

            self.coverage(),



            "Mortar Ratio":

            self.mortar_ratio(),



            "Unit Price":

            self.price(),



            "Unit":

            self.unit(),



            "Wastage":

            self.wastage()

        }