from config.house_templates import HOUSE_TEMPLATES


class HouseService:

    def __init__(self, house_type):

        self.house = HOUSE_TEMPLATES[house_type]

    def main_doors(self):
        return self.house["main_doors"]

    def internal_doors(self):
        return self.house["internal_doors"]

    def bathroom_doors(self):
        return self.house["bathroom_doors"]

    def windows(self):
        return self.house["windows"]

    def toilet_windows(self):
        return self.house["toilet_windows"]

    def summary(self):

        return self.house