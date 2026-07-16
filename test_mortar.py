from estimators.mortar import MortarEstimator


mortar = MortarEstimator(

    wall_material_quantity=1425,

    mortar_ratio="1:4"

)


print(mortar.summary())