"""
BuildQuote AI

New Estimate Page
Professional Construction Estimator
Version 3.0

Connected To:
- Estimation Engine v3
- Estimation Service
- County Pricing
- BOQ Generator
- PDF Generator
"""

import streamlit as st
import pandas as pd

from services.estimation_service import EstimationService
from models.project import Project

from quotation_generator import generate_pdf

from services.ai_assistant import get_ai_recommendations

from config.counties import COUNTIES
from config.settings_manager import get_company_settings



# =====================================================
# COMPANY SETTINGS
# =====================================================

company = get_company_settings()


company_name = company.get(
    "company_name",
    "BuildQuote AI"
)


currency = company.get(
    "currency",
    "KES"
)


logo = company.get(
    "logo",
    "assets/logo.png"
)


show_logo = company.get(
    "show_logo",
    True
)



# =====================================================
# PAGE CONFIGURATION
# =====================================================


st.set_page_config(

    page_title=f"{company_name} - New Estimate",

    page_icon="🏗️",

    layout="wide",

    initial_sidebar_state="expanded"

)



# =====================================================
# CUSTOM CSS
# =====================================================


st.markdown(

"""

<style>


#MainMenu{
display:none;
}


footer{
display:none;
}


header{
display:none;
}



.block-container{

padding-top:1rem;

padding-bottom:2rem;

}



section[data-testid="stSidebar"]{

background:#0f172a;

}



section[data-testid="stSidebar"] *{

color:white;

}



div[data-testid="stMetric"]{

background:#1e293b;

color:white;

padding:15px;

border-radius:12px;

border:1px solid #334155;

box-shadow:0 2px 10px rgba(0,0,0,.25);

}

div[data-testid="stMetric"] label{

color:#cbd5e1 !important;

}

div[data-testid="stMetricValue"]{

color:white !important;

}




</style>


""",

unsafe_allow_html=True

)




# =====================================================
# SIDEBAR
# =====================================================


with st.sidebar:


    if show_logo:

        try:

            st.image(

                logo,

                width=150

            )

        except:

            st.title(

                "🏗️ " + company_name

            )

    else:

        st.title(

            company_name

        )


    st.markdown(

        f"## {company_name}"

    )


    st.caption(

        "Professional Construction Intelligence Platform"

    )


    st.divider()


    modules = [

        "🏗 Foundation",

        "🧱 Walling",

        "🪨 Mortar",

        "🏠 Roofing",

        "🎨 Finishes",

        "⚡ Electrical",

        "🚰 Plumbing",

        "🚪 Doors & Windows",

        "📄 PDF Reports"

    ]


    for module in modules:

        st.write(module)



    st.divider()


    st.success(

        "🇰🇪 Kenyan Construction Standards"

    )





# =====================================================
# HEADER
# =====================================================


st.title(

    "🏗️ Create New Construction Estimate"

)


st.caption(

    "Generate BOQ, material quantities, labour costing and professional quotation."

)


st.divider()




# =====================================================
# CLIENT INFORMATION
# =====================================================

st.header("👤 Client Information")

if "client_name" not in st.session_state:
    st.session_state["client_name"] = ""

if "project_name" not in st.session_state:
    st.session_state["project_name"] = ""

col1, col2 = st.columns(2)

with col1:

    client_name = st.text_input(
        "Client Name",
        key="client_name",
        placeholder="Flavian Otieno"
    )

with col2:

    project_name = st.text_input(
        "Project Name",
        key="project_name",
        placeholder="3 Bedroom Residential House"
    )





# =====================================================
# PROJECT DETAILS
# =====================================================


st.header(

    "🏠 Project Details"

)



p1,p2,p3 = st.columns(3)



with p1:


    county = st.selectbox(

        "County",

        COUNTIES

    )



with p2:


    project_type = st.selectbox(

        "Project Type",

        [

            "Residential",

            "Commercial"

        ]

    )



with p3:


    house_type = st.selectbox(

        "House Type",

        [

            "Bedsitter",

            "1 Bedroom",

            "2 Bedroom",

            "3 Bedroom",

            "4 Bedroom",

            "Maisonette",

            "Villa"

        ]

    )



# =====================================================
# MATERIAL SELECTION
# =====================================================


st.header(

    "🧱 Building Materials"

)



m1,m2 = st.columns(2)



with m1:


    wall_material = st.selectbox(

        "Wall Material",

        [

            "Machine Cut Stone",

            "Concrete Blocks",

            "Clay Bricks",

            "Coral Blocks"

        ]

    )



