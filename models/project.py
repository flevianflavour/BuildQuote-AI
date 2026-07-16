from datetime import datetime


class Project:


    def __init__(

        self,

        client_name,

        project_name,

        county,

        project_type,

        house_type,

        floors,

        length,

        width,

        height,

        wall_material,

        roof_type

    ):


        # =============================
        # Project Information
        # =============================

        self.client_name = client_name

        self.project_name = project_name

        self.county = county

        self.project_type = project_type

        self.house_type = house_type



        # =============================
        # Building Details
        # =============================

        self.floors = floors

        self.length = length

        self.width = width

        self.height = height


        self.wall_material = wall_material

        self.roof_type = roof_type



        # =============================
        # System Information
        # =============================

        self.created_at = datetime.now()


        self.project_id = (

            f"BQ-{self.created_at.strftime('%Y%m%d%H%M%S')}"

        )



    # =================================
    # Convert Project To Dictionary
    # =================================

    def summary(self):


        return {


            "project_id":

            self.project_id,


            "client_name":

            self.client_name,


            "project_name":

            self.project_name,


            "county":

            self.county,


            "project_type":

            self.project_type,


            "house_type":

            self.house_type,


            "floors":

            self.floors,


            "length":

            self.length,


            "width":

            self.width,


            "height":

            self.height,


            "wall_material":

            self.wall_material,


            "roof_type":

            self.roof_type,


            "created_at":

            self.created_at.strftime(
                "%d-%m-%Y %H:%M"
            )

        }