import streamlit as st

from config.company_profile import COMPANY_PROFILE

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ BuildQuote AI Settings")
st.caption("Configure company information used in quotations and reports.")

st.divider()

# ==================================================
# INITIALIZE SESSION SETTINGS
# ==================================================

if "company_profile" not in st.session_state:

    st.session_state.company_profile = COMPANY_PROFILE.copy()

profile = st.session_state.company_profile

# ==================================================
# COMPANY INFORMATION
# ==================================================

st.header("🏢 Company Information")

company_name = st.text_input(
    "Company Name",
    value=profile["company_name"]
)

tagline = st.text_input(
    "Company Tagline",
    value=profile["tagline"]
)

contractor = st.text_input(
    "Contractor Name",
    value=profile["contractor"]
)

registration = st.text_input(
    "Registration",
    value=profile["registration"]
)

st.divider()

# ==================================================
# CONTACT INFORMATION
# ==================================================

st.header("📞 Contact Information")

phone = st.text_input(
    "Phone",
    value=profile["phone"]
)

email = st.text_input(
    "Email",
    value=profile["email"]
)

location = st.text_input(
    "Location",
    value=profile["location"]
)

st.divider()

# ==================================================
# ESTIMATION SETTINGS
# ==================================================

st.header("💰 Estimation Settings")

currency = st.selectbox(
    "Currency",
    [
        "KES",
        "USD",
        "EUR"
    ]
)

vat_rate = st.number_input(
    "VAT (%)",
    min_value=0.0,
    max_value=100.0,
    value=16.0
)

contingency = st.number_input(
    "Contingency (%)",
    min_value=0.0,
    max_value=30.0,
    value=5.0
)

st.divider()

# ==================================================
# PDF SETTINGS
# ==================================================

st.header("📄 PDF Quotation Settings")

show_logo = st.checkbox(
    "Display Company Logo",
    value=True
)

show_signature = st.checkbox(
    "Display Signature Section",
    value=True
)

show_vat = st.checkbox(
    "Include VAT",
    value=True
)

st.divider()

# ==================================================
# SAVE SETTINGS
# ==================================================

if st.button(
    "💾 Save Settings",
    use_container_width=True
):

    st.session_state.company_profile = {

        "company_name": company_name,

        "tagline": tagline,

        "phone": phone,

        "email": email,

        "location": location,

        "contractor": contractor,

        "registration": registration,

        "currency": currency,

        "vat_rate": vat_rate,

        "contingency": contingency,

        "show_logo": show_logo,

        "show_signature": show_signature,

        "show_vat": show_vat

    }

    st.success("Settings saved successfully.")

st.divider()

# ==================================================
# CURRENT SETTINGS
# ==================================================

st.header("📋 Current Configuration")

st.json(st.session_state.company_profile)

st.divider()

st.info(
    """
These settings are used when generating quotations, reports and PDFs.

In a future version, the settings can be stored permanently in a database or configuration file.
"""
)

st.caption(
    "BuildQuote AI • Settings • Version 1.0"
)