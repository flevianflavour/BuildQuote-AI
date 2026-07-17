"""
BuildQuote AI

Project Model

Stores:
• Client Information
• Building Details
• Construction Preferences
• System Metadata
"""


from datetime import datetime
import uuid





class Project:



    def __init__(

        self,


        client_name,


        project_name,


        county,


        project_type,


        house_type=None,


        floors=1,


        length=10,


        width=12,


        height=3,


        wall_material="Machine Cut Stone",


        roof_type="Mabati",


        bedrooms=3,


        contractor="BuildQuote AI",


        location=None

    ):



        # ==================================
        # CLIENT INFORMATION
        # ==================================


        self.client_name = client_name


        self.project_name = project_name


        self.contractor = contractor


        self.location = location or county





        # ==================================
        # PROJECT DETAILS
        # ==================================


        self.county = county


        self.project_type = project_type


        self.house_type = house_type



        self.bedrooms = bedrooms





        # ==================================
        # BUILDING DIMENSIONS
        # ==================================


        self.floors = floors


        self.length = length


        self.width = width


        self.height = height





        # ==================================
        # MATERIAL SELECTION
        # ==================================


        self.wall_material = wall_material


        self.roof_type = roof_type





        # ==================================
        # SYSTEM INFORMATION
        # ==================================


        self.created_at = datetime.now()



        self.project_id = (

            f"BQ-{self.created_at.strftime('%Y%m%d%H%M%S')}-"

            f"{uuid.uuid4().hex[:4].upper()}"

        )






    # ==================================
    # PROJECT SUMMARY
    # ==================================

    def summary(self):


        return {


            "project_id":

            self.project_id,



            "client_name":

            self.client_name,



            "project_name":

            self.project_name,



            "contractor":

            self.contractor,



            "location":

            self.location,



            "county":

            self.county,



            "project_type":

            self.project_type,



            "house_type":

            self.house_type,



            "bedrooms":

            self.bedrooms,



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




    # ==================================
    # DICTIONARY FORMAT
    # For Database / Session / PDF
    # ==================================

    def to_dict(self):


        return self.summary()





    # ==================================
    # DISPLAY NAME
    # ==================================

    def __str__(self):


        return (

            f"{self.project_name} - "

            f"{self.client_name}"

        )