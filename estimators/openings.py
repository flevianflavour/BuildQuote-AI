class OpeningsEstimator:

    # Standard Kenyan Sizes (metres)

    MAIN_DOOR = 1.2 * 2.1

    INTERNAL_DOOR = 0.9 * 2.1

    BATHROOM_DOOR = 0.75 * 2.1

    WINDOW = 1.2 * 1.2

    TOILET_WINDOW = 0.6 * 0.6

    def __init__(

        self,

        main_doors,

        internal_doors,

        bathroom_doors,

        windows,

        toilet_windows

    ):

        self.main_doors = main_doors

        self.internal_doors = internal_doors

        self.bathroom_doors = bathroom_doors

        self.windows = windows

        self.toilet_windows = toilet_windows

    def total_area(self):

        return (

            self.main_doors * self.MAIN_DOOR

            +

            self.internal_doors * self.INTERNAL_DOOR

            +

            self.bathroom_doors * self.BATHROOM_DOOR

            +

            self.windows * self.WINDOW

            +

            self.toilet_windows * self.TOILET_WINDOW

        )

    def summary(self):

        return {

            "Opening Area": {

                "unit": "m²",

                "quantity": round(

                    self.total_area(),

                    2

                )

            }

        }