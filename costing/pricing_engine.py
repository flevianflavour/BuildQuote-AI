"""
BuildQuote AI

Pricing Engine

Gets material and labour prices
for the selected county.
"""

import pandas as pd
import os


class PricingEngine:

    def __init__(self):

        base = os.path.dirname(
            os.path.dirname(__file__)
        )

        csv_file = os.path.join(
            base,
            "data",
            "rate_database.csv"
        )

        self.df = pd.read_csv(csv_file)

    # ----------------------------------

    def get_rate(

        self,

        county,

        item

    ):

        result = self.df[

            (self.df["County"].str.lower() == county.lower())

            &

            (self.df["Item"].str.lower() == item.lower())

        ]

        if result.empty:

            return None

        return float(

            result.iloc[0]["Rate"]

        )

    # ----------------------------------

    def list_items(

        self,

        county

    ):

        result = self.df[

            self.df["County"].str.lower()

            ==

            county.lower()

        ]

        return result


pricing_engine = PricingEngine()