"""
BuildQuote AI

Material Calculation Engine

This module calculates material quantities only.

No prices are used here.

Pricing is handled by county_prices.py
"""

import math


class MaterialEngine:

    # ------------------------------------
    # Concrete Mix
    # ------------------------------------

    def concrete_mix(self, volume, mix="1:2:4"):
        """
        Returns estimated material quantities
        for concrete.

        volume -> m3
        """

        mixes = {

            "1:2:4": {
                "cement": 7.3,
                "sand": 0.44,
                "ballast": 0.88,
                "water": 210
            },

            "1:3:6": {
                "cement": 5.2,
                "sand": 0.55,
                "ballast": 1.10,
                "water": 180
            }

        }

        if mix not in mixes:

            raise ValueError(
                f"Unsupported mix: {mix}"
            )

        data = mixes[mix]

        return {

            "cement_bags": math.ceil(
                volume * data["cement"]
            ),

            "sand_m3": round(
                volume * data["sand"],
                2
            ),

            "ballast_m3": round(
                volume * data["ballast"],
                2
            ),

            "water_litres": round(
                volume * data["water"]
            )

        }

    # ------------------------------------
    # Mortar
    # ------------------------------------

    def mortar_mix(self, volume):

        return {

            "cement_bags": math.ceil(
                volume * 6.5
            ),

            "sand_m3": round(
                volume * 1.10,
                2
            )

        }

    # ------------------------------------
    # Plaster
    # ------------------------------------

    def plaster_mix(self, area):

        cement = area * 0.18

        sand = area * 0.018

        return {

            "cement_bags": math.ceil(cement),

            "sand_m3": round(
                sand,
                2
            )

        }

    # ------------------------------------
    # Floor Screed
    # ------------------------------------

    def screed_mix(self, area):

        cement = area * 0.22

        sand = area * 0.025

        return {

            "cement_bags": math.ceil(cement),

            "sand_m3": round(
                sand,
                2
            )

        }

    # ------------------------------------
    # Walling
    # ------------------------------------

    def wall_materials(
        self,
        wall_area,
        block_type="Machine Cut Stone"
    ):

        if block_type == "Machine Cut Stone":

            blocks = math.ceil(
                wall_area * 12.5
            )

        else:

            blocks = math.ceil(
                wall_area * 10
            )

        mortar = self.mortar_mix(
            wall_area * 0.03
        )

        return {

            "blocks": blocks,

            "cement_bags":
                mortar["cement_bags"],

            "sand_m3":
                mortar["sand_m3"]

        }


material_engine = MaterialEngine()