"""
BuildQuote AI

Main Application Home Page

Professional Landing Dashboard v3.0

Features:
- Dynamic Company Branding
- Logo Support
- Quick Navigation
- AI Construction Platform Overview
- System Monitoring
"""

import streamlit as st

from config.settings_manager import get_company_settings


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(

    page_title="BuildQuote AI",

    page_icon="🏗️",

    layout="wide",

    initial_sidebar_state="expanded"

)



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
    "Smart Construction Estimation Platform"
)


logo = company.get(
    "logo",
    "assets/logo.png"
)


version = company.get(
    "version",
    "3.0"
)


currency = company.get(
    "currency",
    "KES"
)


# =====================================================
# GLOBAL BUILDQUOTE AI DARK THEME CSS
# =====================================================

st.markdown("""
<style>


/* =====================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
===================================================== */

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}



/* =====================================================
   MAIN PAGE BACKGROUND
===================================================== */

.stApp{

    background:#0f172a;

}



.block-container{

    padding-top:1rem;

    padding-bottom:2rem;

}



/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"]{

    background:#020617;

}


section[data-testid="stSidebar"] *{

    color:white !important;

}



/* =====================================================
   GLOBAL TEXT
===================================================== */


h1,
h2,
h3,
h4,
h5,
h6{

    color:white !important;

}


p,
span,
label,
div{

    color:#e2e8f0;

}



/* =====================================================
   KPI METRIC CARDS
===================================================== */


div[data-testid="stMetric"]{


    background:#1e293b;


    border-radius:16px;


    padding:18px;


    border:1px solid #334155;


    box-shadow:
    0 5px 15px rgba(0,0,0,0.35);


}



/* KPI LABEL */

div[data-testid="stMetricLabel"]{

    color:#94a3b8 !important;

    font-weight:600;

}



/* KPI VALUE */

div[data-testid="stMetricValue"]{

    color:white !important;

    font-size:28px;

    font-weight:700;

}



/* KPI DELTA */

div[data-testid="stMetricDelta"]{

    color:#22c55e !important;

}



/* =====================================================
   DASHBOARD CARDS / CONTAINERS
===================================================== */


div[data-testid="stVerticalBlockBorderWrapper"]{


    background:#1e293b;


    border-radius:16px;


    padding:20px;


    border:1px solid #334155;


}



/* =====================================================
   ALERT BOXES
===================================================== */


div[data-testid="stAlert"]{


    background:#1e293b;


    border-radius:12px;


    border:1px solid #334155;


}


div[data-testid="stAlert"] *{

    color:white !important;

}



/* =====================================================
   TABLES
===================================================== */


[data-testid="stDataFrame"]{


    background:#1e293b;


    border-radius:12px;


}



[data-testid="stDataFrame"] *{

    color:white !important;

}



/* =====================================================
   INPUT BOXES
===================================================== */


input,
textarea,
select{


    background:#1e293b !important;


    color:white !important;


}



/* =====================================================
   BUTTONS
===================================================== */


.stButton button{


    background:#2563eb;


    color:white;


    border-radius:12px;


    border:none;


    padding:10px 20px;


    font-weight:600;


}


.stButton button:hover{


    background:#1d4ed8;


}



/* =====================================================
   DIVIDERS
===================================================== */


hr{

    border-color:#334155;

}



/* =====================================================
   FOOTER / CAPTIONS / ICONS
===================================================== */


footer,
footer *,
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] *{


    color:#94a3b8 !important;

}



footer svg{


    fill:#94a3b8 !important;

}
/* REMOVE WHITE BACKGROUND FROM FOOTER MESSAGE */

[data-testid="stMarkdownContainer"]{

    background:transparent !important;

}


/* =====================================================
   SUCCESS / WARNING / INFO
===================================================== */


.stSuccess,
.stInfo,
.stWarning,
.stError{


    border-radius:12px;

}



/* =====================================================
   SCROLL BAR
===================================================== */


::-webkit-scrollbar{

    width:8px;

}


::-webkit-scrollbar-track{

    background:#020617;

}


::-webkit-scrollbar-thumb{

    background:#334155;

    border-radius:10px;

}


</style>
""",
unsafe_allow_html=True)

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

                width=140

            )

        except:

            st.title(
                "🏗️"
            )


    st.markdown(

        f"# {company_name}"

    )


    st.caption(

        tagline

    )


    st.success(

        f"Version {version}"

    )


    st.divider()



    st.markdown(

        "### 🏗 Platform Modules"

    )


    modules = [

        "🏠 Project Builder",

        "⛏ Foundation Estimator",

        "🧱 Walling Calculator",

        "🪨 Mortar Estimator",

        "🏗 Concrete Calculator",

        "🏠 Roofing Engine",

        "🎨 Finishes Estimator",

        "⚡ Electrical",

        "🚰 Plumbing",

        "🚪 Doors & Windows",

        "📄 PDF Quotations",

        "🤖 AI Recommendations"

    ]


    for module in modules:

        st.write(module)



    st.divider()


    st.info(

        "🇰🇪 Designed for Kenyan construction pricing and standards"

    )



