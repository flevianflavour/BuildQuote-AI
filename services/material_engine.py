"""
BuildQuote AI

Material Calculation Engine v3

Calculates:

• Concrete Materials
• Mortar Materials
• Plaster Materials
• Screed Materials
• Wall Materials

No pricing included.

Prices are handled by:
costing.county_prices
"""



import math





class MaterialEngine:




    # =====================================
    # MATERIAL COVERAGE
    # =====================================


    BLOCK_COVERAGE = {


        "Machine Cut Stone":12.5,


        "Quarry Stone":10,


        "Concrete Block":12,


        "Clay Brick":60

    }





    # =====================================
    # CONCRETE MIX
    # =====================================


    def concrete_mix(

        self,

        volume,

        mix="1:2:4"

    ):



        mixes = {


            "1:2:4":{


                "cement":7.3,

                "sand":0.44,

                "ballast":0.88,

                "water":210

            },


            "1:3:6":{


                "cement":5.2,

                "sand":0.55,

                "ballast":1.10,

                "water":180

            }


        }




        if mix not in mixes:


            raise ValueError(

                f"Unsupported concrete mix {mix}"

            )



        data = mixes[mix]



        return {


            "cement_bags":math.ceil(

                volume *

                data["cement"]

            ),



            "sand_m3":round(

                volume *

                data["sand"],

                2

            ),



            "ballast_m3":round(

                volume *

                data["ballast"],

                2

            ),



            "water_litres":round(

                volume *

                data["water"]

            )

        }







    # =====================================
    # MORTAR
    # =====================================


    def mortar_mix(

        self,

        volume

    ):


        return {


            "cement_bags":math.ceil(

                volume *

                6.5

            ),



            "sand_m3":round(

                volume *

                1.10,

                2

            )

        }







    # =====================================
    # PLASTER
    # =====================================


    def plaster_mix(

        self,

        area

    ):



        return {


            "cement_bags":math.ceil(

                area *

                0.18

            ),



            "sand_m3":round(

                area *

                0.018,

                2

            )

        }







    # =====================================
    # FLOOR SCREED
    # =====================================


    def screed_mix(

        self,

        area

    ):



        return {


            "cement_bags":math.ceil(

                area *

                0.22

            ),



            "sand_m3":round(

                area *

                0.025,

                2

            )

        }







    # =====================================
    # WALL MATERIALS
    # =====================================


    def wall_materials(


        self,


        wall_area,


        block_type="Machine Cut Stone",


        wastage=0.05


    ):



        coverage = self.BLOCK_COVERAGE.get(

            block_type,

            self.BLOCK_COVERAGE["Machine Cut Stone"]

        )



        blocks = math.ceil(

            wall_area *

            coverage

        )



        # Add 5% wastage


        blocks = math.ceil(

            blocks *

            (1 + wastage)

        )





        mortar_volume = (

            wall_area *

            0.03

        )



        mortar = self.mortar_mix(

            mortar_volume

        )



        return {


            "material":

            block_type,



            "wall_area":

            round(

                wall_area,

                2

            ),



            "blocks":

            blocks,



            "cement_bags":

            mortar["cement_bags"],



            "sand_m3":

            mortar["sand_m3"],



            "coverage":

            coverage

        }







    # =====================================
    # SUMMARY
    # =====================================


    def summary(self):


        return {


            "supported_materials":

            list(

                self.BLOCK_COVERAGE.keys()

            )

        }





# =====================================
# GLOBAL INSTANCE
# =====================================


material_engine = MaterialEngine()