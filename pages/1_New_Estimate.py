"""
BuildQuote AI

New Estimate
Professional Version 1.1
"""

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
""", unsafe_allow_html=True)

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

left, right = st.columns(2)

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
# PROJECT CONFIGURATION
# =====================================================

st.header("🏠 Project Details")

c1, c2, c3 = st.columns(3)

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

m1, m2 = st.columns(2)

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

d1, d2, d3 = st.columns(3)

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

o1, o2 = st.columns(2)

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

p1, p2, p3, p4 = st.columns(4)

p1.metric("County", county)
p2.metric("House", house_type)
p3.metric("Wall", wall_material)
p4.metric("Roof", roof_type)

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

    # Validation

    if client_name.strip() == "":
        st.error("Please enter the Client Name.")
        st.stop()

    if project_name.strip() == "":
        st.error("Please enter the Project Name.")
        st.stop()

    with st.spinner("BuildQuote AI is calculating the estimate..."):

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

    st.success("✅ Construction estimate generated successfully.")

# =====================================================
# DISPLAY RESULTS
# =====================================================# =====================================================
# DISPLAY RESULTS
# =====================================================

if "estimate" in st.session_state:

    estimate = st.session_state["estimate"]
    project = estimate["project"]

    st.divider()

    st.success("✅ Estimate Ready")

    # =====================================================
    # COST SUMMARY
    # =====================================================

    st.header("💰 Cost Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Subtotal",
        f"KES {estimate['subtotal']:,.2f}"
    )

    c2.metric(
        "VAT (16%)",
        f"KES {estimate['vat']:,.2f}"
    )

    c3.metric(
        "Grand Total",
        f"KES {estimate['grand_total']:,.2f}"
    )

    area = project["Length"] * project["Width"]

    c4.metric(
        "Cost / m²",
        f"KES {estimate['grand_total']/area:,.0f}"
    )

    st.divider()

    # =====================================================
    # PROJECT SUMMARY
    # =====================================================

    st.header("📋 Project Summary")

    a, b, c = st.columns(3)

    with a:

        st.info(f"""
**Client**

{st.session_state['client_name']}

**Project**

{st.session_state['project_name']}
""")

    with b:

        st.info(f"""
**County**

{project['County']}

**Project Type**

{project['Project Type']}

**House**

{project['House Type']}
""")

    with c:

        st.info(f"""
**Wall**

{project['Block Type']}

**Roof**