# =====================================================
# BUILDQUOTE AI FOOTER MESSAGE
# =====================================================
st.markdown(f"""
<div style="
background:linear-gradient(135deg,#0f172a,#1e3a8a);
padding:40px;
border-radius:18px;
border:1px solid #334155;
text-align:center;
box-shadow:0 10px 25px rgba(0,0,0,0.35);
">

<h1 style="
color:white;
margin-bottom:10px;
">

🏗 {company_name}

</h1>

<h3 style="
color:#bfdbfe;
margin-bottom:20px;
">

Building The Future Of Construction Estimation

</h3>

<p style="
color:#e2e8f0;
font-size:18px;
line-height:1.8;
">

BuildQuote AI combines intelligent BOQ generation,
AI-powered cost estimation,
county-based pricing,
professional PDF & Excel reporting,
and real-time construction analytics
to help engineers, contractors and developers
deliver projects faster and more accurately.

</p>

<p style="
color:#94a3b8;
margin-top:25px;
font-size:15px;
">

© 2026 {company_name} | Powered by BuildQuote AI

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# QUICK ACTIONS
# =====================================================

st.subheader(
    "🚀 Quick Actions"
)


q1,q2,q3,q4 = st.columns(4)


with q1:

    st.button(
        "🏗 New Estimate",
        use_container_width=True
    )


with q2:

    st.button(
        "📊 Dashboard",
        use_container_width=True
    )


with q3:

    st.button(
        "📄 Reports",
        use_container_width=True
    )


with q4:

    st.button(
        "⚙ Settings",
        use_container_width=True
    )



st.divider()# =====================================================
# PLATFORM STATISTICS
# =====================================================

st.header(
    "📊 BuildQuote AI Intelligence Overview"
)


s1,s2,s3 = st.columns(3)

s1.metric(
    "🇰🇪 Counties",
    "47"
)

s2.metric(
    "🏗 Modules",
    "12"
)

s3.metric(
    "🤖 AI Status",
    "ACTIVE"
)

s4,s5,s6 = st.columns(3)

s4.metric(
    "📄 Reports",
    "PDF + Excel"
)

s5.metric(
    "⚡ Version",
    version
)

s6.metric(
    "🎯 Accuracy",
    "95%"
)

# =====================================================
# PLATFORM FEATURES
# =====================================================

st.header(

    "🚀 Platform Capabilities"

)



features = {


"🏠 Project Management":[

    "Client information",

    "County selection",

    "House templates",

    "Building dimensions",

    "Material selection"

],



"🧱 Construction Engine":[

    "Foundation estimation",

    "Wall quantity calculation",

    "Mortar calculation",

    "Concrete volume",

    "Material costing"

],



"⚙ Professional Services":[

    "Doors & Windows",

    "Electrical estimates",

    "Plumbing estimates",

    "Labour costing",

    "Finishes calculation"

],



"🤖 Intelligence & Reports":[

    "AI recommendations",

    "Cost analysis",

    "BOQ generation",

    "PDF quotations",

    "Project dashboard"

]


}



feature_columns = st.columns(4)



for column, (title, items) in zip(

    feature_columns,

    features.items()

):


    with column:


        st.info(

            title

        )


        for item in items:


            st.write(

                "✔ " + item

            )



st.divider()



# =====================================================
# HOW THE SYSTEM WORKS
# =====================================================

st.header(

    "⚙️ How BuildQuote AI Works"

)



step1, step2, step3 = st.columns(3)



with step1:


    st.success(

        "1️⃣ Project Setup"

    )


    st.write(

"""

Capture project information:

• Client details

• County location

• House type

• Building dimensions

• Selected materials

"""

    )



with step2:


    st.success(

        "2️⃣ AI Estimation Engine"

    )


    st.write(

"""

Automatically calculates:

• Foundation quantities

• Walling materials

• Cement & sand

• Labour requirements

• Construction costs

"""

    )



with step3:


    st.success(

        "3️⃣ Professional Reports"

    )


    st.write(

"""

Generate:

• BOQ

• Cost dashboard

• PDF quotation

• AI recommendations

• Project analysis

"""

    )



st.divider()



# =====================================================
# CONSTRUCTION PIPELINE
# =====================================================

st.header(

    "🏗 Construction Intelligence Pipeline"

)



pipeline = [

    "📐 Project Dimensions",

    "⛏ Foundation",

    "🧱 Walling",

    "🪨 Mortar",

    "🏗 Concrete",

    "🚪 Openings",

    "🏠 Roofing",

    "🎨 Finishes",

    "👷 Labour",

    "💰 Cost Engine",

    "🧾 VAT",

    "📄 Professional BOQ"

]



pipeline_text = " ➜ ".join(pipeline)



st.success(

    pipeline_text

)



st.divider()# =====================================================
# AI CONSTRUCTION INTELLIGENCE
# =====================================================

st.header(

    "🤖 AI Construction Assistant"

)


ai1, ai2, ai3 = st.columns(3)



with ai1:


    st.info(

        "🌍 County Intelligence"

    )


    st.write(

"""

Uses Kenyan county information
to improve:

✔ Material pricing

✔ Climate considerations

✔ Construction recommendations

"""

    )



with ai2:


    st.info(

        "📈 Cost Intelligence"

    )


    st.write(

"""

Analyzes:

✔ Project budget

✔ Cost per square metre

✔ Material consumption

✔ Possible savings

"""

    )



with ai3:


    st.info(

        "🏗 Construction Advice"

    )


    st.write(

"""

Provides:

✔ Building tips

✔ Risk warnings

✔ Quality recommendations

✔ Planning guidance

"""

    )



st.divider()



# =====================================================
# SYSTEM STATUS
# =====================================================

st.header(

    "📊 System Status"

)



status1, status2, status3, status4 = st.columns(4)



with status1:


    st.metric(

        "Estimation Engine",

        "🟢 Online"

    )


with status2:


    st.metric(

        "County Database",

        "🟢 Active"

    )


with status3:


    st.metric(

        "PDF Generator",

        "🟢 Ready"

    )


with status4:


    st.metric(

        "AI Module",

        "🟢 Available"

    )



st.divider()



# =====================================================
# CURRENT PROJECT STATUS
# =====================================================

st.header(

    "🏗 Current Project Status"

)



if "estimate" in st.session_state:


    estimate = st.session_state.get(

        "estimate",

        {}

    )


    project = estimate.get(

        "project",

        {}

    )


    st.success(

        "✅ Active construction estimate detected"

    )


    p1,p2,p3 = st.columns(3)



    p1.metric(

        "Project",

        project.get(

            "House Type",

            "Available"

        )

    )


    p2.metric(

        "County",

        project.get(

            "County",

            "-"

        )

    )


    p3.metric(

        "Status",

        "Generated"

    )



else:


    st.warning(

        "No active estimate available"

    )


    st.info(

        "Create a new project to generate BOQ and quotation reports."

    )



st.divider()



# =====================================================
# WHY BUILDQUOTE AI
# =====================================================

st.header(

    "⭐ Why Choose BuildQuote AI?"

)



reasons = [

    "✅ Faster construction cost estimation",

    "✅ Reduces manual BOQ preparation errors",

    "✅ Uses Kenyan construction context",

    "✅ Generates professional quotations",

    "✅ Supports contractors and engineers",

    "✅ Provides AI-powered recommendations"

]



for reason in reasons:


    st.success(

        reason

    )



st.divider()



# =====================================================
# COMPANY INFORMATION
# =====================================================

st.header(

    "🏢 Company Information"

)



info1, info2 = st.columns(2)



with info1:


    st.write(

        f"**Company:** {company_name}"

    )


    st.write(

        f"**Platform:** BuildQuote AI"

    )


    st.write(

        f"**Version:** {version}"

    )



with info2:


    st.write(

        f"**Currency:** {currency}"

    )


    st.write(

        "**Market:** Kenya"

    )


    st.write(

        "**Industry:** Construction Technology"

    )


st.divider()# =====================================================
# SUPPORT & CONTACT
# =====================================================

st.header(

    "📞 Support & Contact"

)


contact1, contact2, contact3 = st.columns(3)



with contact1:

    st.info(

        "🏢 Company"

    )

    st.write(

        company.get(

            "company_name",

            "BuildQuote AI"

        )

    )



with contact2:

    st.info(

        "📱 Contact"

    )

    st.write(

        company.get(

            "phone",

            "Not configured"

        )

    )



with contact3:

    st.info(

        "✉ Email"

    )

    st.write(

        company.get(

            "email",

            "Not configured"

        )

    )



st.divider()



# =====================================================
# FINAL MESSAGE
# =====================================================

st.markdown(f"""
<div style="
background:linear-gradient(135deg,#0f172a,#1e3a8a);
padding:35px;
border-radius:18px;
border:1px solid #334155;
text-align:center;
box-shadow:0 10px 20px rgba(0,0,0,0.35);
">

<h2 style="color:white;">

🏗 {company_name}

</h2>

<p style="
color:#e2e8f0;
font-size:18px;
line-height:1.8;
">

Building the future of construction estimation through
technology, automation and artificial intelligence.

</p>

<p style="
color:#94a3b8;
">

Powered by BuildQuote AI Construction Intelligence Platform

</p>

</div>

""", unsafe_allow_html=True)


# =====================================================
# FOOTER
# =====================================================

st.caption(

f"""

© 2026 {company_name}

|

Version {version}

|

🇰🇪 Kenyan Construction Intelligence Platform

|

Developed by Flavian Otieno

"""

)