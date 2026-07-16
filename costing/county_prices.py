"""
BuildQuote AI
County Pricing Engine

Loads county-specific material and labour rates from:

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

        self.data["County"] = self.data["County"].str.strip()

    # ------------------------------------------------

    def get_counties(self):

        return sorted(
            self.data["County"].unique().tolist()
        )

    # ------------------------------------------------

    def get_rates(self, county):

        row = self.data[
            self.data["County"].str.lower()
            ==
            county.lower()
        ]

        if row.empty:

            raise ValueError(
                f"County '{county}' not found."
            )

        row = row.iloc[0]

        return {

            # ==========================================
            # FOUNDATION
            # ==========================================

            "Excavation": row["Excavation"],
            "Hardcore": row["Hardcore"],
            "Blinding": row["Blinding"],
            "Concrete": row["Concrete"],

            "Cement_Bag": row["Cement_Bag"],
            "Sand_m3": row["Sand_m3"],
            "Ballast_m3": row["Ballast_m3"],

            "Machine_Cut_Stone": row["Machine_Cut_Stone"],
            "Quarry_Stone": row["Quarry_Stone"],

            "Steel_kg": row["Steel_kg"],
            "Binding_Wire_kg": row["Binding_Wire_kg"],

            "DPC_m": row["DPC_m"],
            "DPM_m2": row["DPM_m2"],
            "Anti_Termite_m2": row["Anti_Termite_m2"],

            # ==========================================
            # ROOF
            # ==========================================

            "Timber": row["Timber"],
            "Iron_Sheet": row["Iron_Sheet"],
            "Ridge_Cap": row["Ridge_Cap"],
            "Roof_Nails": row["Roof_Nails"],

            # ==========================================
            # FINISHES
            # ==========================================

            "Plaster": row["Plaster"],
            "Paint": row["Paint"],
            "Floor_Tile": row["Floor_Tile"],
            "Ceiling_Board": row["Ceiling_Board"],

            # ==========================================
            # ELECTRICAL
            # ==========================================

            "Cable": row["Cable"],
            "Conduit": row["Conduit"],
            "Socket": row["Socket"],
            "Switch": row["Switch"],
            "Light": row["Light"],
            "Distribution_Board": row["Distribution_Board"],

            # ==========================================
            # PLUMBING
            # ==========================================

            "Water_Pipe": row["Water_Pipe"],
            "Waste_Pipe": row["Waste_Pipe"],
            "Toilet": row["Toilet"],
            "Wash_Basin": row["Wash_Basin"],
            "Kitchen_Sink": row["Kitchen_Sink"],
            "Shower_Mixer": row["Shower_Mixer"],
            "Floor_Trap": row["Floor_Trap"],

            # ==========================================
            # DOORS & WINDOWS
            # ==========================================

            "External_Door": row["External_Door"],
            "Internal_Door": row["Internal_Door"],
            "Window": row["Window"],
            "Frame": row["Frame"],
            "Door_Lock": row["Door_Lock"],

            # ==========================================
            # LABOUR
            # ==========================================

            "Mason_Day": row["Mason_Day"],
            "Fundi_Day": row["Fundi_Day"],
            "Labourer_Day": row["Labourer_Day"],
            "Carpenter_Day": row["Carpenter_Day"],
            "Steel_Fixer_Day": row["Steel_Fixer_Day"],
            "Electrician_Day": row["Electrician_Day"],
            "Plumber_Day": row["Plumber_Day"]

        }


pricing = CountyPricing()