import streamlit as st
import matplotlib.pyplot as plt

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="BuildQuote AI Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 BuildQuote AI Dashboard")
st.caption("Professional Construction Estimation Dashboard")

# ==================================================
# CHECK SESSION
# ==================================================

if "estimate" not in st.session_state:
    st.warning("No project estimate found.")
    st.info("Go to **New Project** and generate an estimate first.")
    st.stop()

estimate = st.session_state["estimate"]
project = estimate["project"]

# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.header("🏗 Executive Summary")

left, right = st.columns(2)

with left:
    st.write(f"**County:** {project['County']}")
    st.write(f"**Project Type:** {project['Project Type']}")
    st.write(f"**House Type:** {project['House Type']}")

with right:
    st.write(f"**Wall Material:** {project['Block Type']}")
    st.write(f"**Roof Type:** {project['Roof Type']}")
    st.write(f"**Bedrooms:** {project['Bedrooms']}")

st.divider()

# ==================================================
# COST SUMMARY
# ==================================================

st.header("💰 Cost Summary")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Subtotal",
    f"KES {estimate['subtotal']:,.2f}"
)

c2.metric(
    "VAT",
    f"KES {estimate['vat']:,.2f}"
)

c3.metric(
    "Grand Total",
    f"KES {estimate['grand_total']:,.2f}"
)

st.divider()

# ==================================================
# PROJECT VALUE ANALYSIS
# ==================================================

st.header("📐 Building Statistics")

length = project["Length"]
width = project["Width"]

area = length * width

cost_per_m2 = estimate["grand_total"] / area if area else 0

a, b = st.columns(2)

a.metric(
    "Floor Area",
    f"{area:.2f} m²"
)

b.metric(
    "Cost per m²",
    f"KES {cost_per_m2:,.2f}"
)

st.divider()

# ==================================================
# COST BREAKDOWN
# ==================================================

st.header("📊 Cost Breakdown")

labels = ["Subtotal", "VAT"]

values = [
    estimate["subtotal"],
    estimate["vat"]
]

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(labels, values)

ax.set_ylabel("KES")
ax.set_title("Project Cost Summary")

st.pyplot(fig)

st.divider()

# ==================================================
# MATERIAL SUMMARY
# ==================================================

st.header("🧱 Materials")

st.json(estimate["materials"])

st.divider()

# ==================================================
# LABOUR SUMMARY
# ==================================================

st.header("👷 Labour")

st.json(estimate["labour"])

st.divider()

# ==================================================
# BOQ
# ==================================================

st.header("📋 Bill of Quantities")

st.dataframe(
    estimate["boq"],
    use_container_width=True
)

st.divider()

# ==================================================
# MODULE STATUS
# ==================================================

st.header("🛠 Module Status")

modules = {
    "Foundation": True,
    "Walling": True,
    "Roof": True,
    "Finishes": True,
    "Electrical": True,
    "Plumbing": True,
    "Doors & Windows": True
}

for module, status in modules.items():
    st.checkbox(module, value=status, disabled=True)

st.divider()

# ==================================================
# AI RECOMMENDATIONS
# ==================================================

from services.ai_assistant import get_ai_recommendations

st.header("🤖 BuildQuote AI Recommendations")

recommendations = get_ai_recommendations(
    estimate["project"],
    estimate
)

for item in recommendations:
    st.success(item)

# ==================================================
# EXPORT CENTRE
# ==================================================

st.header("📄 Export Centre")

st.info(
    "Generate a quotation from the New Project page."
)

st.caption(
    "© 2026 BuildQuote AI | Version 1.0"
)