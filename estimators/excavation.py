class ExcavationEstimator:

    def __init__(self, length, width):

        self.length = length
        self.width = width

        # Kenyan Standard
        self.foundation_width = 0.60
        self.foundation_depth = 1.20

    def perimeter(self):

        return 2 * (self.length + self.width)

    def trench_length(self):

        return self.perimeter()

    def trench_volume(self):

        return (
            self.trench_length()
            * self.foundation_width
            * self.foundation_depth
        )

    def summary(self):

        return {

            "Trench Length": {
                "unit": "m",
                "quantity": round(self.trench_length(), 2)
            },

            "Excavation": {
                "unit": "m³",
                "quantity": round(self.trench_volume(), 2)
            }

        }