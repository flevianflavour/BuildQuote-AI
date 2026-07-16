"""
BuildQuote AI

Database Manager

Handles:
- Material prices
- Labour rates
- Equipment rates
- Saved projects
- Company profile
"""


import pandas as pd
import json
import os



class Database:


    def __init__(self):


        self.materials = pd.read_csv(
            "data/materials.csv"
        )


        self.labour = pd.read_csv(
            "data/labour.csv"
        )


        self.equipment = pd.read_csv(
            "data/equipment.csv"
        )


        self.projects_file = (
            "data/projects.json"
        )


        self.company_file = (
            "data/company.json"
        )



    # ======================================
    # MATERIAL PRICES
    # ======================================


    def get_material_price(self, material):


        row = self.materials[

            self.materials["Material"]

            ==

            material

        ]


        if not row.empty:

            return row.iloc[0]["Price"]


        return None




    # ======================================
    # LABOUR RATES
    # ======================================


    def get_labour_rate(self, job):


        row = self.labour[

            self.labour["Job"]

            ==

            job

        ]


        if not row.empty:

            return row.iloc[0]["DailyRate"]


        return None




    # ======================================
    # EQUIPMENT RATES
    # ======================================


    def get_equipment_rate(self, equipment):


        row = self.equipment[

            self.equipment["Equipment"]

            ==

            equipment

        ]


        if not row.empty:

            return row.iloc[0]["DailyHire"]


        return None




    # ======================================
    # SAVE PROJECT
    # ======================================


    def save_project(self, project):


        projects = self.get_projects()


        projects.append(project)


        with open(
            self.projects_file,
            "w"
        ) as file:


            json.dump(

                projects,

                file,

                indent=4

            )



    # ======================================
    # GET PROJECTS
    # ======================================


    def get_projects(self):


        if not os.path.exists(
            self.projects_file
        ):

            return []


        with open(
            self.projects_file,
            "r"
        ) as file:


            return json.load(file)




    # ======================================
    # SAVE COMPANY PROFILE
    # ======================================


    def save_company(self, company):


        with open(

            self.company_file,

            "w"

        ) as file:


            json.dump(

                company,

                file,

                indent=4

            )



    # ======================================
    # LOAD COMPANY PROFILE
    # ======================================


    def get_company(self):


        if not os.path.exists(
            self.company_file
        ):

            return {}


        with open(

            self.company_file,

            "r"

        ) as file:


            return json.load(file)





# ==========================================
# TEST
# ==========================================


if __name__ == "__main__":


    db = Database()


    print(
        db.get_material_price(
            "Cement"
        )
    )


    print(
        db.get_labour_rate(
            "Mason"
        )
    )


    print(
        db.get_equipment_rate(
            "Concrete Mixer"
        )
    )