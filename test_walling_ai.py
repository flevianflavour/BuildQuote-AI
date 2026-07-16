from estimators.walling_estimator import WallingEstimator
from services.material_service import MaterialService



material = MaterialService(
    "Machine Cut Stone"
)



wall = WallingEstimator(

    length=12,

    width=10,

    height=3,

    openings_area=18,

    coverage=material.coverage(),

    material_name=material.name()

)



print(wall.summary())
