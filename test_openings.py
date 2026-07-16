from estimators.openings import OpeningsEstimator

opening = OpeningsEstimator(

    main_doors=1,

    internal_doors=5,

    bathroom_doors=2,

    windows=10,

    toilet_windows=2

)

print()

print("====== OPENINGS ======\n")

for item, value in opening.summary().items():

    print(

        f"{item:<20}"

        f"{value['quantity']} "

        f"{value['unit']}"

    )