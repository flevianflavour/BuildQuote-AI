import streamlit as st

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="BuildQuote AI",
    page_icon="🏗️",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("🏗️ BuildQuote AI")
st.subheader("AI-Powered Construction Estimation Software")

st.markdown(
"""
Generate professional **Bills of Quantities (BOQs)**, quotations and construction
cost estimates for projects across Kenya.

BuildQuote AI helps contractors, engineers, architects and quantity surveyors
prepare accurate construction estimates within minutes.
"""
)

st.divider()

# =====================================================
# FEATURES
# =====================================================

st.header("🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🏠 Foundation Estimation")
    st.success("🧱 Walling Estimation")
    st.success("🏗 Roof Estimation")
    st.success("🚪 Doors & Windows")

with col2:
    st.success("📍 County-Based Pricing")
    st.success("💰 Labour Costing")
    st.success("🧾 VAT Calculation")
    st.success("📑 Professional BOQs")

with col3:
    st.success("📄 PDF Quotations")
    st.success("📊 Dashboard & Reports")
    st.success("🤖 AI Cost Optimization")
    st.success("☁ Future Cloud Database")

st.divider()

# =====================================================
# WORKFLOW
# =====================================================

st.header("📋 How It Works")

st.markdown(
"""
### Step 1
Create a **New Project**.

### Step 2
Enter:

- Client Details
- County
- Building Dimensions
- Wall Material
- Roof Type

### Step 3
BuildQuote AI automatically calculates:

- Foundation
- Walling
- Roofing
- Materials
- Labour
- VAT

### Step 4
Generate:

- Professional BOQ
- PDF Quotation
- Cost Report
"""
)

st.divider()

# =====================================================
# MODULE STATUS
# =====================================================

st.header("🛠 Project Progress")

progress = {
    "Foundation Estimator": "✅ Complete",
    "Walling Estimator": "✅ Complete",
    "Roof Estimator": "🚧 In Progress",
    "Cost Engine": "✅ Complete",
    "PDF Generator": "✅ Complete",
    "Dashboard": "🚧 In Progress",
    "Reports": "🚧 In Progress",
    "AI Assistant": "⏳ Planned",
}

for module, status in progress.items():
    st.write(f"**{module}** — {status}")

st.divider()

# =====================================================
# QUICK START
# =====================================================

st.info(
"""
👈 Select **New Project** from the left sidebar to begin creating
a construction estimate.
"""
)

st.caption("BuildQuote AI • Version 1.0 • Kenyan Construction Estimation Platform")