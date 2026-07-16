"""
BuildQuote AI

New Estimate
Professional Version 1.1
"""

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from calculator import generate_estimate
from quotation_generator import generate_pdf
from config.counties import COUNTIES


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="BuildQuote AI - New Estimate",
    page_icon="🏗️",
    layout="wide"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:1rem;
}

div[data-testid="stMetric"]{

    background:#f8f9fa;

    border-radius:10px;

    padding:15px;

    border:1px solid #e6e6e6;

}

</style>
""",
unsafe_allow_html=True)



# =====================================================
# HEADER
# =====================================================

st.title("🏗️ New Construction Estimate")

st.caption(
    "Create a professional construction estimate using county-specific pricing."
)

st.divider()



# =====================================================
# CLIENT INFORMATION
# =====================================================

st.header("👤 Client Information")


left,right = st.columns(2)


with left:

    client_name = st.text_input(
        "Client Name",
        placeholder="Enter client name"
    )


with right:

    project_name = st.text_input(
        "Project Name",
        placeholder="Residential House"
    )



# =====================================================
# PROJECT DETAILS
# =====================================================

st.header("🏠 Project Details")


c1,c2,c3 = st.columns(3)


with c1:

    county = st.selectbox(
        "County",
        COUNTIES
    )


with c2:

    project_type = st.selectbox(
        "Project Type",
        [
            "Residential",
            "Commercial"
        ]
    )


with c3:

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
# MATERIALS
# =====================================================

st.header("🧱 Construction Materials")


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
    )



# =====================================================
# DIMENSIONS
# =====================================================

st.header("📐 Building Dimensions")


d1,d2,d3 = st.columns(3)


with d1:

    length = st.number_input(
        "Length (m)",
        min_value=1.0,
        value=10.0
    )


with d2:

    width = st.number_input(
        "Width (m)",
        min_value=1.0,
        value=12.0
    )


with d3:

    wall_height = st.number_input(
        "Wall Height (m)",
        min_value=2.0,
        value=3.0
    )



# =====================================================
# OPENINGS
# =====================================================

st.header("🚪 Openings")


o1,o2 = st.columns(2)


with o1:

    doors = st.number_input(
        "Doors",
        min_value=1,
        value=2
    )


with o2:

    windows = st.number_input(
        "Windows",
        min_value=1,
        value=4
    )



st.divider()



# =====================================================
# PROJECT PREVIEW
# =====================================================

st.header("📋 Project Preview")


p1,p2,p3,p4 = st.columns(4)


p1.metric("County",county)

p2.metric("House",house_type)

p3.metric("Wall",wall_material)

p4.metric("Roof",roof_type)


floor_area = length * width


st.metric(
    "Estimated Floor Area",
    f"{floor_area:.1f} m²"
)



st.divider()



# =====================================================
# GENERATE ESTIMATE
# =====================================================

if st.button(
    "🚀 Generate Professional Estimate",
    use_container_width=True,
    type="primary"
):


    if client_name.strip()=="":
        st.error("Please enter Client Name")
        st.stop()



    if project_name.strip()=="":
        st.error("Please enter Project Name")
        st.stop()



    with st.spinner(
        "BuildQuote AI is calculating..."
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
        "✅ Construction estimate generated successfully."
    )# =====================================================
# DISPLAY RESULTS
# =====================================================


if "estimate" in st.session_state:


    estimate = st.session_state["estimate"]

    project = estimate.get(
        "project",
        {}
    )


    st.divider()


    st.success(
        "✅ Estimate Ready"
    )



    # =====================================================
    # DEBUG (REMOVE AFTER TESTING)
    # =====================================================

    st.write("DEBUG ESTIMATE KEYS")

    st.write(
        list(estimate.keys())
    )



    # =====================================================
    # COST SUMMARY
    # =====================================================

    st.header("💰 Cost Summary")


    subtotal = estimate.get(
        "subtotal",
        estimate.get(
            "material_cost",
            0
        )
    )


    vat = estimate.get(
        "vat",
        subtotal * 0.16
    )


    grand_total = estimate.get(
        "grand_total",
        estimate.get(
            "total_cost",
            subtotal + vat
        )
    )



    c1,c2,c3,c4 = st.columns(4)



    c1.metric(
        "Subtotal",
        f"KES {subtotal:,.2f}"
    )


    c2.metric(
        "VAT (16%)",
        f"KES {vat:,.2f}"
    )


    c3.metric(
        "Grand Total",
        f"KES {grand_total:,.2f}"
    )


    area = (

        project.get(
            "length",
            project.get(
                "Length",
                0
            )
        )

        *

        project.get(
            "width",
            project.get(
                "Width",
                0
            )
        )

    )



    if area > 0:

        cost_m2 = grand_total / area

    else:

        cost_m2 = 0



    c4.metric(
        "Cost / m²",
        f"KES {cost_m2:,.0f}"
    )



    st.divider()



    # =====================================================
    # PROJECT SUMMARY
    # =====================================================

    st.header(
        "📋 Project Summary"
    )



    a,b,c = st.columns(3)



    with a:

        st.info(
f"""
### 👤 Client

