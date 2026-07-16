from services.house_service import HouseService

house = HouseService("3 Bedroom")

print()

print("====== HOUSE TEMPLATE ======\n")

for key, value in house.summary().items():

    print(f"{key:<20}{value}")