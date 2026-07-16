from services.material_engine import material_engine

print()

print("CONCRETE")

print(
    material_engine.concrete_mix(
        10
    )
)

print()

print("MORTAR")

print(
    material_engine.mortar_mix(
        3
    )
)

print()

print("WALLING")

print(
    material_engine.wall_materials(
        150
    )
)