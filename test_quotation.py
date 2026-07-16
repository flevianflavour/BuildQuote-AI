from models.project import Project
from services.estimation_service import EstimationService
from services.quotation_service import QuotationService

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

estimate = EstimationService().estimate(project)

QuotationService().generate(project, estimate)