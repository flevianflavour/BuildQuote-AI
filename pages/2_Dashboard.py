"""
BuildQuote AI
Executive Dashboard
Version 3.0
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from services.excel_export import export_excel
from services.ai_assistant import get_ai_recommendations
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

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title=f"{company_name} Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CSS
# =====================================================
st.markdown("""
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


/* SIDEBAR */

section[data-testid="stSidebar"]{
    background:#1e293b;
}


section[data-testid="stSidebar"] *{
    color:white;
}


/* KPI CARDS */

div[data-testid="stMetric"]{

    background:rgba(255,255,255,0.08);

    border-radius:15px;

    padding:16px;

    border:1px solid rgba(255,255,255,0.15);

    box-shadow:0 4px 12px rgba(0,0,0,0.20);

}


/* KPI LABEL */

div[data-testid="stMetricLabel"]{

    color:#cbd5e1;

    font-weight:600;

}


/* KPI VALUES */

div[data-testid="stMetricValue"]{

    color:white;

    font-size:28px;

    font-weight:700;

}


/* ALL HEADERS */

h1,h2,h3{

    color:white;

}


/* NORMAL TEXT */

p,span,label{

    color:#e2e8f0;

}


/* TABLES */

[data-testid="stDataFrame"]{

    background:#0f172a;

    border-radius:12px;

}


/* DIVIDERS */

hr{

    border-color:#334155;

}


</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    try:
        st.image("assets/logo.png", width=150)
    except Exception:
        st.title(company_name)

    st.markdown(f"## {company_name}")

    st.caption(
        "Professional Construction Intelligence Platform"
    )

    st.divider()

    st.write("🏗 BOQ Analysis")
    st.write("🧱 Material Tracking")
    st.write("👷 Labour Costing")
    st.write("📊 Cost Dashboard")
    st.write("🤖 AI Insights")

# =====================================================
# CHECK SESSION
# =====================================================

if "estimate" not in st.session_state:

    st.warning("Generate an estimate first.")
    st.stop()

estimate = st.session_state["estimate"]

project = estimate.get("project", {})

client_name = estimate.get(
    "client_name",
    "Customer"
)

project_name = estimate.get(
    "project_name",
    "Construction Project"
)

# =====================================================
# HEADER
# =====================================================

st.title("📊 Executive Construction Dashboard")

st.caption(
    "Professional Project Cost Analysis"
)

st.divider()

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

left, right = st.columns(2)

with left:

    st.write(f"**Client:** {client_name}")
    st.write(f"**Project:** {project_name}")
    st.write(f"**County:** {project.get('County','-')}")
    st.write(f"**Project Type:** {project.get('Project Type','-')}")

with right:

    st.write(f"**House Type:** {project.get('House Type','-')}")
    st.write(f"**Wall Material:** {project.get('Block Type','-')}")
    st.write(f"**Roof Type:** {project.get('Roof Type','-')}")
    st.write(f"**Bedrooms:** {project.get('Bedrooms','-')}")

st.divider()

# =====================================================
# FINANCIAL OVERVIEW
# =====================================================
st.markdown(
"""
<h2 style="color:white;">
💰 Financial Overview
</h2>
""",
unsafe_allow_html=True
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

length = float(
    project.get(
        "Length",
        0
    )
)

width = float(
    project.get(
        "Width",
        0
    )
)

area = length * width

cost_per_m2 = 0

if area > 0:
    cost_per_m2 = grand_total / area

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Subtotal",
    f"{currency} {subtotal:,.0f}"
)

c2.metric(
    "VAT",
    f"{currency} {vat:,.0f}"
)

c3.metric(
    "Grand Total",
    f"{currency} {grand_total:,.0f}"
)

c4.metric(
    "Cost / m²",
    f"{currency} {cost_per_m2:,.0f}"
)

st.divider()# =====================================================
# =====================================================
# BUILDING STATISTICS
# =====================================================

st.markdown(
    """
    <h2 style="color:white;">
    📐 Building Statistics
    </h2>
    """,
    unsafe_allow_html=True
)


wall_height = float(
    project.get(
        "Wall Height",
        3
    )
)


