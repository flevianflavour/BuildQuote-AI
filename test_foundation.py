from estimators.foundation_estimator import FoundationEstimator

foundation = FoundationEstimator(
    length=12,
    width=10
)

results = foundation.summary()

print("\n========== FOUNDATION BOQ ==========\n")

for section, items in results.items():

    print(f"\n--- {section} ---")

    for item, details in items.items():

        print(
            f"{item:<25}"
            f"{details['quantity']} "
            f"{details['unit']}"
        )