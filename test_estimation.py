from models.project import Project
from services.estimation_service import EstimationService

project = Project(
    client_name="John Mwangi",
    project_name="3 Bedroom Bungalow",
    county="Mombasa",
    building_type="Residential",
    floors=1,
    length=12,
    width=10,
    height=3
)

service = EstimationService()

result = service.estimate(project)

print("========== ESTIMATION ==========")

for key, value in result.items():
    print(f"{key}: {value}")