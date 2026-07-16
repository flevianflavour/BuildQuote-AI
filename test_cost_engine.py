from services.estimation_engine import EstimationEngine
from costing.pricing_engine import CostEngine

engine = EstimationEngine(
    length=12,
    width=10,
    height=3,
    house_type="Bedsitter",
    wall_material="Machine Cut Stone"
)

estimate = engine.generate_boq()

cost = CostEngine(
    estimate["boq"],
    "Mombasa"
)

print(cost.summary())