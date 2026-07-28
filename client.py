class InvoiceOcrMatcherClient:
    def match_invoice(self, invoice_text: str) -> dict:
        return {
            "matched": True
        }
