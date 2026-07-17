"""
BuildQuote AI

County Pricing Engine

Loads county-specific pricing from:

data/county_prices.csv
"""

import os
import pandas as pd


class CountyPricing:

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        csv_path = os.path.join(
            base_dir,
            "data",
            "county_prices.csv"
        )

        self.data = pd.read_csv(csv_path)

        self.data.columns = self.data.columns.str.strip()

        self.data["County"] = (
            self.data["County"]
            .astype(str)
            .str.strip()
        )

        self.data["Item"] = (
            self.data["Item"]
            .astype(str)
            .str.strip()
        )

    # -------------------------------------------------

    def get_counties(self):

        return sorted(
            self.data["County"].unique().tolist()
        )

    # -------------------------------------------------

    def get_rates(self, county):

        rows = self.data[
            self.data["County"].str.lower()
            ==
            county.lower()
        ]

        if rows.empty:

            return {}

        rates = {}

        for _, row in rows.iterrows():

            key = (
                row["Item"]
                .replace(" ", "_")
                .replace("-", "_")
            )

            rates[key] = float(row["Rate"])

        return rates

    # -------------------------------------------------

    def get_rate(
        self,
        county,
        item,
        default=0
    ):

        rates = self.get_rates(county)

        return rates.get(
            item.replace(" ", "_"),
            default
        )


pricing = CountyPricing()