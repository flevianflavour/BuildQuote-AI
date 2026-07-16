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

        # -----------------------------
        # Project Information
        # -----------------------------

        self.client_name = client_name
        self.project_name = project_name

        self.project_type = project_type
        self.house_type = house_type

        self.county = county

        # -----------------------------
        # Building Details
        # -----------------------------

        self.floors = floors

        self.length = length
        self.width = width
        self.height = height

        self.wall_material = wall_material
        self.roof_type = roof_type

        # -----------------------------
        # System Information
        # -----------------------------

        self.created_at = datetime.now()

        self.project_id = (
            f"BQ-{self.created_at.strftime('%Y%m%d%H%M%S')}"
        )

    # ---------------------------------

    def summary(self):

        return {

            "Project ID": self.project_id,

            "Client": self.client_name,

            "Project": self.project_name,

            "County": self.county,

            "Project Type": self.project_type,

            "House Type": self.house_type,

            "Floors": self.floors,

            "Length": self.length,

            "Width": self.width,

            "Height": self.height,

            "Wall Material": self.wall_material,

            "Roof Type": self.roof_type,

            "Created": self.created_at.strftime("%d-%m-%Y %H:%M")

        }