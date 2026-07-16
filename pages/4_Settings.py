import streamlit as st

from config.company_profile import COMPANY_PROFILE
from config.settings_manager import save_settings, load_settings


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)


st.title("⚙️ BuildQuote AI Settings")

st.caption(
    "Configure company information used in quotations, reports and PDF documents."
)


st.divider()


# ==================================================
# INITIALIZE SETTINGS
# ==================================================

if "company_profile" not in st.session_state:

    st.session_state.company_profile = load_settings(
        COMPANY_PROFILE.copy()
    )


profile = st.session_state.company_profile



# ==================================================
# COMPANY INFORMATION
# ==================================================

st.header("🏢 Company Information")


company_name = st.text_input(

    "Company Name",

    value=profile.get(
        "company_name",
        ""
    )

)


tagline = st.text_input(

    "Company Tagline",

    value=profile.get(
        "tagline",
        ""
    )

)


contractor = st.text_input(

    "Contractor Name",

    value=profile.get(
        "contractor",
        ""
    )

)


registration = st.text_input(

    "Registration Number",

    value=profile.get(
        "registration",
        ""
    )

)



st.divider()



# ==================================================
# CONTACT INFORMATION
# ==================================================

st.header("📞 Contact Information")


phone = st.text_input(

    "Phone",

    value=profile.get(
        "phone",
        ""
    )

)


email = st.text_input(

    "Email",

    value=profile.get(
        "email",
        ""
    )

)


location = st.text_input(

    "Office Location",

    value=profile.get(
        "location",
        ""
    )

)



st.divider()



# ==================================================
# ESTIMATION SETTINGS
# ==================================================

st.header("💰 Estimation Settings")



currency_options = [

    "KES",
    "USD",
    "EUR"

]


currency = st.selectbox(

    "Currency",

    currency_options,

    index=currency_options.index(

        profile.get(
            "currency",
            "KES"
        )

    )

)



vat_rate = st.number_input(

    "VAT (%)",

    min_value=0.0,

    max_value=100.0,

    value=float(
        profile.get(
            "vat_rate",
            16.0
        )
    )

)



contingency = st.number_input(

    "Contingency (%)",

    min_value=0.0,

    max_value=30.0,

    value=float(
        profile.get(
            "contingency",
            5.0
        )
    )

)



st.divider()



# ==================================================
# PDF SETTINGS
# ==================================================

st.header("📄 PDF Quotation Settings")


show_logo = st.checkbox(

    "Display Company Logo",

    value=profile.get(
        "show_logo",
        True
    )

)



show_signature = st.checkbox(

    "Display Signature Section",

    value=profile.get(
        "show_signature",
        True
    )

)



show_vat = st.checkbox(

    "Include VAT",

    value=profile.get(
        "show_vat",
        True
    )

)



st.divider()



# ==================================================
# SAVE SETTINGS
# ==================================================

if st.button(

    "💾 Save Settings",

    use_container_width=True

):


    updated_profile = {


        "company_name": company_name,


        "tagline": tagline,


        "contractor": contractor,


        "registration": registration,


        "phone": phone,


        "email": email,


        "location": location,


        "currency": currency,


        "vat_rate": vat_rate,


        "contingency": contingency,


        "show_logo": show_logo,


        "show_signature": show_signature,


        "show_vat": show_vat

    }



    st.session_state.company_profile = updated_profile



    save_settings(
        updated_profile
    )



    st.success(
        "✅ Settings saved successfully."
    )



    st.rerun()



st.divider()



# ==================================================
# CURRENT CONFIGURATION
# ==================================================

st.header("📋 Current Configuration")

settings_table = []


for key, value in st.session_state.company_profile.items():

    settings_table.append(

        {
            "Setting": key.replace("_", " ").title(),

            "Value": value

        }

    )


st.dataframe(

    settings_table,

    use_container_width=True,

    hide_index=True

)



st.divider()



st.info(
"""
These settings are automatically used by:

✔ PDF Quotations  
✔ BOQ Reports  
✔ Cost Estimates  
✔ Client Documents  

Future versions can connect these settings to a database for multiple contractors.
"""
)



st.caption(
    "BuildQuote AI • Settings Module • Version 1.1"
)