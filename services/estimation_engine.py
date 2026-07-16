from estimators.foundation_estimator import FoundationEstimator
from estimators.openings import OpeningsEstimator
from estimators.walling_estimator import WallingEstimator
from estimators.mortar import MortarEstimator
from estimators.concrete import ConcreteCalculator

from services.house_service import HouseService
from services.material_service import MaterialService


class EstimationEngine:

    def __init__(
        self,
        length,
        width,
        height,
        house_type,
        wall_material
    ):

        self.length = length
        self.width = width
        self.height = height

        self.house = HouseService(house_type)
        self.material = MaterialService(wall_material)

    # -------------------------------------------------
    # FOUNDATION
    # -------------------------------------------------

    def foundation(self):

        foundation = FoundationEstimator(
            self.length,
            self.width
        )

        return foundation.summary()

    # -------------------------------------------------
    # OPENINGS
    # -------------------------------------------------

    def openings(self):

        return OpeningsEstimator(

            main_doors=self.house.main_doors(),

            internal_doors=self.house.internal_doors(),

            bathroom_doors=self.house.bathroom_doors(),

            windows=self.house.windows(),

            toilet_windows=self.house.toilet_windows()

        )

    # -------------------------------------------------
    # WALLING
    # -------------------------------------------------

    def walling(self):

        openings = self.openings()

        wall = WallingEstimator(

            length=self.length,

            width=self.width,

            height=self.height,

            openings_area=openings.total_area(),

            coverage=self.material.coverage(),

            material_name=self.material.name()

        )

        return wall.summary()

    # -------------------------------------------------
    # MORTAR
    # -------------------------------------------------

    def mortar(self):

        wall = self.walling()

        mortar = MortarEstimator(

            wall["Required Quantity"]["quantity"],

            self.material.mortar_ratio()

        )

        return mortar.summary()

    # -------------------------------------------------
    # CONCRETE
    # -------------------------------------------------

    def concrete(self):

        foundation = FoundationEstimator(

            self.length,

            self.width

        )

        concrete = ConcreteCalculator(

            foundation.foundation_concrete_volume()

        )

        return concrete.summary()

    # -------------------------------------------------
    # MASTER BOQ
    # -------------------------------------------------

    def generate_boq(self):

        perimeter = 2 * (self.length + self.width)

        walling = self.walling()

        mortar = self.mortar()

        foundation = self.foundation()

        concrete = self.concrete()

        blocks = walling["Required Quantity"]["quantity"]

        mason_days = round(blocks / 150, 2)

        return {

            "perimeter": perimeter,

            "wall_area": walling["Net Wall Area"]["quantity"],

            "material_name": self.material.name(),

            "material_unit": walling["Required Quantity"]["unit"],

            "coverage": self.material.coverage(),

            "blocks": blocks,

            "cement_bags": mortar["Cement"]["quantity"],

            "sand_tons": mortar["Sand"]["quantity"],

            "mason_days": mason_days,

            "boq": {

                "Foundation": foundation,

                "Walling": walling,

                "Mortar": mortar,

                "Concrete": concrete

            }

        }