wall_area = (
    2 * (length + width) * wall_height
)


if area < 80:

    duration = "30 - 45 Days"

elif area < 150:

    duration = "45 - 75 Days"

elif area < 250:

    duration = "3 - 5 Months"

else:

    duration = "6+ Months"



s1, s2, s3, s4 = st.columns(4)



s1.metric(
    "📐 Floor Area",
    f"{area:.1f} m²"
)


s2.metric(
    "🧱 Estimated Wall Area",
    f"{wall_area:.1f} m²"
)


s3.metric(
    "💰 Cost / m²",
    f"{currency} {cost_per_m2:,.0f}"
)


s4.metric(
    "⏱ Estimated Duration",
    duration
)


st.divider()
# =====================================================
# COST ANALYSIS
# =====================================================

st.header("📊 Cost Analysis")

fig, ax = plt.subplots(figsize=(8, 4))

labels = [
    "Subtotal",
    "VAT"
]

values = [
    subtotal,
    vat
]

bars = ax.bar(labels, values)

ax.set_ylabel(currency)
ax.set_title("Project Cost Breakdown")

for bar in bars:

    y = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        y,
        f"{y:,.0f}",
        ha="center",
        va="bottom"
    )

st.pyplot(fig)

st.divider()

# =====================================================
# MATERIAL SUMMARY
# =====================================================

st.header("🧱 Material Summary")

material_rows = []

materials = estimate.get("materials", {})

for section_name, section in materials.items():

    if not isinstance(section, dict):
        continue

    for material, qty in section.items():

        if "cost" in material.lower():
            continue

        if "total" in material.lower():
            continue

        material_rows.append({
            "Section": section_name,
            "Material": material.replace("_", " ").title(),
            "Quantity": qty
        })