with m2:


    roof_type = st.selectbox(

        "Roof Type",

        [

            "Mabati",

            "Tile Roof",

            "Decra Roof",

            "Concrete Roof"

        ]

    )# =====================================================
# BUILDING DIMENSIONS
# =====================================================

st.header(
    "📐 Building Dimensions"
)


d1,d2,d3 = st.columns(3)



with d1:

    length = st.number_input(

        "Length (Metres)",

        min_value=1.0,

        value=10.0,

        step=0.5

    )



with d2:

    width = st.number_input(

        "Width (Metres)",

        min_value=1.0,

        value=12.0,

        step=0.5

    )



with d3:

    height = st.number_input(

        "Wall Height (Metres)",

        min_value=2.0,

        value=3.0,

        step=0.1

    )





# =====================================================
# PROJECT PREVIEW
# =====================================================


st.divider()


st.header(
    "📋 Project Preview"
)



floor_area = length * width



c1,c2,c3,c4 = st.columns(4)



c1.metric(

    "County",

    county

)


c2.metric(

    "House Type",

    house_type

)


c3.metric(

    "Wall Material",

    wall_material

)


c4.metric(

    "Floor Area",

    f"{floor_area:.1f} m²"

)



st.divider()




# =====================================================
# GENERATE ESTIMATE
# =====================================================

if st.button(
    "🚀 Generate Professional Estimate",
    type="primary",
    use_container_width=True
):

    if not client_name.strip():
        st.error("Please enter the client name.")
        st.stop()

    if not project_name.strip():
        st.error("Please enter the project name.")
        st.stop()

    with st.spinner("Running BuildQuote AI Estimation Engine..."):

        try:

            # -------------------------------------
            # CREATE PROJECT
            # -------------------------------------

            project = Project(
                client_name=client_name,
                project_name=project_name,
                county=county,
                project_type=project_type,
                house_type=house_type,
                wall_material=wall_material,
                roof_type=roof_type,
                length=length,
                width=width,
                height=height
            )

                        # -------------------------------------
            # RUN ESTIMATION ENGINE
            # -------------------------------------

            service = EstimationService()

            estimate = service.estimate(project)

            # -------------------------------------
            # STORE PROJECT DETAILS INSIDE ESTIMATE
            # -------------------------------------

            estimate["client_name"] = client_name
            estimate["project_name"] = project_name

            # Also keep project details together

            estimate["project"] = {

                "Client": client_name,

                "Project Name": project_name,

                "County": county,

                "Project Type": project_type,

                "House Type": house_type,

                "Block Type": wall_material,

                "Roof Type": roof_type,

                "Bedrooms": (
                    "Bedsitter"
                    if house_type == "Bedsitter"
                    else house_type.replace(" Bedroom", "")
                ),

                "Length": length,

                "Width": width,

                "Wall Height": height,

                "Floor Area": round(length * width, 2)

            }

            # -------------------------------------
            # SAVE SESSION
            # -------------------------------------

            st.session_state["estimate"] = estimate

            st.success(
                "✅ Estimate generated successfully"
            )

            st.rerun()

        except Exception as e:

            st.error(
                f"Estimation failed: {e}"
            )
# =====================================================
# LOAD GENERATED ESTIMATE
# =====================================================


if "estimate" in st.session_state:


    estimate = st.session_state["estimate"]


    project = estimate.get(

        "project",

        {}

    )


    st.divider()



    st.success(

        "✅ Construction Estimate Ready"

    )



    # =================================================
    # COST SUMMARY
    # =================================================


    st.header(

        "💰 Cost Summary"

    )



    subtotal = float(

        estimate.get(

            "subtotal",

            0

        )

    )



    vat = float(

        estimate.get(

            "vat",

            0

        )

    )



    grand_total = float(

        estimate.get(

            "grand_total",

            0

        )

    )



    cost1,cost2,cost3 = st.columns(3)



    cost1.metric(

        "Subtotal",

        f"{currency} {subtotal:,.2f}"

    )


    cost2.metric(

        "VAT",

        f"{currency} {vat:,.2f}"

    )


    cost3.metric(

        "Grand Total",

        f"{currency} {grand_total:,.2f}"

    )



    st.divider()



# =====================================================
# GET PROJECT DATA
# =====================================================

estimate = st.session_state.get("estimate", {})

project = estimate.get("project", {})

# =====================================================
# PROJECT INFORMATION
# =====================================================

st.header("🏠 Project Information")

info1, info2 = st.columns(2)

