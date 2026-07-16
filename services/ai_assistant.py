"""
BuildQuote AI
Rule-Based AI Assistant
"""

def get_ai_recommendations(project, estimate):

    recommendations = []

    county = project["County"]
    roof = project["Roof Type"]
    wall = project["Block Type"]
    total = estimate["grand_total"]

    # ===============================
    # Coastal Counties
    # ===============================

    coastal = [
        "Mombasa",
        "Kilifi",
        "Kwale",
        "Lamu",
        "Tana River"
    ]

    # ===============================
    # Cold / Highland Counties
    # ===============================

    cold = [
        "Nairobi",
        "Nyeri",
        "Kiambu",
        "Murang'a",
        "Nyandarua",
        "Kirinyaga",
        "Meru",
        "Embu",
        "Uasin Gishu",
        "Nandi",
        "Kericho",
        "Elgeyo Marakwet",
        "Trans Nzoia",
        "Bomet"
    ]

    # ===============================
    # Hot / Dry Counties
    # ===============================

    hot = [
        "Turkana",
        "Marsabit",
        "Garissa",
        "Mandera",
        "Wajir",
        "Isiolo",
        "Samburu"
    ]

    # ===============================
    # Heavy Rainfall Counties
    # ===============================

    rainy = [
        "Kakamega",
        "Vihiga",
        "Bungoma",
        "Kisii",
        "Nyamira",
        "Migori",
        "Siaya",
        "Busia",
        "Homa Bay"
    ]

    # --------------------------------
    # Coastal Advice
    # --------------------------------

    if county in coastal:

        recommendations.append(
            "🌊 Use corrosion-resistant roofing sheets due to salty coastal air."
        )

        recommendations.append(
            "🛡 Apply anti-rust treatment on steel members."
        )

    # --------------------------------
    # Cold Areas
    # --------------------------------

    elif county in cold:

        recommendations.append(
            "🏠 Install ceiling insulation to improve indoor warmth."
        )

        recommendations.append(
            "☀ Position larger windows to maximize natural daylight."
        )

    # --------------------------------
    # Hot Areas
    # --------------------------------

    elif county in hot:

        recommendations.append(
            "🌞 Use reflective roofing and roof insulation to reduce heat."
        )

        recommendations.append(
            "🌳 Plant shade trees around the house."
        )

    # --------------------------------
    # Rainy Areas
    # --------------------------------

    elif county in rainy:

        recommendations.append(
            "🌧 Design larger roof overhangs to protect external walls."
        )

        recommendations.append(
            "💧 Install proper drainage around the foundation."
        )

    # --------------------------------
    # Roofing Advice
    # --------------------------------

    if roof == "Concrete Roof":

        recommendations.append(
            "🏗 Verify structural loading before constructing a concrete roof."
        )

    elif roof == "Mabati":

        recommendations.append(
            "🔊 Install insulation to reduce rain noise."
        )

    elif roof == "Tile Roof":

        recommendations.append(
            "🏡 Tile roofs improve thermal comfort and durability."
        )

    elif roof == "Decra Roof":

        recommendations.append(
            "⭐ Decra roofing offers long-term durability with low maintenance."
        )

    # --------------------------------
    # Wall Advice
    # --------------------------------

    if wall == "Machine Cut Stone":

        recommendations.append(
            "🧱 Machine Cut Stone provides strong and accurate wall alignment."
        )

    elif wall == "Coral Blocks":

        recommendations.append(
            "🌊 Coral blocks perform well in coastal environments."
        )

    elif wall == "Concrete Blocks":

        recommendations.append(
            "🏢 Concrete blocks are suitable for commercial buildings."
        )

    elif wall == "Clay Bricks":

        recommendations.append(
            "🔥 Clay bricks provide excellent thermal insulation."
        )

    # --------------------------------
    # Budget Advice
    # --------------------------------

    if total > 5000000:

        recommendations.append(
            "💰 This is a high-value project. Schedule phased procurement."
        )

    else:

        recommendations.append(
            "💵 Compare supplier quotations before purchasing materials."
        )

    recommendations.append(
        "📦 Purchase materials in phases to reduce wastage."
    )

    recommendations.append(
        "📋 Keep a contingency budget of 5–10%."
    )

    return recommendations