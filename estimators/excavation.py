"""
BuildQuote AI

Excavation Estimator

Calculates:

• Trench Length
• Excavation Volume
• Labour
• BOQ
"""


# ==================================================
# IMPORTS
# ==================================================

try:

    from costing.county_prices import pricing

except ImportError:

    pricing = None




# ==================================================
# DEFAULT RATES
# ==================================================

DEFAULT_RATES = {


    "Excavation_m3": 600,

    "Excavation_Labour_Day": 1500

}




# ==================================================
# EXCAVATION ESTIMATOR
# ==================================================

class ExcavationEstimator:



    def __init__(

        self,

        length,

        width

    ):


        self.length = length

        self.width = width



        # Kenyan standard foundation trench

        self.foundation_width = 0.60

        self.foundation_depth = 1.20





    # ==================================================
    # GEOMETRY
    # ==================================================

    def perimeter(self):


        return 2 * (

            self.length

            +

            self.width

        )





    def trench_length(self):


        return self.perimeter()





    def trench_volume(self):


        return (

            self.trench_length()

            *

            self.foundation_width

            *

            self.foundation_depth

        )





    # ==================================================
    # RATES
    # ==================================================

    def get_rates(self, county=None):


        if pricing and county:


            return pricing.get_rates(county)



        return {}





    def get_rate(

        self,

        rates,

        key,

        default

    ):


        value = rates.get(key)



        if value is None:


            return default



        try:

            return float(value)


        except:


            return default





    # ==================================================
    # BOQ
    # ==================================================

    def boq(self, county=None):


        rates = self.get_rates(county)



        excavation_rate = self.get_rate(

            rates,

            "Excavation_m3",

            DEFAULT_RATES["Excavation_m3"]

        )



        labour_rate = self.get_rate(

            rates,

            "Excavation_Labour_Day",

            DEFAULT_RATES["Excavation_Labour_Day"]

        )



        volume = self.trench_volume()



        excavation_cost = (

            volume

            *

            excavation_rate

        )



        labour_days = round(

            volume / 5,

            1

        )



        labour_cost = (

            labour_days

            *

            labour_rate

        )




        return [



            {


                "description":"Foundation Excavation",


                "quantity":round(volume,2),


                "unit":"m³",


                "rate":excavation_rate,


                "amount":round(

                    excavation_cost,

                    2

                )

            },



            {


                "description":"Excavation Labour",


                "quantity":labour_days,


                "unit":"Days",


                "rate":labour_rate,


                "amount":round(

                    labour_cost,

                    2

                )

            }


        ]






    # ==================================================
    # SUMMARY
    # ==================================================

    def summary(self, county=None):


        boq = self.boq(county)



        subtotal = sum(

            item["amount"]

            for item in boq

        )



        vat = subtotal * 0.16



        total = subtotal + vat




        volume = self.trench_volume()




        return {


            "section":"Excavation",



            "dimensions":{


                "length":self.length,


                "width":self.width,


                "foundation_width":

                    self.foundation_width,


                "foundation_depth":

                    self.foundation_depth

            },



            "quantities":{


                "trench_length":

                {


                    "unit":"m",


                    "quantity":round(

                        self.trench_length(),

                        2

                    )

                },



                "excavation_volume":

                {


                    "unit":"m³",


                    "quantity":round(

                        volume,

                        2

                    )

                }

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

    def estimate(self, county=None):


        return self.summary(county)





# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":


    from pprint import pprint



    excavation = ExcavationEstimator(


        length=10,


        width=12


    )



    pprint(

        excavation.summary(

            county="Mombasa"

        )

    )