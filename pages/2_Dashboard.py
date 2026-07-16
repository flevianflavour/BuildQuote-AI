"""
BuildQuote AI

Executive Construction Dashboard

Features:
- Project Summary
- Cost Analysis
- BOQ Review
- Material Analysis
- Labour Analysis
- AI Recommendations
- Project Health
"""


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


from services.ai_assistant import get_ai_recommendations
from config.settings_manager import get_company_settings



# ==================================================
# LOAD SETTINGS
# ==================================================

company = get_company_settings()


company_name = company.get(
    "company_name",
    "BuildQuote AI"
)


currency = company.get(
    "currency",
    "KES"
)



# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(

    page_title=f"{company_name} Dashboard",

    page_icon="📊",

    layout="wide",

    initial_sidebar_state="expanded"

)



# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
"""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}


.block-container{
padding-top:1rem;
padding-bottom:1rem;
}


div[data-testid="stMetric"]{

background:#f8f9fa;

padding:15px;

border-radius:12px;

border:1px solid #e5e5e5;

}

</style>

""",
unsafe_allow_html=True
)



# ==================================================
# SIDEBAR BRANDING
# ==================================================

with st.sidebar:


    if company.get(
        "show_logo",
        True
    ):

        try:

            st.image(
                company.get(
                    "logo",
                    "assets/logo.png"
                ),
                width=140
            )

        except:

            st.title(
                "🏗️ " + company_name
            )


    st.markdown(

        f"## {company_name}"

    )


    st.caption(

        "Construction Intelligence Dashboard"

    )


    st.divider()



    st.write(
        "✅ BOQ Analysis"
    )

    st.write(
        "✅ Material Tracking"
    )

    st.write(
        "✅ Labour Costing"
    )

    st.write(
        "✅ AI Recommendations"
    )



# ==================================================
# CHECK SESSION
# ==================================================

if "estimate" not in st.session_state:


    st.warning(
        "No project estimate found."
    )


    st.info(

        "Please create a New Project before opening the Dashboard."

    )


    st.stop()



estimate = st.session_state["estimate"]


project = estimate.get(
    "project",
    {}
)



client_name = st.session_state.get(

    "client_name",

    "Customer"

)



project_name = st.session_state.get(

    "project_name",

    "Construction Project"

)



# ==================================================
# HEADER
# ==================================================

st.title(

    f"📊 {company_name} Dashboard"

)


st.caption(

    "Professional Construction Estimation Dashboard"

)


st.divider()



# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.header(

    "🏗 Executive Summary"

)



left,right = st.columns(2)



with left:


    st.write(

        f"**👤 Client:** {client_name}"

    )


    st.write(

        f"**📌 Project:** {project_name}"

    )


    st.write(

        f"**📍 County:** {project.get('County','')}"

    )


    st.write(

        f"**🏠 Type:** {project.get('Project Type','')}"

    )



with right:


    st.write(

        f"**🏡 House:** {project.get('House Type','')}"

    )


    st.write(

        f"**🧱 Wall:** {project.get('Block Type','')}"

    )


    st.write(

        f"**🏗 Roof:** {project.get('Roof Type','')}"

    )


    st.write(

        f"**🛏 Bedrooms:** {project.get('Bedrooms','')}"

    )



st.divider()



# ==================================================
# FINANCIAL OVERVIEW
# ==================================================

st.header(

    "💰 Financial Overview"

)



k1,k2,k3,k4 = st.columns(4)



subtotal = estimate.get(
    "subtotal",
    0
)


vat = estimate.get(
    "vat",
    0
)


grand_total = estimate.get(
    "grand_total",
    0
)



k1.metric(

    "Subtotal",

    f"{currency} {subtotal:,.0f}"

)



k2.metric(

    "VAT",

    f"{currency} {vat:,.0f}"

)



k3.metric(

    "Grand Total",

    f"{currency} {grand_total:,.0f}"

)



area = (

    project.get(
        "Length",
        0
    )

    *

    project.get(
        "Width",
        0
    )

)



cost_per_m2 = 0


if area > 0:

    cost_per_m2 = grand_total / area



k4.metric(

    "Cost / m²",

    f"{currency} {cost_per_m2:,.0f}"

)



st.divider()



# ==================================================
# BUILDING STATISTICS
# ==================================================

st.header(

    "📐 Building Statistics"

)



wall_area = (

    project.get(
        "Length",
        0
    )

    *

    2

    +

    project.get(
        "Width",
        0
    )

    *

    2

)



wall_area *= project.get(

    "Wall Height",

    3

)



b1,b2,b3,b4 = st.columns(4)



b1.metric(

    "Floor Area",

    f"{area:.1f} m²"

)



b2.metric(

    "Wall Area",

    f"{wall_area:.1f} m²"

)



b3.metric(

    "Cost / m²",

    f"{currency} {cost_per_m2:,.0f}"

)



if area < 80:

    duration="30-45 Days"

elif area <150:

    duration="45-75 Days"

elif area <250:

    duration="3-5 Months"

else:

    duration="6+ Months"



b4.metric(

    "Duration",

    duration

)



st.divider()



# ==================================================
# COST GRAPH
# ==================================================

st.header(

    "📊 Cost Analysis"

)



labels=[

    "Subtotal",

    "VAT"

]


values=[

    subtotal,

    vat

]



fig,ax = plt.subplots(

    figsize=(8,4)

)



ax.bar(

    labels,

    values

)



ax.set_ylabel(

    currency

)


ax.set_title(

    "Project Cost Breakdown"

)



st.pyplot(fig)



st.divider()



# ==================================================
# MATERIALS
# ==================================================

st.header(

    "🧱 Material Summary"

)



material_rows=[]



for section,values in estimate.get(
    "materials",
    {}
).items():


    if isinstance(values,dict):


        for material,qty in values.items():

            material_rows.append(

                {

                "Section":section,

                "Material":material,

                "Quantity":qty

                }

            )



if material_rows:


    st.dataframe(

        pd.DataFrame(material_rows),

        use_container_width=True

    )


else:

    st.info(

        "No material breakdown available."

    )



st.divider()



# ==================================================
# BOQ
# ==================================================

st.header(

    "📋 Bill of Quantities"

)



boq = estimate.get(

    "boq",

    []

)



if boq:


    st.dataframe(

        pd.DataFrame(boq),

        use_container_width=True

    )


else:

    st.info(

        "No BOQ generated."

    )



st.divider()



# ==================================================
# AI INSIGHTS
# ==================================================

st.header(

    "🤖 AI Construction Insights"

)



recommendations = get_ai_recommendations(

    project,

    estimate

)



for rec in recommendations:

    st.success(rec)



st.divider()



# ==================================================
# EXPORT
# ==================================================

st.header(

    "📄 Export Centre"

)



e1,e2,e3 = st.columns(3)



with e1:

    st.button(

        "📄 Download PDF",

        use_container_width=True

    )


with e2:

    st.button(

        "📊 Export Excel",

        use_container_width=True

    )


with e3:

    st.button(

        "🖨 Print BOQ",

        use_container_width=True

    )



st.divider()



st.caption(

    f"© 2026 {company_name} | Construction Intelligence Platform"

)


st.caption(

    "Developed by Flavian Otieno"

)