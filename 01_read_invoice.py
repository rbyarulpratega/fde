import csv

with open("homework_invoices.csv") as file:
    reader=csv.DictReader(file)
    invoices = list(reader)
    totalinvoices=len(invoices)
    invoice_greaterthan100k = 0
    invalidamt = 0
    for invoice in invoices:
        vendor = invoice['vendor']
        amount = invoice['amount']
        status = invoice['status']
        print(f"Vendor:{vendor},Amount:{amount},Status:{status}")
        try:
           amount = float(amount)
           if amount > 100000:
            invoice_greaterthan100k += 1
        except ValueError:
            invalidamt += 1
print(f"Total Invoices: {totalinvoices}")
print(f"Invoice Amount Greater than 100K: {invoice_greaterthan100k}")
print(f"Invalid Amount: {invalidamt}")