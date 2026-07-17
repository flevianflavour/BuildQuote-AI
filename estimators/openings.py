"""
BuildQuote AI

Openings Estimator

Calculates:

• Doors
• Windows
• Opening Area
• BOQ
"""

# ==================================================
# DEFAULT RATES (KENYA)
# ==================================================

DEFAULT_RATES = {


    "Main_Door": 35000,

    "Internal_Door": 12000,

    "Bathroom_Door": 9000,

    "Window": 15000,

    "Toilet_Window": 6000

}




# ==================================================
# OPENINGS ESTIMATOR
# ==================================================

class OpeningsEstimator:


    # Standard Kenyan Sizes (metres)


    MAIN_DOOR = 1.2 * 2.1


    INTERNAL_DOOR = 0.9 * 2.1


    BATHROOM_DOOR = 0.75 * 2.1


    WINDOW = 1.2 * 1.2


    TOILET_WINDOW = 0.6 * 0.6




    def __init__(

        self,

        main_doors=1,

        internal_doors=5,

        bathroom_doors=2,

        windows=8,

        toilet_windows=2

    ):


        self.main_doors = main_doors


        self.internal_doors = internal_doors


        self.bathroom_doors = bathroom_doors


        self.windows = windows


        self.toilet_windows = toilet_windows





    # ==================================================
    # AREA CALCULATION
    # ==================================================

    def total_area(self):


        return round(


            (

                self.main_doors * self.MAIN_DOOR

                +

                self.internal_doors * self.INTERNAL_DOOR

                +

                self.bathroom_doors * self.BATHROOM_DOOR

                +

                self.windows * self.WINDOW

                +

                self.toilet_windows * self.TOILET_WINDOW

            ),

            2

        )





    # ==================================================
    # COST ESTIMATION
    # ==================================================

    def calculate_cost(self,rates=None):


        if rates is None:

            rates = DEFAULT_RATES



        main_cost = (

            self.main_doors

            *

            rates["Main_Door"]

        )



        internal_cost = (

            self.internal_doors

            *

            rates["Internal_Door"]

        )



        bathroom_cost = (

            self.bathroom_doors

            *

            rates["Bathroom_Door"]

        )



        window_cost = (

            self.windows

            *

            rates["Window"]

        )



        toilet_window_cost = (

            self.toilet_windows

            *

            rates["Toilet_Window"]

        )



        return {


            "material_total": round(

                main_cost

                +

                internal_cost

                +

                bathroom_cost

                +

                window_cost

                +

                toilet_window_cost,

                2

            ),



            "main_doors_cost": main_cost,


            "internal_doors_cost": internal_cost,


            "bathroom_doors_cost": bathroom_cost,


            "windows_cost": window_cost,


            "toilet_windows_cost": toilet_window_cost

        }





    # ==================================================
    # BOQ
    # ==================================================

    def boq(self,rates=None):


        if rates is None:

            rates = DEFAULT_RATES



        return [


            {

                "description":"Main Door",

                "quantity":self.main_doors,

                "unit":"Pieces",

                "rate":rates["Main_Door"],

                "amount":

                    self.main_doors *

                    rates["Main_Door"]

            },



            {

                "description":"Internal Doors",

                "quantity":self.internal_doors,

                "unit":"Pieces",

                "rate":rates["Internal_Door"],

                "amount":

                    self.internal_doors *

                    rates["Internal_Door"]

            },



            {

                "description":"Bathroom Doors",

                "quantity":self.bathroom_doors,

                "unit":"Pieces",

                "rate":rates["Bathroom_Door"],

                "amount":

                    self.bathroom_doors *

                    rates["Bathroom_Door"]

            },



            {

                "description":"Windows",

                "quantity":self.windows,

                "unit":"Pieces",

                "rate":rates["Window"],

                "amount":

                    self.windows *

                    rates["Window"]

            },



            {

                "description":"Toilet Windows",

                "quantity":self.toilet_windows,

                "unit":"Pieces",

                "rate":rates["Toilet_Window"],

                "amount":

                    self.toilet_windows *

                    rates["Toilet_Window"]

            }


        ]





    # ==================================================
    # SUMMARY FOR ENGINE
    # ==================================================

    def summary(self):


        boq = self.boq()


        subtotal = sum(

            item["amount"]

            for item in boq

        )


        vat = subtotal * 0.16


        total = subtotal + vat



        return {


            "section":"Openings",



            "opening_area":{


                "unit":"m²",

                "quantity":self.total_area()

            },



            "materials":{


                "main_doors":self.main_doors,


                "internal_doors":self.internal_doors,


                "bathroom_doors":self.bathroom_doors,


                "windows":self.windows,


                "toilet_windows":self.toilet_windows


            },



            "boq":boq,



            "material_total":round(subtotal,2),



            "labour_total":0,



            "subtotal":round(subtotal,2),



            "vat":round(vat,2),



            "total":round(total,2),



            "grand_total":round(total,2)

        }





    # ==================================================
    # ENGINE COMPATIBILITY
    # ==================================================

    def estimate(self):


        return self.summary()





# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":


    from pprint import pprint



    openings = OpeningsEstimator(


        main_doors=1,


        internal_doors=6,


        bathroom_doors=2,


        windows=8,


        toilet_windows=2


    )


    pprint(

        openings.summary()

    )