if material_rows:

    st.dataframe(
        pd.DataFrame(material_rows),
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No material data available.")

# =====================================================
# LABOUR SUMMARY
# =====================================================

st.header("👷 Labour Summary")

labour_rows = []

labour = estimate.get("labour", {})

for section_name, section in labour.items():

    if not isinstance(section, dict):
        continue

    for activity, value in section.items():

        if "cost" in activity.lower():
            continue

        if "total" in activity.lower():
            continue

        labour_rows.append({
            "Section": section_name,
            "Activity": activity.replace("_", " ").title(),
            "Value": value
        })

if labour_rows:

    st.dataframe(
        pd.DataFrame(labour_rows),
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No labour data available.")
# =====================================================
# BILL OF QUANTITIES
# =====================================================

st.header("📋 Bill of Quantities")

boq = estimate.get("boq", [])

if boq:

    st.dataframe(
        pd.DataFrame(boq),
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning("No BOQ available.")# =====================================================
# AI CONSTRUCTION INSIGHTS
# =====================================================

st.header("🤖 AI Construction Insights")

try:

    recommendations = get_ai_recommendations(
        project,
        estimate
    )

    if recommendations:

        for rec in recommendations:
            st.success(rec)

    else:

        county = project.get("County", "")

        if county in ["Mombasa", "Kilifi", "Kwale"]:

            st.info(
                "🌊 Coastal construction detected. Use corrosion-resistant reinforcement, sulphate-resistant cement and quality waterproofing."
            )

        elif county in ["Kiambu", "Nyeri", "Kirinyaga", "Murang'a"]:

            st.info(
                "🌧 High rainfall region. Ensure proper drainage and damp-proof construction."
            )

        elif county in ["Nakuru", "Narok", "Kajiado"]:

            st.info(
                "🪨 Carry out a soil test before foundation construction."
            )

        else:

            st.info(
                "🏗 Always perform a site investigation before construction."
            )

except Exception:

    st.info(
        "AI recommendations are currently unavailable."
    )

st.divider()

# =====================================================
# PROJECT HEALTH SCORE
# =====================================================

st.markdown(
    """
    <h2 style="color:white;">
    🏆 Project Health Score
    </h2>
    """,
    unsafe_allow_html=True
)


score = 100

warnings = []


if grand_total > 5_000_000:

    score -= 10

    warnings.append(
        "High overall project cost."
    )


if project.get("Roof Type") == "Concrete Roof":

    score -= 5

    warnings.append(
        "Concrete roofs require stronger structural support."
    )


if project.get("Block Type") == "Coral Blocks":

    score -= 5

    warnings.append(
        "Coral blocks require additional waterproofing."
    )


county = project.get(
    "County",
    ""
)


if county in [
    "Mombasa",
    "Kilifi",
    "Kwale"
]:

    warnings.append(
        "Coastal climate detected. Use anti-corrosion reinforcement."
    )



# SCORE DISPLAY

st.progress(
    score / 100
)


score1, score2 = st.columns(2)


with score1:

    st.metric(
        "🏆 Project Score",
        f"{score}/100"
    )


with score2:

    if score >= 90:

        st.success(
            "Excellent"
        )

    elif score >= 75:

        st.info(
            "Good"
        )

    else:

        st.warning(
            "Needs Review"
        )



# RECOMMENDATIONS

if warnings:

    st.markdown(
        """
        <h3 style="color:white;">
        ⚠ Recommendations
        </h3>
        """,
        unsafe_allow_html=True
    )


    for item in warnings:

        st.warning(
            item
        )


else:

    st.success(
        "Project configuration looks excellent."
    )


st.divider()

# =====================================================
# PROJECT TIMELINE
# =====================================================

st.header("📅 Estimated Timeline")

t1, t2 = st.columns(2)

t1.metric(
    "Estimated Duration",
    duration
)

t2.metric(
    "Current Stage",
    "Planning"
)

st.divider()

# =====================================================
# SMART CONSTRUCTION TIPS
# =====================================================

st.header("💡 Smart Construction Tips")

tips = [

    "Purchase materials in phases to reduce theft.",

    "Compare supplier quotations before purchasing.",

    "Carry out a soil investigation before excavation.",

    "Keep a contingency budget of 5–10%.",

    "Inspect all materials before accepting delivery.",

    "Follow Kenya Building Code requirements."

]

for tip in tips:

    st.success(tip)

st.divider()

# =====================================================
# EXPORT CENTRE
# =====================================================

st.header("📤 Export Centre")

col1, col2 = st.columns(2)

# -------------------------------------
# EXPORT EXCEL
# -------------------------------------

with col1:

    if st.button(
        "📊 Export Excel",
        use_container_width=True,
        type="primary"
    ):

        try:

            filename = export_excel(
                estimate=estimate,
                client_name=client_name,
                project_name=project_name
            )

            with open(filename, "rb") as excel_file:

                st.download_button(
                    label="⬇ Download Excel Report",
                    data=excel_file,
                    file_name=filename,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )

            st.success(
                "✅ Excel report generated successfully."
            )

        except Exception as e:

            st.error(
                f"Excel export failed: {e}"
            )

# -------------------------------------
# PRINT BOQ
# -------------------------------------

with col2:

    if st.button(
        "🖨 Print BOQ",
        use_container_width=True
    ):

        st.info(
            "Press Ctrl + P (Windows) or Cmd + P (Mac) to print this report."
        )

st.divider()
# =====================================================
# PROJECT SUMMARY
# =====================================================

st.header("📌 Project Summary")

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
        "Estimated Cost"

    ],

    "Value":[

        client_name,
        project_name,
        project.get("County", "-"),
        project.get("Project Type", "-"),
        project.get("House Type", "-"),
        project.get("Block Type", "-"),
        project.get("Roof Type", "-"),
        project.get("Bedrooms", "-"),
        f"{area:.1f} m²",
        f"{currency} {grand_total:,.0f}"

    ]

})

st.dataframe(

    summary,

    use_container_width=True,

    hide_index=True

)

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown(
    "<hr>",
    unsafe_allow_html=True
)

f1, f2, f3 = st.columns(3)

with f1:
    st.caption(f"🏗 {company_name}")

with f2:
    st.caption("Professional Construction Estimation Platform")

with f3:
    st.caption("Version 3.0")

st.caption(
    "© 2026 BuildQuote AI | Developed by Flavian Otieno"
)