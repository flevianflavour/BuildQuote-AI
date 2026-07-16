from services.material_service import MaterialService


material = MaterialService(
    "Machine Cut Stone"
)


print("Material:", material.name())

print(
    "Coverage:",
    material.coverage(),
    "pieces/m²"
)

print(
    "Mortar Ratio:",
    material.mortar_ratio()
)