{project['Roof Type']}
""")

    st.divider()

    # =====================================================
    # TABS
    # =====================================================

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
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

        st.subheader("Bill of Quantities")

        st.dataframe(
            estimate["boq"],
            use_container_width=True,
            hide_index=True
        )

    # =====================================================
    # MATERIALS
    # =====================================================

    with tab2:

        st.subheader("Material Schedule")

        materials = estimate["materials"]

        material_table = []

        for key, value in materials.items():

            material_table.append(
                {
                    "Material": key.replace("_", " ").title(),
                    "Quantity": value
                }
            )

        st.table(material_table)

    # =====================================================
    # LABOUR
    # =====================================================

    with tab3:

        st.subheader("Labour Schedule")

        labour = estimate["labour"]

        labour_table = []

        for key, value in labour.items():

            labour_table.append(
                {
                    "Trade": key.replace("_", " ").title(),
                    "Value": value
                }
            )

        st.table(labour_table)

    # =====================================================
    # ANALYSIS
    # =====================================================

    with tab4:

        st.subheader("Project Analysis")

        import matplotlib.pyplot as plt

        labels = [
            "Subtotal",
            "VAT"
        ]

        values = [
            estimate["subtotal"],
            estimate["vat"]
        ]

        fig, ax = plt.subplots(figsize=(7,4))

        bars = ax.bar(
            labels,
            values
        )

        ax.set_ylabel("KES")
        ax.set_title("Cost Breakdown")

        for bar in bars:

            height = bar.get_height()

            ax.text(
                bar.get_x() + bar.get_width()/2,
                height,
                f"{height:,.0f}",
                ha="center",
                va="bottom"
            )

        st.pyplot(fig)

        st.metric(
            "Estimated Floor Area",
            f"{area:.1f} m²"
        )

        st.metric(
            "Estimated Cost per m²",
            f"KES {estimate['grand_total']/area:,.2f}"
        )

    # =====================================================
    # EXPORT
    # =====================================================

    with tab5:

        st.subheader("Quotation")

        if st.button(
            "📄 Generate Professional PDF",
            use_container_width=True
        ):

            pdf_file = "BuildQuote_Quotation.pdf"

            generate_pdf(

                filename=pdf_file,

                estimate=estimate,

                client_name=st.session_state["client_name"],

                project_name=st.session_state["project_name"]

            )

            with open(pdf_file, "rb") as file:

                st.download_button(

                    "⬇ Download PDF",

                    file,

                    file_name=pdf_file,

                    mime="application/pdf",

                    use_container_width=True

                )

        st.info(
            "Excel export and BOQ printing will be available in Version 2."
        )

    st.divider()

    # =====================================================
    # AI SUMMARY
    # =====================================================

    st.header("🤖 BuildQuote AI Insights")

    st.success(
        f"Estimated construction cost in {project['County']} is "
        f"approximately KES {estimate['grand_total']:,.0f}."
    )

    st.info(
        f"Recommended wall material: {project['Block Type']}."
    )

    st.info(
        f"Selected roofing system: {project['Roof Type']}."
    )

    st.success(
        "Always allow a contingency budget of 5–10% for unexpected costs."
    )# =====================================================
# PROJECT HEALTH SCORE
# =====================================================

st.divider()

st.header("🏆 Project Health Score")

score = 100

warnings = []

if estimate["grand_total"] > 5000000:
    score -= 10
    warnings.append("High project budget.")

if project["Roof Type"] == "Concrete Roof":
    score -= 5
    warnings.append("Concrete roofing increases structural load.")

if project["Block Type"] == "Coral Blocks":
    score -= 5
    warnings.append("Coral blocks require proper moisture protection.")

if project["County"] in ["Mombasa", "Kilifi", "Kwale"]:

    warnings.append(
        "Coastal environment detected."
    )

st.progress(score/100)

st.metric(
    "Overall Project Score",
    f"{score}/100"
)

if len(warnings) == 0:

    st.success(
        "Excellent project configuration."
    )

else:

    for item in warnings:

        st.warning(item)

# =====================================================
# PROJECT TIMELINE
# =====================================================

st.divider()

st.header("📅 Estimated Timeline")

area = project["Length"] * project["Width"]

if area < 80:

    duration = "30 - 45 Days"

elif area < 150:

    duration = "45 - 75 Days"

elif area < 250:

    duration = "3 - 5 Months"

else:

    duration = "6+ Months"

t1, t2 = st.columns(2)

t1.metric(
    "Estimated Duration",
    duration
)

t2.metric(
    "Floor Area",
    f"{area:.1f} m²"
)

# =====================================================
# MATERIAL DISTRIBUTION
# =====================================================

st.divider()

st.header("📊 Material Distribution")

import matplotlib.pyplot as plt

materials = estimate["materials"]

labels = []
values = []

for k, v in materials.items():

    if isinstance(v, (int, float)):

        labels.append(k.replace("_", " ").title())

        values.append(v)

if len(values) > 0:

    fig, ax = plt.subplots(figsize=(7,5))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title(
        "Material Distribution"
    )

    st.pyplot(fig)

# =====================================================
# SMART CONSTRUCTION TIPS
# =====================================================

st.divider()

st.header("💡 Smart Construction Tips")

tips = [

    "Purchase materials in phases to reduce storage losses.",

    "Compare supplier quotations before procurement.",

    "Inspect materials upon delivery.",

    "Allow a contingency budget of 5–10%.",

    "Hire qualified artisans for structural work.",

    "Follow Kenyan Building Code requirements."

]

for tip in tips:

    st.success(tip)

# =====================================================
# NEXT STEPS
# =====================================================

st.divider()

st.header("🚀 Next Steps")

step1, step2, step3 = st.columns(3)

with step1:

    st.info(
        """
### 1

Review the BOQ

Verify quantities before procurement.
"""
    )

with step2:

    st.info(
        """
### 2

Download PDF

Generate a professional quotation.
"""
    )

with step3:

    st.info(
        """
### 3

Start Construction

Begin procurement and scheduling.
"""
    )

# =====================================================
# BUILDQUOTE QUALITY BADGE
# =====================================================

st.divider()

st.success(
    "✔ Estimate Generated Successfully using BuildQuote AI Professional Estimation Engine"
)

st.caption(
    "© 2026 BuildQuote AI • Developed by Flavian Otieno • Version 1.1"
)