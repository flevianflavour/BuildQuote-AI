"""
BuildQuote AI

New Project Page

Allows users to select:
- County
- Project Type
- House Type
- Roof Type
- Wall Material
- Building Dimensions

Then generates:
- BOQ
- Materials
- Labour
- VAT
- Total Estimate
- PDF Quotation
"""

import streamlit as st

from calculator import generate_estimate

from quotation_generator import generate_pdf

from config.counties import COUNTIES



# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="BuildQuote AI - New Project",
    page_icon="🏗️",
    layout="wide"
)


st.title("🏗️ BuildQuote AI - New Project")


st.write(
    "Create a construction estimate by entering project details below."
)



# ==================================================
# CLIENT DETAILS
# ==================================================

st.subheader("👤 Client Information")


client_name = st.text_input(
    "Client Name"
)


project_name = st.text_input(
    "Project Name"
)



# ==================================================
# PROJECT DETAILS
# ==================================================

st.subheader("🏠 Project Configuration")


col1, col2, col3 = st.columns(3)


with col1:

    county = st.selectbox(
        "County",
        COUNTIES
    )


with col2:

    project_type = st.selectbox(
        "Project Type",
        [
            "Residential",
            "Commercial"
        ]
    )


with col3:

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



# ==================================================
# MATERIAL SELECTION
# ==================================================

st.subheader("🧱 Construction Materials")


col4, col5 = st.columns(2)


with col4:

    wall_material = st.selectbox(
        "Wall Material",
        [
            "Machine Cut Stone",
            "Concrete Blocks",
            "Clay Bricks",
            "Coral Blocks"
        ]
    )


with col5:

    roof_type = st.selectbox(
        "Roof Type",
        [
            "Mabati",
            "Tile Roof",
            "Decra Roof",
            "Concrete Roof"
        ]
    )



# ==================================================
# BUILDING DIMENSIONS
# ==================================================

st.subheader("📐 Building Dimensions")


col6, col7, col8 = st.columns(3)


with col6:

    length = st.number_input(
        "Length (Metres)",
        min_value=1.0,
        value=10.0
    )


with col7:

    width = st.number_input(
        "Width (Metres)",
        min_value=1.0,
        value=12.0
    )


with col8:

    wall_height = st.number_input(
        "Wall Height (Metres)",
        min_value=1.0,
        value=3.0
    )



# ==================================================
# OPENINGS
# ==================================================

st.subheader("🚪 Openings")


col9, col10 = st.columns(2)


with col9:

    doors = st.number_input(
        "Number of Doors",
        min_value=1,
        value=2
    )


with col10:

    windows = st.number_input(
        "Number of Windows",
        min_value=1,
        value=4
    )



# ==================================================
# GENERATE ESTIMATE
# ==================================================

if st.button(
    "🚀 Generate Estimate",
    use_container_width=True
):


    estimate = generate_estimate(

        county=county,

        project_type=project_type,

        house_type=house_type,

        length=length,

        width=width,

        wall_height=wall_height,

        block_type=wall_material,

        roof_type=roof_type,

        doors=doors,

        windows=windows

    )


    st.session_state["estimate"] = estimate

    st.session_state["client_name"] = client_name

    st.session_state["project_name"] = project_name


    st.success(
        "Estimate Generated Successfully!"
    )



# ==================================================
# DISPLAY RESULTS
# ==================================================

if "estimate" in st.session_state:


    estimate = st.session_state["estimate"]


    st.divider()


    st.subheader("📊 Project Summary")


    project = estimate["project"]


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "House Type",
            project["House Type"]
        )


    with col2:

        st.metric(
            "Roof",
            project["Roof Type"]
        )


    with col3:

        st.metric(
            "Subtotal",
            f"KES {estimate['subtotal']:,.2f}"
        )


    with col4:

        st.metric(
            "Grand Total",
            f"KES {estimate['grand_total']:,.2f}"
        )



    # ==============================================
    # BOQ TABLE
    # ==============================================

    st.subheader("📋 Bill of Quantities")


    st.dataframe(

        estimate["boq"],

        use_container_width=True

    )



    # ==============================================
    # MATERIALS
    # ==============================================

    st.subheader("🧱 Materials")


    st.json(

        estimate["materials"]

    )



    # ==============================================
    # LABOUR
    # ==============================================

    st.subheader("👷 Labour")


    st.json(

        estimate["labour"]

    )



    # ==============================================
    # PDF QUOTATION
    # ==============================================

    st.divider()


    st.subheader("📄 Generate Quotation")


    if st.button(
        "📄 Create PDF Quotation",
        use_container_width=True
    ):


        pdf_file = "BuildQuote_Quotation.pdf"



        generate_pdf(

            filename=pdf_file,

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
            pdf_file,
            "rb"
        ) as file:


            st.download_button(

                label="⬇️ Download Quotation PDF",

                data=file,

                file_name=pdf_file,

                mime="application/pdf"

            )