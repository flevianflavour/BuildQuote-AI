"""
BuildQuote AI
Professional Quotation PDF Generator
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.pdfbase.pdfmetrics import stringWidth

from datetime import datetime

import random
import os

from config.settings_manager import get_company_settings


# ==========================================================
# STYLES
# ==========================================================

styles = getSampleStyleSheet()

title_style = styles["Title"]
title_style.alignment = TA_CENTER

heading = styles["Heading2"]

normal = styles["BodyText"]

small = styles["Italic"]
small.fontSize = 8


# ==========================================================
# HELPERS
# ==========================================================

def money(value, currency):

    try:
        value = float(value)
    except Exception:
        value = 0

    return f"{currency} {value:,.2f}"


def add_table_style(table):

    table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1f4e78")),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),8),

            ("TOPPADDING",(0,0),(-1,0),8),

            ("VALIGN",(0,0),(-1,-1),"MIDDLE"),

            ("ROWBACKGROUNDS",
             (0,1),
             (-1,-1),
             [colors.white, colors.HexColor("#f5f7fa")]
            )

        ])

    )

    return table


# ==========================================================
# MAIN PDF
# ==========================================================

def generate_pdf(

    filename,

    estimate,

    client_name="Customer",

    project_name="Construction Project"

):

    company = get_company_settings()

    currency = company.get(
        "currency",
        "KES"
    )

    project = estimate.get(
        "project",
        {}
    )

    quotation_number = (
        "BQA-" +
        str(random.randint(1000,9999))
    )

    doc = SimpleDocTemplate(

        filename,

        pagesize=A4,

        rightMargin=25,

        leftMargin=25,

        topMargin=25,

        bottomMargin=25

    )

    elements = []

    # ======================================================
    # LOGO
    # ======================================================

    if company.get("show_logo", True):

        logo = company.get(
            "logo",
            "assets/logo.png"
        )

        if os.path.exists(logo):

            elements.append(

                Image(

                    logo,

                    width=75,

                    height=75

                )

            )

            elements.append(
                Spacer(1,10)
            )

    # ======================================================
    # COMPANY NAME
    # ======================================================

    elements.append(

        Paragraph(

            f"<b>{company.get('company_name','BuildQuote AI')}</b>",

            title_style

        )

    )

    elements.append(

        Paragraph(

            company.get(

                "tagline",

                "Professional Construction Estimation Platform"

            ),

            normal

        )

    )

    elements.append(
        Spacer(1,15)
    )

    # ======================================================
    # COMPANY DETAILS
    # ======================================================

    company_table = Table(

        [

            ["Contractor", company.get("contractor","")],

            ["Phone", company.get("phone","")],

            ["Email", company.get("email","")],

            ["Location", company.get("location","")],

            ["Registration", company.get("registration","")]

        ],

        colWidths=[130,300]

    )

    company_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.lightgrey),

            ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold")

        ])

    )

    elements.append(company_table)

    elements.append(
        Spacer(1,20)
    )

    # ======================================================
    # PROJECT INFORMATION
    # ======================================================

    project_table = Table(

        [

            ["Quotation No", quotation_number],

            ["Date", datetime.now().strftime("%d %B %Y")],

            ["Client", client_name],

            ["Project", project_name],

            ["County", project.get("County","")],

            ["Project Type", project.get("Project Type","")],

            ["House Type", project.get("House Type","")],

            ["Wall Material", project.get("Block Type","")],

            ["Roof Type", project.get("Roof Type","")],

            ["Bedrooms", str(project.get("Bedrooms",""))],

            ["Length", str(project.get("Length",""))],

            ["Width", str(project.get("Width",""))],

            ["Wall Height", str(project.get("Wall Height",""))]

        ],

        colWidths=[140,290]

    )

    project_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.lightgrey),

            ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold")

        ])

    )

    elements.append(project_table)

    elements.append(
        Spacer(1,20)
    )    # ======================================================
    # BILL OF QUANTITIES
    # ======================================================

    elements.append(

        Paragraph(

            "<b>BILL OF QUANTITIES (BOQ)</b>",

            heading

        )

    )

    elements.append(
        Spacer(1, 8)
    )

    boq_rows = [

        [
            "Section",
            "Description",
            "Value"
        ]

    ]

    sections = estimate.get(
        "sections",
        {}
    )

    for section_name, section in sections.items():

        if not isinstance(section, dict):
            continue

        # ---------------------------------------
        # Section Title
        # ---------------------------------------

        boq_rows.append(

            [
                section_name,
                "",
                ""
            ]

        )

        for key, value in section.items():

            if isinstance(value, (dict, list)):
                continue

            label = (

                key
                .replace("_", " ")
                .title()

            )

            boq_rows.append(

                [
                    "",
                    label,
                    str(value)
                ]

            )

    boq_table = Table(

        boq_rows,

        colWidths=[
            120,
            220,
            120
        ],

        repeatRows=1

    )

    add_table_style(
        boq_table
    )

    elements.append(
        boq_table
    )

    elements.append(
        Spacer(1,20)
    )

    # ======================================================
    # MATERIAL SUMMARY
    # ======================================================

    elements.append(

        Paragraph(

            "<b>MATERIAL SUMMARY</b>",

            heading

        )

    )

    elements.append(
        Spacer(1,8)
    )

    material_rows = [

        [
            "Section",
            "Material",
            "Quantity"
        ]

    ]

    materials = estimate.get(
        "materials",
        {}
    )

    for section_name, section in materials.items():

        if not isinstance(section, dict):
            continue

        for material, quantity in section.items():

            material_rows.append(

                [

                    section_name,

                    material
                    .replace("_"," ")
                    .title(),

                    str(quantity)

                ]

            )

    if len(material_rows) == 1:

        material_rows.append(

            [

                "-",

                "No material data",

                "-"

            ]

        )

    material_table = Table(

        material_rows,

        colWidths=[
            120,
            220,
            120
        ],

        repeatRows=1

    )

    add_table_style(
        material_table
    )

    elements.append(
        material_table
    )

    elements.append(
        Spacer(1,20)
    )

    # ======================================================
    # LABOUR SUMMARY
    # ======================================================

    elements.append(

        Paragraph(

            "<b>LABOUR SUMMARY</b>",

            heading

        )

    )

    elements.append(
        Spacer(1,8)
    )

    labour_rows = [

        [

            "Section",

            "Activity",

            "Value"

        ]

    ]

    labour = estimate.get(
        "labour",
        {}
    )

    for section_name, section in labour.items():

        if not isinstance(section, dict):
            continue

        for activity, value in section.items():

            labour_rows.append(

                [

                    section_name,

                    activity
                    .replace("_"," ")
                    .title(),

                    str(value)

                ]

            )

    if len(labour_rows) == 1:

        labour_rows.append(

            [

                "-",

                "No labour data",

                "-"

            ]

        )

    labour_table = Table(

        labour_rows,

        colWidths=[
            120,
            220,
            120
        ],

        repeatRows=1

    )

    add_table_style(
        labour_table
    )

    elements.append(
        labour_table
    )

    elements.append(
        Spacer(1,20)
    )    # ==================================================
    # PROJECT INFORMATION
    # ==================================================

    project = estimate.get("project", {})

    quotation_number = (
        f"BQA-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000,9999)}"
    )

    project_details = [
        ["Quotation No.", quotation_number],
        ["Date", datetime.now().strftime("%d %B %Y")],
        ["Client", client_name],
        ["Project", project_name],
        ["County", project.get("County", "-")],
        ["Project Type", project.get("Project Type", "-")],
        ["House Type", project.get("House Type", "-")],
        ["Wall Material", project.get("Block Type", "-")],
        ["Roof Type", project.get("Roof Type", "-")],
        ["Bedrooms", str(project.get("Bedrooms", "-"))]
    ]

    table = Table(project_details, colWidths=[160, 280])

    table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#E8F0FE")),

        ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),

        ("BOTTOMPADDING",(0,0),(-1,-1),6)

    ]))

    elements.append(table)
    elements.append(Spacer(1,18))


    # ==================================================
    # BILL OF QUANTITIES
    # ==================================================

    elements.append(
        Paragraph(
            "<b>Bill of Quantities (BOQ)</b>",
            styles["Heading2"]
        )
    )

    boq = estimate.get("boq", {})

    boq_rows = [
        [
            "Section",
            "Description",
            "Amount"
        ]
    ]

    if isinstance(boq, dict):

        for section, values in boq.items():

            amount = 0

            if isinstance(values, dict):

                amount = (
                    values.get("subtotal")
                    or values.get("total")
                    or values.get("grand_total")
                    or 0
                )

            boq_rows.append([

                section,

                section,

                f"{currency} {amount:,.2f}"

            ])

    boq_table = Table(

        boq_rows,

        colWidths=[150,220,120],

        repeatRows=1

    )

    boq_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),0.5,colors.black),

        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0F4C81")),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("ALIGN",(2,1),(2,-1),"RIGHT"),

        ("BOTTOMPADDING",(0,0),(-1,0),8)

    ]))

    elements.append(boq_table)
    elements.append(Spacer(1,20))


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

        ["Section","Material","Quantity"]

    ]

    materials = estimate.get("materials", {})

    for section, data in materials.items():

        if not isinstance(data, dict):
            continue

        for item, qty in data.items():

            material_rows.append([

                section,

                item.replace("_"," ").title(),

                str(qty)

            ])

    if len(material_rows) == 1:

        material_rows.append(["-","No Materials","-"])

    material_table = Table(

        material_rows,

        colWidths=[150,220,120]

    )

    material_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),0.5,colors.black),

        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1B5E20")),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

    ]))

    elements.append(material_table)
    elements.append(Spacer(1,20))    # ==================================================
    # LABOUR SUMMARY
    # ==================================================

    elements.append(
        Paragraph(
            "<b>Labour Summary</b>",
            styles["Heading2"]
        )
    )

    labour_rows = [
        ["Section", "Activity", "Value"]
    ]

    labour = estimate.get("labour", {})

    for section, data in labour.items():

        if not isinstance(data, dict):
            continue

        for activity, value in data.items():

            labour_rows.append([
                section,
                activity.replace("_", " ").title(),
                str(value)
            ])

    if len(labour_rows) == 1:

        labour_rows.append([
            "-",
            "No Labour Data",
            "-"
        ])

    labour_table = Table(
        labour_rows,
        colWidths=[150, 220, 120]
    )

    labour_table.setStyle(TableStyle([

        ("GRID", (0,0), (-1,-1), 0.5, colors.black),

        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#6A1B9A")),

        ("TEXTCOLOR", (0,0), (-1,0), colors.white),

        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0,0), (-1,0), 8)

    ]))

    elements.append(labour_table)
    elements.append(Spacer(1, 20))
    # ==================================================
    # COST SUMMARY
    # ==================================================

    elements.append(
        Paragraph(
            "<b>Project Cost Summary</b>",
            styles["Heading2"]
        )
    )


    material_cost = float(
        estimate.get(
            "material_cost",
            0
        )
    )


    labour_cost = float(
        estimate.get(
            "labour_cost",
            0
        )
    )


    equipment_cost = float(
        estimate.get(
            "equipment_cost",
            0
        )
    )


    subtotal = float(
        estimate.get(
            "subtotal",
            material_cost + labour_cost + equipment_cost
        )
    )


    vat_rate = company.get(
        "vat_rate",
        16
    )


    vat = float(
        estimate.get(
            "vat",
            subtotal * vat_rate / 100
        )
    )


    contingency_rate = company.get(
        "contingency",
        5
    )


    contingency = float(
        estimate.get(
            "contingency",
            subtotal * contingency_rate / 100
        )
    )


    grand_total = float(
        estimate.get(
            "grand_total",
            subtotal + vat + contingency
        )
    )


    cost_rows = [

        [
            "Materials",
            f"{currency} {material_cost:,.2f}"
        ],

        [
            "Labour",
            f"{currency} {labour_cost:,.2f}"
        ],

        [
            "Equipment",
            f"{currency} {equipment_cost:,.2f}"
        ],

        [
            "Subtotal",
            f"{currency} {subtotal:,.2f}"
        ],

        [
            f"VAT ({vat_rate}%)",
            f"{currency} {vat:,.2f}"
        ],

        [
            f"Contingency ({contingency_rate}%)",
            f"{currency} {contingency:,.2f}"
        ],

        [
            "GRAND TOTAL",
            f"{currency} {grand_total:,.2f}"
        ]

    ]


    cost_table = Table(
        cost_rows,
        colWidths=[250,160]
    )


    cost_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),0.5,colors.black),

        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#E8F0FE")),

        ("BACKGROUND",(0,6),(-1,6),colors.HexColor("#FFF59D")),

        ("FONTNAME",(0,6),(-1,6),"Helvetica-Bold"),

        ("ALIGN",(1,0),(1,-1),"RIGHT")

    ]))


    elements.append(cost_table)

    elements.append(
        Spacer(1,25)
    )

     # ==================================================
    # SIGNATURE SECTION
    # ==================================================

    elements.append(
        Paragraph(
            "<b>Approval & Signatures</b>",
            styles["Heading2"]
        )
    )

    signature_rows = [

        [
            "Prepared By",
            "Client Approval"
        ],

        [
            "",
            ""
        ],

        [
            "________________________",
            "________________________"
        ],

        [
            company.get(
                "contractor",
                company.get(
                    "company_name",
                    "BuildQuote AI"
                )
            ),
            client_name
        ]

    ]

    signature_table = Table(

        signature_rows,

        colWidths=[250, 250]

    )

    signature_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#E8F0FE")),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("BOTTOMPADDING",(0,0),(-1,0),8),

        ("TOPPADDING",(0,1),(-1,-1),12)

    ]))

    elements.append(signature_table)

    elements.append(
        Spacer(1,20)
    )


    # ==================================================
    # NOTES
    # ==================================================

    elements.append(

        Paragraph(

            "<b>Notes</b>",

            styles["Heading2"]

        )

    )

    notes = [

        "• This quotation is valid for 30 days from the date of issue.",

        "• Material prices are based on current market rates and may change without notice.",

        "• Final costs may vary after site inspection, soil investigation and client variations.",

        "• Construction shall comply with the Kenya Building Code and County Government regulations.",

        "• Payments shall follow the agreed project milestones."

    ]

    for note in notes:

        elements.append(
            Paragraph(
                note,
                styles["Normal"]
            )
        )

    elements.append(
        Spacer(1,20)
    )


    # ==================================================
    # FOOTER
    # ==================================================

    elements.append(
        Paragraph(
            "<b>Thank you for choosing "
            f"{company.get('company_name','BuildQuote AI')}</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            company.get(
                "tagline",
                "Professional Construction Estimation & BOQ Services"
            ),
            styles["Italic"]
        )
    )

    elements.append(
        Spacer(1,10)
    )

    elements.append(
        Paragraph(
            f"""
            Generated on {datetime.now().strftime('%d %B %Y at %I:%M %p')}<br/>
            Contractor: {company.get('contractor','')}<br/>
            Phone: {company.get('phone','')}<br/>
            Email: {company.get('email','')}<br/>
            Website: {company.get('website','')}<br/><br/>
            <b>Generated Automatically by BuildQuote AI v2.0</b><br/>
            © 2026 BuildQuote AI | Developed by Flavian Otieno
            """,
            styles["Normal"]
        )
    )


    # ==================================================
    # BUILD PDF
    # ==================================================

    doc.build(elements)

    return filename