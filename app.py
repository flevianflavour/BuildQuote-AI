"""
BuildQuote AI

Main Application Home Page

Dynamic Version:
- Company Branding
- Logo
- Features
- Platform Overview
"""


import streamlit as st

from config.settings_manager import get_company_settings



# =====================================================
# LOAD COMPANY SETTINGS
# =====================================================


company = get_company_settings()


company_name = company.get(
    "company_name",
    "BuildQuote AI"
)


tagline = company.get(

    "tagline",

    "Professional Construction Estimation Platform"

)


logo = company.get(

    "logo",

    "assets/logo.png"

)



# =====================================================
# PAGE CONFIGURATION
# =====================================================


st.set_page_config(

    page_title=company_name,

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

#MainMenu {visibility:hidden;}

footer {visibility:hidden;}

header {visibility:hidden;}


.block-container{

    padding-top:1rem;

    padding-bottom:1rem;

}


section[data-testid="stSidebar"]{

    background-color:#f5f7fa;

}



div[data-testid="stMetric"]{

    background:#f8f9fa;

    padding:15px;

    border-radius:10px;

    border:1px solid #e6e6e6;

}


</style>

""",

unsafe_allow_html=True

)



# =====================================================
# SIDEBAR
# =====================================================


with st.sidebar:



    if company.get(
        "show_logo",
        True
    ):


        try:

            st.image(
                logo,
                width=150
            )

        except:

            st.title(
                "🏗️ " + company_name
            )



    st.markdown(

        f"## {company_name}"

    )


    st.caption(

        tagline

    )


    st.success(

        "Version 1.2"

    )


    st.divider()



    st.markdown(

        "### Platform Features"

    )



    features = [

        "✅ Bills of Quantities (BOQ)",

        "✅ County-Based Pricing",

        "✅ Material Estimation",

        "✅ Labour Costing",

        "✅ VAT Calculation",

        "✅ PDF Quotations",

        "✅ Interactive Dashboard",

        "✅ AI Recommendations"

    ]



    for feature in features:

        st.write(feature)



    st.divider()



    st.info(

        "🇰🇪 Designed for the Kenyan Construction Industry."

    )



# =====================================================
# HERO SECTION
# =====================================================


st.title(

    f"🏗️ {company_name}"

)


st.subheader(

    tagline

)



st.write(

f"""

{company_name} enables contractors, engineers,
architects and quantity surveyors to generate
professional construction estimates, Bills of Quantities
(BOQs), cost reports and quotations using intelligent
county-based pricing.

"""

)



st.divider()



# =====================================================
# QUICK METRICS
# =====================================================


m1, m2, m3, m4 = st.columns(4)



m1.metric(

    "Supported Counties",

    "47"

)


m2.metric(

    "Estimate Time",

    "< 1 min"

)


m3.metric(

    "Construction Modules",

    "7"

)


m4.metric(

    "Quotation Format",

    "PDF"

)



st.divider()



# =====================================================
# MAIN FEATURES
# =====================================================


st.header(

    "🚀 Core Features"

)



c1,c2,c3 = st.columns(3)



with c1:


    st.success(
        "🏠 Residential Projects"
    )

    st.success(
        "🏢 Commercial Projects"
    )

    st.success(
        "📍 County-Specific Pricing"
    )

    st.success(
        "📐 Building Dimension Analysis"
    )



with c2:


    st.success(
        "🧱 Material Quantification"
    )

    st.success(
        "👷 Labour Estimation"
    )

    st.success(
        "🧾 VAT Calculation"
    )

    st.success(
        "💰 Cost Breakdown"
    )



with c3:


    st.success(
        "📄 Professional BOQs"
    )

    st.success(
        "📑 PDF Quotations"
    )

    st.success(
        "📊 Executive Dashboard"
    )

    st.success(
        "🤖 AI Construction Insights"
    )



st.divider()



# =====================================================
# WORKFLOW
# =====================================================


st.header(

    "⚙️ Simple Workflow"

)



step1,step2,step3 = st.columns(3)



with step1:


    st.info(
        "1️⃣ Create New Estimate"
    )


    st.markdown(
"""
- Client Information
- Project Location
- County Selection
- Building Dimensions
- House Type
"""
    )



with step2:


    st.info(
        "2️⃣ Automatic Estimation"
    )


    st.markdown(
"""
Calculates:

- Foundation
- Walling
- Roofing
- Finishes
- Electrical
- Plumbing
- Labour
- VAT
"""
    )



with step3:


    st.info(
        "3️⃣ Generate Reports"
    )


    st.markdown(
"""
Export:

- Bill of Quantities
- Cost Summary
- Dashboard
- PDF Quotation
"""
    )



st.divider()



# =====================================================
# WHY CHOOSE
# =====================================================


st.header(

    "⭐ Why Choose " + company_name + "?"

)



left,right = st.columns(2)



with left:


    st.markdown(
"""
### Benefits

- Accurate quantity estimation

- Faster project costing

- County-based pricing

- Professional BOQs

- Automated VAT calculations

- AI-powered recommendations

- Easy PDF quotation generation
"""
    )



with right:


    st.markdown(
"""
### Ideal For

✔ Quantity Surveyors

✔ Civil Engineers

✔ Building Contractors

✔ Architects

✔ Developers

✔ Construction Firms

✔ Students & Researchers
"""
    )



st.divider()



# =====================================================
# CAPABILITIES
# =====================================================


st.header(

    "📌 Current Capabilities"

)



cap1,cap2 = st.columns(2)



with cap1:


    st.write(
        "✔ Foundation Estimation"
    )

    st.write(
        "✔ Walling Estimation"
    )

    st.write(
        "✔ Roofing Estimation"
    )

    st.write(
        "✔ Doors & Windows"
    )



with cap2:


    st.write(
        "✔ Labour Costing"
    )

    st.write(
        "✔ Material Costing"
    )

    st.write(
        "✔ AI Recommendations"
    )

    st.write(
        "✔ Professional Reports"
    )



st.divider()



# =====================================================
# START
# =====================================================


st.success(

f"""

👈 Select **New Estimate** from the left navigation menu
to begin creating your construction estimate.

"""

)



st.info(

"""

After generating an estimate, you can:


• View the Dashboard

• Review the BOQ

• Analyze Costs

• Download Professional PDF Quotations

• Receive Intelligent Construction Recommendations


"""

)



st.divider()



st.caption(

f"""

© 2026 {company_name}

| Version 1.2 Presentation Edition

| Developed by Flavian Otieno

"""

)