{st.session_state.get(
    "client_name",
    "Customer"
)}


### 📌 Project

{st.session_state.get(
    "project_name",
    "Construction Project"
)}

"""
        )



    with b:

        st.info(
f"""
### 📍 County

{project.get(
    "county",
    project.get(
        "County",
        "-"
    )
)}


### 🏠 House Type

{project.get(
    "house_type",
    project.get(
        "House Type",
        "-"
    )
)}


### 🏢 Project Type

{project.get(
    "project_type",
    project.get(
        "Project Type",
        "-"
    )
)}

"""
        )



    with c:

        st.info(
f"""
### 🧱 Wall Material

{project.get(
    "wall_material",
    project.get(
        "Block Type",
        "-"
    )
)}


### 🏗 Roof Type

{project.get(
    "roof_type",
    project.get(
        "Roof Type",
        "-"
    )
)}

"""
        )



    st.divider()



    # =====================================================
    # TABS
    # =====================================================


    tab1,tab2,tab3,tab4,tab5 = st.tabs(

        [
            "📋 BOQ",
            "🧱 Materials",
            "👷 Labour",
            "📈 Analysis",
            "📄 Export"
        ]

    )



    # =====================================================
    # BOQ
    # =====================================================


    with tab1:


        st.subheader(
            "📋 Bill of Quantities"
        )


        boq = estimate.get(
            "boq",
            []
        )



        if boq:


            boq_df = pd.DataFrame(
                boq
            )


            st.dataframe(

                boq_df,

                use_container_width=True,

                hide_index=True

            )


        else:


            st.info(
                "No BOQ generated."
            )



    # =====================================================
    # MATERIALS
    # =====================================================


    with tab2:


        st.subheader(
            "🧱 Material Schedule"
        )


        materials = estimate.get(
            "materials",
            {}
        )


        material_rows=[]


        for key,value in materials.items():


            material_rows.append(

                {

                "Material":

                key.replace("_"," ").title(),


                "Quantity":

                value

                }

            )



        if material_rows:


            st.dataframe(

                pd.DataFrame(material_rows),

                use_container_width=True,

                hide_index=True

            )


        else:

            st.info(
                "No material information available."
            )



    # =====================================================
    # LABOUR
    # =====================================================


    with tab3:


        st.subheader(
            "👷 Labour Schedule"
        )


        labour = estimate.get(
            "labour",
            {}
        )


        labour_rows=[]


        for key,value in labour.items():


            labour_rows.append(

                {

                "Trade":

                key.replace("_"," ").title(),


                "Value":

                value

                }

            )



        if labour_rows:


            st.dataframe(

                pd.DataFrame(labour_rows),

                use_container_width=True,

                hide_index=True

            )


        else:

            st.info(
                "No labour information available."
            )    # =====================================================
    # ANALYSIS
    # =====================================================

    with tab4:

        st.subheader(
            "📈 Project Analysis"
        )


        labels = [

            "Subtotal",

            "VAT"

        ]


        values = [

            subtotal,

            vat

        ]



        fig,ax = plt.subplots(
            figsize=(7,4)
        )


        bars = ax.bar(
            labels,
            values
        )


        ax.set_ylabel(
            "KES"
        )


        ax.set_title(
            "Construction Cost Breakdown"
        )


        for bar in bars:

            height = bar.get_height()


            ax.text(

                bar.get_x()+bar.get_width()/2,

                height,

                f"{height:,.0f}",

                ha="center",

                va="bottom"

            )


        st.pyplot(fig)



        st.metric(

            "Floor Area",

            f"{area:.1f} m²"

        )


        st.metric(

            "Cost Per m²",

            f"KES {cost_m2:,.0f}"

        )




    # =====================================================
    # EXPORT
    # =====================================================


    with tab5:


        st.subheader(
            "📄 Professional Quotation"
        )


        if st.button(

            "📄 Generate PDF",

            use_container_width=True

        ):


            pdf_file = (

                "BuildQuote_Quotation.pdf"

            )


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

                    "⬇ Download PDF",

                    file,

                    file_name=pdf_file,

                    mime="application/pdf",

                    use_container_width=True

                )



        st.info(

            "Professional BOQ reports and quotations generated by BuildQuote AI."

        )



    st.divider()



    # =====================================================
    # AI SUMMARY
    # =====================================================


    st.header(
        "🤖 BuildQuote AI Insights"
    )


    st.success(

        f"Estimated construction cost in "

        f"{project.get('county','selected county')} "

        f"is approximately "

        f"KES {grand_total:,.0f}"

    )


    st.info(

        f"Recommended wall material: "

        f"{project.get('wall_material','N/A')}"

    )


    st.info(

        f"Roofing system: "

        f"{project.get('roof_type','N/A')}"

    )


    st.success(

        "Maintain a contingency budget of 5-10% for unexpected costs."

    )



    # =====================================================
    # PROJECT HEALTH SCORE
    # =====================================================


    st.divider()


    st.header(
        "🏆 Project Health Score"
    )


    score = 100


    warnings = []



    if grand_total > 5000000:


        score -= 10

        warnings.append(
            "Large project budget detected."
        )



    if project.get(
        "roof_type"
    ) == "Concrete Roof":


        score -= 5

        warnings.append(

            "Concrete roofing increases structural requirements."

        )



    if project.get(
        "county"
    ) in [

        "Mombasa",

        "Kilifi",

        "Kwale"

    ]:


        warnings.append(

            "Coastal environment detected. Consider corrosion protection."

        )



    st.progress(
        score / 100
    )


    st.metric(

        "Project Score",

        f"{score}/100"

    )



    if warnings:


        for warning in warnings:

            st.warning(warning)


    else:


        st.success(

            "Excellent project configuration."

        )



    # =====================================================
    # TIMELINE
    # =====================================================


    st.divider()


    st.header(
        "📅 Estimated Timeline"
    )


    if area < 80:

        duration = "30 - 45 Days"


    elif area < 150:

        duration = "45 - 75 Days"


    elif area < 250:

        duration = "3 - 5 Months"


    else:

        duration = "6+ Months"



    t1,t2 = st.columns(2)


    t1.metric(

        "Estimated Duration",

        duration

    )


    t2.metric(

        "Building Area",

        f"{area:.1f} m²"

    )



    # =====================================================
    # SMART TIPS
    # =====================================================


    st.divider()


    st.header(
        "💡 Smart Construction Tips"
    )


    tips = [

        "Purchase materials in phases to reduce losses.",

        "Compare several supplier quotations.",

        "Inspect materials before accepting delivery.",

        "Keep 5-10% contingency budget.",

        "Schedule labour according to milestones.",

        "Follow Kenyan building regulations."

    ]



    for tip in tips:

        st.success(tip)



# =====================================================
# FOOTER
# =====================================================


st.divider()


st.caption(

    "© 2026 BuildQuote AI | Professional Construction Estimation Platform"

)


st.caption(

    "Developed by Flavian Otieno | Version 1.1"

)