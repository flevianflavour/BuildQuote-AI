"""
BuildQuote AI

Quotation PDF Generator

Features:
- Company Header
- Logo
- Client Details
- Project Details
- BOQ
- Materials Summary
- Labour Summary
- Cost Summary
- VAT
- Contingency
- Signature Section
"""


from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from datetime import datetime

import random
import os


from config.settings_manager import get_company_settings



# ==================================================
# GENERATE PDF
# ==================================================


def generate_pdf(

    filename,

    estimate,

    client_name="Customer",

    project_name="Construction Project"

):


    company = get_company_settings()



    doc = SimpleDocTemplate(

        filename,

        pagesize=A4

    )


    styles = getSampleStyleSheet()


    elements = []



    currency = company.get(
        "currency",
        "KES"
    )



    # ==================================================
    # COMPANY HEADER
    # ==================================================


    if company.get(
        "show_logo",
        True
    ):


        logo_path = company.get(

            "logo",

            "assets/logo.png"

        )


        if os.path.exists(logo_path):


            elements.append(

                Image(

                    logo_path,

                    width=80,

                    height=80

                )

            )



    elements.append(

        Paragraph(

            f"""

            <b>

            <font size=22>

            {company.get('company_name','BuildQuote AI')}

            </font>

            </b>

            """,

            styles["Title"]

        )

    )



    elements.append(

        Paragraph(

            company.get(

                "tagline",

                "Construction Estimation & BOQ System"

            ),

            styles["Normal"]

        )

    )


    elements.append(
        Spacer(1,15)
    )



    # ==================================================
    # COMPANY DETAILS
    # ==================================================


    company_details = Table(

        [

            [
                "Contractor",
                company.get("contractor","")
            ],

            [
                "Phone",
                company.get("phone","")
            ],

            [
                "Email",
                company.get("email","")
            ],

            [
                "Location",
                company.get("location","")
            ],

            [
                "Registration",
                company.get("registration","")
            ]

        ],

        colWidths=[120,300]

    )



    company_details.setStyle(

        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            ),

            (
                "BACKGROUND",
                (0,0),
                (0,-1),
                colors.lightgrey
            )

        ])

    )



    elements.append(company_details)

    elements.append(
        Spacer(1,20)
    )



    # ==================================================
    # PROJECT INFORMATION
    # ==================================================


    project = estimate.get(
        "project",
        {}
    )



    quotation_number = (

        "BQA-"

        +

        str(
            random.randint(
                1000,
                9999
            )
        )

    )



    project_details = Table(

        [

            [
                "Quotation No",
                quotation_number
            ],

            [
                "Date",
                datetime.now().strftime(
                    "%d %B %Y"
                )
            ],

            [
                "Client",
                client_name
            ],

            [
                "Project",
                project_name
            ],

            [
                "County",
                project.get(
                    "county",
                    ""
                )
            ],

            [
                "House Type",
                project.get(
                    "house_type",
                    ""
                )
            ],

            [
                "Roof Type",
                project.get(
                    "roof_type",
                    ""
                )
            ],

            [
                "Wall Material",
                project.get(
                    "wall_material",
                    ""
                )
            ]

        ],

        colWidths=[150,250]

    )



    project_details.setStyle(

        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            ),

            (
                "BACKGROUND",
                (0,0),
                (0,-1),
                colors.lightgrey
            )

        ])

    )



    elements.append(project_details)

    elements.append(
        Spacer(1,20)
    )



    # ==================================================
    # BOQ
    # ==================================================


    elements.append(

        Paragraph(

            "<b>Bill of Quantities</b>",

            styles["Heading2"]

        )

    )



    boq_rows = [

        [
            "Description",
            "Quantity",
            "Unit",
            "Rate",
            "Amount"
        ]

    ]



    for item in estimate.get(
        "boq",
        []
    ):


        boq_rows.append(

            [

                item.get(
                    "description",
                    ""
                ),

                item.get(
                    "quantity",
                    ""
                ),

                item.get(
                    "unit",
                    ""
                ),

                f"{item.get('rate',0):,.2f}",

                f"{item.get('amount',0):,.2f}"

            ]

        )



    boq_table = Table(

        boq_rows,

        repeatRows=1

    )



    boq_table.setStyle(

        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            ),

            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.darkblue
            ),

            (
                "TEXTCOLOR",
                (0,0),
                (-1,0),
                colors.white
            )

        ])

    )



    elements.append(boq_table)

    elements.append(
        Spacer(1,20)
    )



    # ==================================================
    # MATERIAL SUMMARY
    # ==================================================


    elements.append(

        Paragraph(

            "<b>Material Summary</b>",

            styles["Heading2"]

        )

    )



    material_rows = [

        [
            "Section",
            "Details"
        ]

    ]



    for section,data in estimate.get(
        "materials",
        {}
    ).items():


        material_rows.append(

            [

                section,

                str(data)

            ]

        )



    material_table = Table(
        material_rows
    )


    material_table.setStyle(

        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            )

        ])

    )


    elements.append(material_table)

    elements.append(
        Spacer(1,20)
    )



    # ==================================================
    # COST SUMMARY
    # ==================================================


    subtotal = estimate.get(
        "subtotal",
        0
    )


    vat = estimate.get(
        "vat",
        subtotal * company.get(
            "vat_rate",
            16
        ) / 100
    )


    contingency = estimate.get(
        "contingency",
        subtotal * company.get(
            "contingency",
            5
        ) / 100
    )



    total = (

        subtotal

        +

        vat

        +

        contingency

    )



    cost_table = Table(

        [

            [
                "Subtotal",
                f"{currency} {subtotal:,.2f}"
            ],

            [
                "VAT",
                f"{currency} {vat:,.2f}"
            ],

            [
                "Contingency",
                f"{currency} {contingency:,.2f}"
            ],

            [
                "TOTAL PROJECT COST",
                f"{currency} {total:,.2f}"
            ]

        ]

    )



    cost_table.setStyle(

        TableStyle([

            (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                colors.black
            ),

            (
                "BACKGROUND",
                (0,3),
                (-1,3),
                colors.lightgrey
            )

        ])

    )


    elements.append(cost_table)



    elements.append(
        Spacer(1,25)
    )



    # ==================================================
    # SIGNATURE SECTION
    # ==================================================


    if company.get(
        "show_signature",
        True
    ):


        signature = Table(

            [

                [
                    "Prepared By",
                    "Client Approval"
                ],

                [
                    "________________",
                    "________________"
                ],

                [
                    company.get(
                        "contractor",
                        "Contractor"
                    ),

                    client_name

                ]

            ]

        )


        signature.setStyle(

            TableStyle([

                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    0.5,
                    colors.black
                )

            ])

        )


        elements.append(signature)



    elements.append(

        Spacer(1,15)

    )


    elements.append(

        Paragraph(

            f"""

            Generated automatically by

            {company.get('company_name','BuildQuote AI')}

            """,

            styles["Italic"]

        )

    )



    doc.build(elements)