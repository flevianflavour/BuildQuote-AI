class QuotationService:

    def generate(self, project, estimate):

        subtotal = (
            estimate["block_cost"]
            + estimate["cement_cost"]
            + estimate["labour_cost"]
        )

        vat = subtotal * 0.16

        total = subtotal + vat

        print("\n")

        print("=" * 50)

        print("              BUILDQUOTE AI")

        print("=" * 50)

        print(f"Client   : {project.client_name}")

        print(f"Project  : {project.project_name}")

        print(f"County   : {project.county}")

        print("-" * 50)

        print("DESCRIPTION".ljust(20), "TOTAL")

        print("-" * 50)

        print(f"Blocks".ljust(20), f"KES {estimate['block_cost']:,}")

        print(f"Cement".ljust(20), f"KES {estimate['cement_cost']:,}")

        print(f"Labour".ljust(20), f"KES {estimate['labour_cost']:,}")

        print("-" * 50)

        print(f"Subtotal".ljust(20), f"KES {subtotal:,}")

        print(f"VAT (16%)".ljust(20), f"KES {vat:,.0f}")

        print(f"TOTAL".ljust(20), f"KES {total:,.0f}")

        print("=" * 50)