"""
BuildQuote AI

Quotation PDF Generator

Generates:
- Company Header
- Client Details
- BOQ
- Materials Summary
- Labour Summary
- Cost Summary
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


from config.company_profile import COMPANY_PROFILE



def generate_pdf(

    filename,

    estimate,

    client_name="Customer",

    project_name="Construction Project",

):


    doc = SimpleDocTemplate(

        filename,

        pagesize=A4

    )


    styles = getSampleStyleSheet()

    elements = []



    # =====================================
    # COMPANY HEADER
    # =====================================


    logo_path = COMPANY_PROFILE.get(
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

            f"<b><font size=22>{COMPANY_PROFILE.get('company_name','BuildQuote AI')}</font></b>",

            styles["Title"]

        )

    )


    elements.append(

        Paragraph(

            COMPANY_PROFILE.get(
                "tagline",
                "Construction Estimation & BOQ System"
            ),

            styles["Normal"]

        )

    )


    elements.append(
        Spacer(1,15)
    )



    # COMPANY DETAILS


    company_table = Table(

        [

            [
                "Phone",
                COMPANY_PROFILE.get("phone","")
            ],

            [
                "Email",
                COMPANY_PROFILE.get("email","")
            ],

            [
                "Location",
                COMPANY_PROFILE.get("location","")
            ],

            [
                "Registration",
                COMPANY_PROFILE.get("registration","")
            ]

        ],

        colWidths=[120,300]

    )


    company_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.black),

            ("BACKGROUND",(0,0),(0,-1),colors.lightgrey)

        ])

    )


    elements.append(company_table)

    elements.append(
        Spacer(1,20)
    )



    # =====================================
    # PROJECT DETAILS
    # =====================================


    project = estimate.get(
        "project",
        {}
    )


    details = [

        [
            "Quotation No",
            f"BQA-{random.randint(1000,9999)}"
        ],

        [
            "Date",
            datetime.now().strftime("%d %B %Y")
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
            project.get("County","")
        ],

        [
            "House Type",
            project.get("House Type","")
        ],

        [
            "Roof Type",
            project.get("Roof Type","")
        ],

        [
            "Wall Material",
            project.get("Block Type","")
        ]

    ]


    table = Table(

        details,

        colWidths=[150,250]

    )


    table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.black),

            ("BACKGROUND",(0,0),(0,-1),colors.lightgrey)

        ])

    )


    elements.append(table)

    elements.append(
        Spacer(1,20)
    )



    # =====================================
    # BOQ
    # =====================================


    elements.append(

        Paragraph(

            "<b>Bill of Quantities</b>",

            styles["Heading2"]

        )

    )


    boq_rows = [

        [
            "Description",
            "Qty",
            "Unit",
            "Rate",
            "Amount"
        ]

    ]


    for item in estimate.get("boq",[]):

        boq_rows.append(

            [

                item.get("description",""),

                item.get("quantity",""),

                item.get("unit",""),

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

            ("GRID",(0,0),(-1,-1),0.5,colors.black),

            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white)

        ])

    )


    elements.append(boq_table)

    elements.append(
        Spacer(1,20)
    )



    # =====================================
    # MATERIAL SUMMARY
    # =====================================


    elements.append(

        Paragraph(

            "<b>Material Summary</b>",

            styles["Heading2"]

        )

    )


    material_rows = [

        [
            "Section",
            "Materials"
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


    material_table = Table(material_rows)


    material_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.black)

        ])

    )


    elements.append(material_table)

    elements.append(
        Spacer(1,20)
    )



    # =====================================
    # COST SUMMARY
    # =====================================


    summary = Table(

        [

            [
                "Subtotal",
                f"KES {estimate.get('subtotal',0):,.2f}"
            ],

            [
                "VAT 16%",
                f"KES {estimate.get('vat',0):,.2f}"
            ],

            [
                "TOTAL PROJECT COST",
                f"KES {estimate.get('grand_total',0):,.2f}"
            ]

        ]

    )


    summary.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.black),

            ("BACKGROUND",(0,2),(-1,2),colors.lightgrey)

        ])

    )


    elements.append(summary)

    elements.append(
        Spacer(1,25)
    )



    # =====================================
    # SIGNATURE
    # =====================================


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
                COMPANY_PROFILE.get(
                    "contractor",
                    "Contractor"
                ),

                client_name
            ]

        ]

    )


    signature.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.black)

        ])

    )


    elements.append(signature)


    elements.append(

        Paragraph(

            f"Generated automatically by {COMPANY_PROFILE.get('company_name','BuildQuote AI')}",

            styles["Italic"]

        )

    )


    doc.build(elements)