import pandas as pd

def load_materials():
    return pd.read_csv("data/materials.csv")

def get_material_price(material_name):
    materials = load_materials()

    result = materials.loc[
        materials["Material"] == material_name,
        "Price"
    ]

    if not result.empty:
        return result.iloc[0]

    return None

print("Testing BuildQuote AI")
print(load_materials())
print("Price of Cement:", get_material_price("Cement"))