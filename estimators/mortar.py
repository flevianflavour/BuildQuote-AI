"""
BuildQuote AI

Mortar Estimator

Calculates:

• Mortar Volume
• Cement
• Sand
• Material Cost
• BOQ
"""



# ==================================================
# DEFAULT RATES
# ==================================================

DEFAULT_RATES = {


    "Cement": 850,

    "Sand": 2500

}





# ==================================================
# MORTAR ESTIMATOR
# ==================================================

class MortarEstimator:



    CEMENT_BAG_VOLUME = 0.035



    def __init__(

        self,

        wall_material_quantity,

        mortar_ratio="1:5"

    ):


        self.wall_material_quantity = wall_material_quantity


        self.mortar_ratio = mortar_ratio





    # ==================================================
    # MORTAR VOLUME
    # ==================================================

    def mortar_volume(self):


        return round(

            self.wall_material_quantity * 0.002,

            3

        )





    # ==================================================
    # CEMENT AND SAND
    # ==================================================

    def cement_sand(self):


        volume = self.mortar_volume()



        ratios = {


            "1:4":(1,4),


            "1:5":(1,5),


            "1:6":(1,6)

        }




        if self.mortar_ratio not in ratios:


            raise ValueError(

                f"Unsupported mortar ratio: {self.mortar_ratio}"

            )




        cement_parts, sand_parts = ratios[

            self.mortar_ratio

        ]



        total_parts = (

            cement_parts

            +

            sand_parts

        )




        cement_volume = (

            volume

            *

            cement_parts

            /

            total_parts

        )



        sand_volume = (

            volume

            *

            sand_parts

            /

            total_parts

        )



        cement_bags = round(

            cement_volume

            /

            self.CEMENT_BAG_VOLUME

        )




        return {


            "cement_volume":round(

                cement_volume,

                3

            ),


            "sand_volume":round(

                sand_volume,

                3

            ),


            "cement_bags":cement_bags

        }





    # ==================================================
    # BOQ
    # ==================================================

    def boq(self,rates=None):


        if rates is None:


            rates = DEFAULT_RATES




        materials = self.cement_sand()




        cement_cost = (

            materials["cement_bags"]

            *

            rates["Cement"]

        )



        sand_cost = (

            materials["sand_volume"]

            *

            rates["Sand"]

        )




        return [



            {


                "description":"Cement for Mortar",


                "quantity":materials["cement_bags"],


                "unit":"Bags",


                "rate":rates["Cement"],


                "amount":round(

                    cement_cost,

                    2

                )

            },



            {


                "description":"Mortar Sand",


                "quantity":materials["sand_volume"],


                "unit":"m³",


                "rate":rates["Sand"],


                "amount":round(

                    sand_cost,

                    2

                )

            }


        ]





    # ==================================================
    # SUMMARY
    # ==================================================

    def summary(self,rates=None):


        materials = self.cement_sand()



        boq = self.boq(rates)



        subtotal = sum(

            item["amount"]

            for item in boq

        )



        vat = subtotal * 0.16



        total = subtotal + vat





        return {


            "section":"Mortar",



            "mortar_volume":{


                "unit":"m³",


                "quantity":self.mortar_volume()

            },



            "materials":{


                "cement_bags":

                    materials["cement_bags"],



                "cement_volume":

                    materials["cement_volume"],



                "sand_volume":

                    materials["sand_volume"],



                "ratio":

                    self.mortar_ratio

            },



            "boq":boq,



            "material_total":round(

                subtotal,

                2

            ),



            "labour_total":0,



            "subtotal":round(

                subtotal,

                2

            ),



            "vat":round(

                vat,

                2

            ),



            "total":round(

                total,

                2

            ),



            "grand_total":round(

                total,

                2

            )

        }





    # ==================================================
    # ENGINE COMPATIBILITY
    # ==================================================

    def estimate(self,rates=None):


        return self.summary(rates)





# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":


    from pprint import pprint



    mortar = MortarEstimator(


        wall_material_quantity=1500,


        mortar_ratio="1:5"


    )



    pprint(

        mortar.summary()

    )