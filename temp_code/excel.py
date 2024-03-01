import openpyxl
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font

workbook = load_workbook("../test_data/excel_test.xlsx")

data = ["Name", "Address", "Contact"]
sheet = workbook["Line Items"]
row = 3
# workbook.create_sheet("Description")
# sheet.title = "Line Items"
# bold_font = Font(bold=True)
# for col_idx, header in enumerate(data, 1):
#     sheet.cell(row, col_idx).value = header
#     sheet.cell(row, col_idx).font = bold_font

sheet.append(data)
workbook.save("../test_data/excel_test.xlsx")
