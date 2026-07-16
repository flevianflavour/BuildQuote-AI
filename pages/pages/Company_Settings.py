"""
BuildQuote AI

Company Settings Page

Allows contractors to customize:
- Company Name
- Logo
- Phone
- Email
- Location
- Registration
"""


import streamlit as st
import os
import shutil


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(

    page_title="Company Settings",

    page_icon="⚙️",

    layout="wide"

)



st.title("⚙️ Company Profile Settings")


st.write(
    "Update your company details used in quotations."
)



# ==========================================
# LOAD CURRENT PROFILE
# ==========================================


from config.company_profile import COMPANY_PROFILE



# ==========================================
# COMPANY DETAILS
# ==========================================


company_name = st.text_input(

    "Company Name",

    COMPANY_PROFILE["company_name"]

)


tagline = st.text_input(

    "Company Tagline",

    COMPANY_PROFILE["tagline"]

)


phone = st.text_input(

    "Phone Number",

    COMPANY_PROFILE["phone"]

)


email = st.text_input(

    "Email Address",

    COMPANY_PROFILE["email"]

)


location = st.text_input(

    "Location",

    COMPANY_PROFILE["location"]

)


registration = st.text_input(

    "Registration Number",

    COMPANY_PROFILE["registration"]

)


contractor = st.text_input(

    "Contractor Name",

    COMPANY_PROFILE["contractor"]

)



# ==========================================
# LOGO UPLOAD
# ==========================================


st.subheader("🖼 Company Logo")


logo = st.file_uploader(

    "Upload Logo",

    type=[
        "png",
        "jpg",
        "jpeg"
    ]

)



# ==========================================
# SAVE SETTINGS
# ==========================================


if st.button(
    "💾 Save Company Profile",
    use_container_width=True
):


    profile_code = f'''
"""
BuildQuote AI
Company Profile
"""


COMPANY_PROFILE = {{

    "company_name": "{company_name}",

    "tagline": "{tagline}",

    "phone": "{phone}",

    "email": "{email}",

    "location": "{location}",

    "contractor": "{contractor}",

    "registration": "{registration}"

}}
'''


    with open(

        "config/company_profile.py",

        "w"

    ) as file:

        file.write(profile_code)



    # Save logo

    if logo:


        os.makedirs(

            "assets",

            exist_ok=True

        )


        with open(

            "assets/logo.png",

            "wb"

        ) as f:

            f.write(
                logo.getbuffer()
            )


    st.success(

        "Company profile updated successfully!"

    )


    st.info(

        "Restart Streamlit for changes to appear in new quotations."

    )