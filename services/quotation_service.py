"""
BuildQuote AI

Quotation Service v3

Generates professional quotation summary
from the Master BOQ.
"""





class QuotationService:



    def generate(

        self,

        project,

        estimate

    ):



        # =====================================
        # COST SUMMARY
        # =====================================


        subtotal = estimate.get(

            "subtotal",

            0

        )



        vat = estimate.get(

            "vat",

            subtotal * 0.16

        )



        total = estimate.get(

            "grand_total",

            subtotal + vat

        )





        print("\n")

        print("=" * 60)

        print("                 BUILDQUOTE AI")

        print("          CONSTRUCTION QUOTATION")

        print("=" * 60)



        print()

        print(f"Quotation No : {project.project_id}")

        print(f"Client       : {project.client_name}")

        print(f"Project      : {project.project_name}")

        print(f"County       : {project.county}")

        print(f"Location     : {project.location}")



        print("-" * 60)



        print(

            "DESCRIPTION".ljust(30),

            "AMOUNT"

        )



        print("-" * 60)





        # =====================================
        # SECTION BREAKDOWN
        # =====================================


        sections = estimate.get(

            "construction_sections",

            {}

        )



        for name, section in sections.items():


            if isinstance(section, dict):


                amount = section.get(

                    "subtotal",

                    section.get(

                        "total",

                        0

                    )

                )


                print(

                    name.ljust(30),

                    f"KES {amount:,.2f}"

                )





        print("-" * 60)



        print(

            "SUBTOTAL".ljust(30),

            f"KES {subtotal:,.2f}"

        )



        print(

            "VAT (16%)".ljust(30),

            f"KES {vat:,.2f}"

        )



        print(

            "GRAND TOTAL".ljust(30),

            f"KES {total:,.2f}"

        )



        print("=" * 60)



        return {



            "quotation_number":

            project.project_id,



            "client":

            project.client_name,



            "project":

            project.project_name,



            "county":

            project.county,



            "subtotal":

            round(subtotal,2),



            "vat":

            round(vat,2),



            "grand_total":

            round(total,2),



            "sections":

            sections

        }