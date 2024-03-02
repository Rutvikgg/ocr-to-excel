"""
Constants for ocr and excel reader & writer
"""
from openpyxl.styles import Font

# OCR constants
API_KEY: str = "da251ff94888f0bda69aafd199f12179"

# EXCEL WRITER constants
DEFAULT_SHEET_TITLE: str = "Extracted Data"
SINGLE_SHEET_HEADERS: tuple = ("Date", "Time", "Language", "Currency", "Document Type", "Receipt|Invoice No.",
                               "Due Date", "Net Total", "Total Tax", "Total Amount", "Item Code", "Item Description",
                               "Quantity", "Unit Price", "Total", "Tax Rate", "Tax Amount", "Supplier Name",
                               "Supplier Phone", "Supplier Address", "Registration Info", "Payment Details")

# Excel Styles
BOLD_FONT = Font(bold=True)
