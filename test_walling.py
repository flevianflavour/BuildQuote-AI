from estimators.walling_estimator import WallingEstimator


wall = WallingEstimator(

    length=12,

    width=10,

    height=3,

    openings_area=18,

    coverage=12.5,

    material_name="Machine Cut Stone"

)


result = wall.summary()


print(result)