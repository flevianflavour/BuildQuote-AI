from estimators.excavation import ExcavationEstimator

excavation = ExcavationEstimator(12, 10)

print("\n========== EXCAVATION ==========\n")

results = excavation.summary()

for item, details in results.items():

    print(
        f"{item:<25}"
        f"{details['quantity']} "
        f"{details['unit']}"
    )