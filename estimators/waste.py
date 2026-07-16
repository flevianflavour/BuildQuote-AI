class WasteCalculator:

    def __init__(self):

        self.block_waste = 0.05

        self.cement_waste = 0.03

        self.paint_waste = 0.10

        self.tile_waste = 0.08

    def add_waste(self, quantity, waste):

        return round(
            quantity * (1 + waste),
            2
        )