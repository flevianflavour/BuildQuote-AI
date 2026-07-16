from services.house_service import HouseService
from estimators.openings import OpeningsEstimator

house = HouseService("3 Bedroom")

opening = OpeningsEstimator(

    main_doors=house.main_doors(),

    internal_doors=house.internal_doors(),

    bathroom_doors=house.bathroom_doors(),

    windows=house.windows(),

    toilet_windows=house.toilet_windows()

)

print()

print("====== AI OPENINGS ======\n")

for item, value in opening.summary().items():

    print(

        f"{item:<20}"

        f"{value['quantity']} "

        f"{value['unit']}"

    )