with info1:

    st.write(
        f"**Client:** {st.session_state.get('client_name', '-')}"
    )

    st.write(
        f"**Project:** {st.session_state.get('project_name', '-')}"
    )

    st.write(
        f"**County:** {project.get('County', '-')}"
    )

    st.write(
        f"**Project Type:** {project.get('Project Type', '-')}"
    )

with info2:

    st.write(
        f"**House Type:** {project.get('House Type', '-')}"
    )

    st.write(
        f"**Wall Material:** {project.get('Block Type', '-')}"
    )

    st.write(
        f"**Roof Type:** {project.get('Roof Type', '-')}"
    )

    st.write(
        f"**Bedrooms:** {project.get('Bedrooms', '-')}"
    )

st.divider()

# =====================================================
# BUILDING STATISTICS
# =====================================================

st.header("📐 Building Statistics")



length_value = float(

    project.get(

        "Length",

        0

    )

)


width_value = float(

    project.get(

        "Width",

        0

    )

)


height_value = float(

    project.get(

        "Wall Height",

        3

    )

)



floor_area = (

    length_value *

    width_value

)



wall_area = (

    2 *

    (length_value + width_value)

    *

    height_value

)



if floor_area < 80:

    duration = "30 - 45 Days"


elif floor_area < 150:

    duration = "45 - 75 Days"


elif floor_area < 250:

    duration = "3 - 5 Months"


else:

    duration = "6+ Months"




s1,s2,s3,s4 = st.columns(4)



s1.metric(

    "Floor Area",

    f"{floor_area:.1f} m²"

)



s2.metric(

    "Wall Area",

    f"{wall_area:.1f} m²"

)



s3.metric(

    "Cost / m²",

    f"{currency} {(grand_total/floor_area):,.0f}"

    if floor_area > 0

    else "0"

)



s4.metric(

    "Timeline",

    duration

)



st.divider()




# =====================================================
# BILL OF QUANTITIES
# =====================================================


st.header(

    "📋 Bill of Quantities (BOQ)"

)



boq = estimate.get(

    "boq",

    {}

)



boq_rows = []



if isinstance(boq,dict):


    for section,details in boq.items():


        if isinstance(details,dict):


            for item,value in details.items():


                boq_rows.append({

                    "Section":
                    section,

                    "Item":
                    item,

                    "Value":
                    value

                })



elif isinstance(boq,list):


    boq_rows = boq




if boq_rows:


    boq_df = pd.DataFrame(

        boq_rows

    )


    st.dataframe(

        boq_df,

        use_container_width=True,

        hide_index=True

    )


else:


    st.info(

        "BOQ information unavailable"

    )



st.divider()




# =====================================================
# MATERIAL SUMMARY
# =====================================================

st.header(
    "🧱 Materials Summary"
)


material_rows = []


materials = estimate.get(
    "materials",
    {}
)


def flatten_materials(data, section=""):

    rows = []

    if isinstance(data, dict):

        for key,value in data.items():

            if isinstance(value, dict):

                rows.extend(
                    flatten_materials(
                        value,
                        key
                    )
                )

            else:

                rows.append({

                    "Section": section,

                    "Material": key,

                    "Quantity": value

                })

    return rows



material_rows = flatten_materials(
    materials
)



if material_rows:


    material_df = pd.DataFrame(
        material_rows
    )


    st.dataframe(

        material_df,

        use_container_width=True,

        hide_index=True

    )


else:

    st.info(
        "No materials generated"
    )


st.divider()


# =====================================================
# LABOUR SUMMARY
# =====================================================

st.header(
    "👷 Labour Summary"
)


labour = estimate.get(
    "labour",
    {}
)


labour_rows = []


def flatten_labour(data, section=""):

    rows=[]


    if isinstance(data,dict):

        for key,value in data.items():


            if isinstance(value,dict):

                rows.extend(
                    flatten_labour(
                        value,
                        key
                    )
                )


            else:

                rows.append({

                    "Section": section,

                    "Activity": key,

                    "Cost": round(
                        float(value),
                        2
                    )

                })


    return rows



labour_rows = flatten_labour(
    labour
)



if labour_rows:


    labour_df = pd.DataFrame(
        labour_rows
    )


    st.dataframe(

        labour_df,

        use_container_width=True,

        hide_index=True

    )


else:


    st.info(
        "No labour costing available"
    )


st.divider()


# =====================================================
# AI CONSTRUCTION ASSISTANT
# =====================================================


st.header(

    "🤖 AI Construction Recommendations"

)



