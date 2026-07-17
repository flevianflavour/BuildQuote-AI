"""
BuildQuote AI

House Service

Provides:
• Doors
• Windows
• House Template Data
"""



from config.house_templates import HOUSE_TEMPLATES





class HouseService:



    def __init__(self, house_type):


        self.house_type = house_type



        # ----------------------------------
        # Handle invalid house type
        # ----------------------------------


        if house_type not in HOUSE_TEMPLATES:


            # Default fallback

            house_type = "3 Bedroom"



        self.house = HOUSE_TEMPLATES[house_type]






    # =====================================
    # OPENINGS
    # =====================================


    def main_doors(self):

        return self.house.get(

            "main_doors",

            1

        )



    def internal_doors(self):

        return self.house.get(

            "internal_doors",

            6

        )



    def bathroom_doors(self):

        return self.house.get(

            "bathroom_doors",

            2

        )



    def windows(self):

        return self.house.get(

            "windows",

            10

        )



    def toilet_windows(self):

        return self.house.get(

            "toilet_windows",

            2

        )






    # =====================================
    # HOUSE DETAILS
    # =====================================


    def bedrooms(self):

        return self.house.get(

            "bedrooms",

            3

        )





    def floors(self):

        return self.house.get(

            "floors",

            1

        )






    # =====================================
    # SUMMARY
    # =====================================


    def summary(self):


        return {


            "house_type":

            self.house_type,



            "details":

            self.house

        }