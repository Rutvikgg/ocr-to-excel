"""
Constants for ocr and excel reader & writer
"""
from openpyxl.styles import Font

# OCR constants
API_KEY: str = "da251ff94888f0bda69aafd199f12179"

# EXCEL WRITER constants
SINGLE_SHEET_TITLE: str = "Extracted Data"
SINGLE_SHEET_HEADERS: tuple = ("Date", "Time", "Language", "Currency", "Document Type", "Receipt/Invoice No.",
                               "Reference Numbers", "Due Date", "Net Total", "Total Tax", "Total Amount", "Tip",
                               "Item Code", "Item Description", "Quantity", "Unit Price", "Total", "Tax Rate",
                               "Tax Amount", "Supplier Name", "Supplier Phone", "Supplier Address",
                               "Supplier Registration Info", "Payment Details", "Customer Name", "Customer Address",
                               "Customer Registration Info")
MULTI_SHEET_TITLES: tuple = ("Main Info", "Supplier Info", "Customer Info", "Line Items")
MAIN_SHEET_HEADERS: tuple = ("Date", "Time", "Language", "Currency", "Document Type", "Receipt|Invoice No.",
                             "Reference Numbers", "Due Date", "Net Total", "Total Tax", "Total Amount", "Tip")
SUPPLIER_SHEET_HEADERS: tuple = ("Receipt/Invoice No.", "Payment Details", "Name", "Address", "Phone Number",
                                 "Registration Info")
CUSTOMER_SHEET_HEADERS: tuple = ("Receipt/Invoice No.", "Name", "Address", "Registration Info")
LINE_ITEMS_SHEET_HEADERS: tuple = ("Receipt/Invoice No.", "Item Code", "Description", "Quantity", "Unit Price", "Tax Rate", "Tax Amount",
                                   "Line Total")

# Excel Styles
BOLD_FONT: Font = Font(bold=True)