try:


    recommendations = get_ai_recommendations(

        project,

        estimate

    )



    if recommendations:


        for recommendation in recommendations:


            st.success(

                recommendation

            )


    else:


        st.info(

            "No recommendations available"

        )



except Exception:


    st.info(

        "AI assistant unavailable"

    )



st.divider()
# =====================================================
# PROJECT HEALTH SCORE
# =====================================================


st.header(
    "🏆 Project Health Score"
)


# GET TOTAL COST SAFELY

grand_total = float(

    estimate.get(

        "grand_total",

        0

    )

)



score = 100


warnings = []



if grand_total > 5000000:


    score -= 10


    warnings.append(

        "Large project budget detected"

    )



if project.get(

    "Roof Type"

) == "Concrete Roof":


    score -= 5


    warnings.append(

        "Concrete roof increases structural load"

    )



if project.get(

    "Block Type"

) == "Coral Blocks":


    score -= 5


    warnings.append(

        "Coral blocks require moisture protection"

    )



# SCORE DISPLAY

st.progress(

    score / 100

)



col1,col2 = st.columns(2)



with col1:

    st.metric(

        "🏆 Project Rating",

        f"{score}/100"

    )



with col2:


    st.metric(

        "💰 Project Cost",

        f"KES {grand_total:,.2f}"

    )



if warnings:


    st.subheader(

        "⚠ Recommendations"

    )


    for warning in warnings:


        st.warning(

            warning

        )


else:


    st.success(

        "Project configuration looks good"

    )


st.divider()



#=====================================================
# PDF EXPORT CENTRE
# =====================================================


st.header(

    "📄 Professional Report Export"

)



if st.button(

    "📄 Generate PDF Quotation",

    type="primary",

    use_container_width=True

):


    with st.spinner(

        "Creating professional quotation..."

    ):


        try:


            filename = "BuildQuoteAI_Quotation.pdf"



            generate_pdf(

                filename=filename,

                estimate=estimate,

                client_name=st.session_state.get(

                    "client_name",

                    "Customer"

                ),

                project_name=st.session_state.get(

                    "project_name",

                    "Construction Project"

                )

            )



            with open(

                filename,

                "rb"

            ) as pdf_file:


                st.download_button(

                    label="⬇ Download PDF Quotation",

                    data=pdf_file,

                    file_name=filename,

                    mime="application/pdf",

                    use_container_width=True

                )



            st.success(

                "PDF quotation generated successfully"

            )



        except Exception as e:


            st.error(

                f"PDF generation failed: {e}"

            )



st.divider()




# =====================================================
# PROJECT SUMMARY CARD
# =====================================================


st.header(

    "📌 Final Project Summary"

)



summary = pd.DataFrame({


    "Property":[


        "Client",

        "Project",

        "County",

        "Project Type",

        "House Type",

        "Wall Material",

        "Roof Type",

        "Bedrooms",

        "Floor Area",

        "Total Cost"

    ],



    "Value":[


        st.session_state.get(

            "client_name",

            "-"

        ),



        st.session_state.get(

            "project_name",

            "-"

        ),



        project.get(

            "County",

            "-"

        ),



        project.get(

            "Project Type",

            "-"

        ),



        project.get(

            "House Type",

            "-"

        ),



        project.get(

            "Block Type",

            "-"

        ),



        project.get(

            "Roof Type",

            "-"

        ),



        project.get(

            "Bedrooms",

            "-"

        ),



        f"{floor_area:.1f} m²",



        f"{currency} {grand_total:,.2f}"

    ]



})



st.dataframe(

    summary,

    use_container_width=True,

    hide_index=True

)



st.divider()




# =====================================================
# SMART CONSTRUCTION TIPS
# =====================================================


st.header(

    "💡 Smart Construction Tips"

)



tips = [


    "Buy materials according to construction phases.",


    "Confirm supplier prices before procurement.",


    "Carry out soil investigation before foundation work.",


    "Maintain 5-10% contingency budget.",


    "Inspect materials during delivery.",


    "Follow Kenya Building Code requirements."



]



for tip in tips:


    st.success(

        tip

    )



st.divider()




# =====================================================
# FOOTER
# =====================================================


st.markdown(

"""

<hr>

""",

unsafe_allow_html=True

)



footer1,footer2,footer3 = st.columns(3)



with footer1:


    st.caption(

        f"🏗 {company_name}"

    )



with footer2:


    st.caption(

        "Professional Construction Estimation Platform"

    )



with footer3:


    st.caption(

        "Version 3.0"

    )



st.caption(

    "© 2026 BuildQuote AI | Developed by Flavian Otieno"

)