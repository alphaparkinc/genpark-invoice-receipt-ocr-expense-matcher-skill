from client import InvoiceOcrMatcherClient

def main():
    client = InvoiceOcrMatcherClient()
    res = client.match_invoice(invoice_text='Vendor Inc - $500')
    print(f"Result for matched: {res['matched']}")

if __name__ == "__main__":
    main()
