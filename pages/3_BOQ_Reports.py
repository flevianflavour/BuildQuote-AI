"""
BuildQuote AI

BOQ Reports Dashboard v5

Displays:
• Project Information
• Cost Summary
• Cost Distribution
• Section Totals
• BOQ
• Materials
• Labour
• Statistics
• AI Insights
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="BuildQuote AI Reports",
    page_icon="📄",
    layout="wide"
)


st.title("📄 BuildQuote AI Reports")

st.caption(
    "Professional Construction Cost Report"
)


# =====================================================
# LOAD ESTIMATE
# =====================================================

if "estimate" not in st.session_state:

    st.warning(
        "No estimate available."
    )

    st.stop()


estimate = st.session_state["estimate"]


project = estimate.get(
    "project",
    {}
)


sections = estimate.get(
    "sections",
    {}
)


materials = estimate.get(
    "materials",
    {}
)


labour = estimate.get(
    "labour",
    {}
)


boq = estimate.get(
    "boq",
    []
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


# =====================================================
# PROJECT INFORMATION
# =====================================================

st.header("🏗 Project Information")


col1, col2 = st.columns(2)


with col1:

    st.write(
        f"**County:** {project.get('County','N/A')}"
    )

    st.write(
        f"**House Type:** {project.get('House Type','N/A')}"
    )

    st.write(
        f"**Bedrooms:** {project.get('Bedrooms','N/A')}"
    )

    st.write(
        f"**Wall Material:** {project.get('Wall Material','N/A')}"
    )


with col2:

    st.write(
        f"**Length:** {project.get('Length','N/A')} m"
    )

    st.write(
        f"**Width:** {project.get('Width','N/A')} m"
    )

    st.write(
        f"**Wall Height:** {project.get('Wall Height','N/A')} m"
    )

    st.write(
        f"**Floor Area:** {project.get('Floor Area','N/A')} m²"
    )


st.divider()


# =====================================================
# COST SUMMARY
# =====================================================

st.header("💰 Cost Summary")


material_cost = 0

for section in materials.values():

    if isinstance(section, dict):

        for key,value in section.items():

            if "cost" in key.lower():

                material_cost += float(value)



labour_cost = 0

for section in labour.values():

    if isinstance(section, dict):

        for key,value in section.items():

            if "cost" in key.lower():

                labour_cost += float(value)



# fallback from subtotal

if material_cost == 0 and labour_cost == 0:

    material_cost = subtotal



c1,c2,c3,c4 = st.columns(4)


c1.metric(
    "Materials",
    f"KES {material_cost:,.2f}"
)


c2.metric(
    "Labour",
    f"KES {labour_cost:,.2f}"
)


c3.metric(
    "VAT",
    f"KES {vat:,.2f}"
)


c4.metric(
    "Grand Total",
    f"KES {grand_total:,.2f}"
)


st.divider()


# =====================================================
# COST DISTRIBUTION
# =====================================================

st.header("📊 Cost Distribution")


labels = []

values = []


if material_cost > 0:

    labels.append(
        "Materials"
    )

    values.append(
        material_cost
    )


if labour_cost > 0:

    labels.append(
        "Labour"
    )

    values.append(
        labour_cost
    )


if values:

    fig,ax = plt.subplots(
        figsize=(6,6)
    )


    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )


    st.pyplot(fig)


else:

    st.info(
        "No cost information available."
    )


st.divider()


# =====================================================
# SECTION TOTALS
# =====================================================

st.header("🏗 Section Totals")


section_rows = []


for name,section in sections.items():

    if isinstance(section,dict):

        amount = (

            section.get(
                "subtotal",
                0
            )

            or

            section.get(
                "total",
                0
            )

        )


        section_rows.append({

            "Section":name,

            "Amount (KES)":amount

        })



if section_rows:

    st.dataframe(

        pd.DataFrame(section_rows),

        hide_index=True,

        use_container_width=True

    )


else:

    st.info(
        "No section totals available."
    )



st.divider()


# =====================================================
# BILL OF QUANTITIES
# =====================================================

st.header("📋 Bill of Quantities")


if boq:

    boq_df = pd.DataFrame(boq)


    st.dataframe(

        boq_df,

        hide_index=True,

        use_container_width=True

    )


else:

    st.warning(
        "No BOQ available."
    )


st.divider()


# =====================================================
# MATERIAL REPORT
# =====================================================

st.header("🧱 Material Report")


material_rows=[]


for section,data in materials.items():

    if isinstance(data,dict):

        for item,qty in data.items():

            material_rows.append({

                "Section":section,

                "Material":item,

                "Quantity":qty

            })



if material_rows:

    st.dataframe(

        pd.DataFrame(material_rows),

        hide_index=True,

        use_container_width=True

    )


else:

    st.info(
        "No materials available."
    )


st.divider()


# =====================================================
# LABOUR REPORT
# =====================================================

st.header("👷 Labour Report")


labour_rows=[]


for section,data in labour.items():

    if isinstance(data,dict):

        for activity,value in data.items():

            labour_rows.append({

                "Section":section,

                "Activity":activity,

                "Value":value

            })



if labour_rows:

    st.dataframe(

        pd.DataFrame(labour_rows),

        hide_index=True,

        use_container_width=True

    )


else:

    st.info(
        "No labour information available."
    )


st.divider()


# =====================================================
# PROJECT STATISTICS
# =====================================================

st.header("📐 Project Statistics")


stats=[]


for key,value in project.items():

    if isinstance(value,(int,float)):

        stats.append({

            "Metric":key,

            "Value":value

        })


if stats:

    st.dataframe(

        pd.DataFrame(stats),

        hide_index=True,

        use_container_width=True

    )



st.divider()


# =====================================================
# AI INSIGHTS
# =====================================================

st.header("🤖 BuildQuote AI Insights")


if grand_total < 500000:

    st.success(
        "This project falls within a compact residential construction budget."
    )

elif grand_total < 1000000:

    st.success(
        "This project falls within a medium residential construction budget."
    )

else:

    st.success(
        "This project falls within a high-budget construction category."
    )


st.divider()


# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

st.header("📝 Executive Summary")


st.write(
f"""
This estimate was generated automatically by **BuildQuote AI**.

### Summary

Estimated Material Cost:
KES {material_cost:,.2f}

Estimated Labour Cost:
KES {labour_cost:,.2f}

VAT:
KES {vat:,.2f}

Grand Total:
KES {grand_total:,.2f}

The estimate combines foundation, walling,
mortar, concrete and openings using
construction calculations and project data.
"""
)


st.success(
    f"Estimated Project Cost: KES {grand_total:,.2f}"
)


st.divider()


st.caption(
    "© 2026 BuildQuote AI | Smart Construction Estimation Platform"
)