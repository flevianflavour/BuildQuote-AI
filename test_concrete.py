from estimators.concrete import ConcreteCalculator

concrete = ConcreteCalculator(

    volume=5.28,

    mix_ratio="1:2:3"

)

print()

print("========== CONCRETE ESTIMATE ==========\n")

for item, value in concrete.summary().items():

    print(

        f"{item:<20}"

        f"{value['quantity']} "

        f"{value['unit']}"

    )