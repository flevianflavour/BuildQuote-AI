from config.kenya_standards import ROOFING


class RoofService:

    def __init__(self, roof):

        self.roof = roof

    def timber(self):

        return ROOFING[self.roof]["timber_per_m2"]

    def ridge_price(self):

        return ROOFING[self.roof]["ridge_price"]