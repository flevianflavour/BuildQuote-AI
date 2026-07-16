class VATCalculator:

    VAT_RATE = 0.16

    def __init__(self, subtotal):

        self.subtotal = subtotal

    def vat_amount(self):

        return round(
            self.subtotal * self.VAT_RATE,
            2
        )

    def total(self):

        return round(
            self.subtotal + self.vat_amount(),
            2
        )

    def summary(self):

        return {

            "Subtotal": self.subtotal,

            "VAT Rate": "16%",

            "VAT Amount": self.vat_amount(),

            "Grand Total": self.total()

        }