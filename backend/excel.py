"""
This is where we implement excel functionality
"""

from openpyxl.workbook import Workbook
import backend.constants as c
import backend.functions as f


class ExcelWriter:
    def __init__(self):
        pass

    @staticmethod
    def create_wb(data: dict, save_location: str | None = None):
        wb = Workbook()
        sheet = wb.active
        sheet.title = c.DEFAULT_SHEET_TITLE

        # Adding heading for columns
        for i, heading in enumerate(c.SINGLE_SHEET_HEADERS, 1):
            cell = sheet.cell(3, i)
            cell.value = heading
            cell.font = c.BOLD_FONT

        # Cell formatting
        for col in sheet.iter_cols():
            max_length = 0
            for cell in col:
                if cell.value is None:
                    continue
                max_length = max(max_length, len(cell.value))
            sheet.column_dimensions[col[0].column_letter].width = max_length + 1

        # Adding Data
        line_items = f.get_line_items(data.get("line_items"))
        append_list = [data.get("date"),
                       data.get("time"),
                       data.get("locale", {}).get("language"),
                       data.get("locale", {}).get("currency"),
                       data.get("document_type"),
                       data.get("invoice_number"),
                       data.get("due_date"),
                       data.get("total_net"),
                       data.get("total_tax"),
                       data.get("total_amount"),
                       line_items[0][0],
                       line_items[0][1],
                       line_items[0][2],
                       line_items[0][3],
                       line_items[0][4],
                       line_items[0][5],
                       line_items[0][6],
                       data.get("supplier", {}).get("name"),
                       data.get("supplier", {}).get("phone_number"),
                       data.get("supplier", {}).get("address"),
                       f.get_reg_info(data.get("supplier", {}).get("reg_info")),
                       f.get_payment_details(data.get("supplier", {}).get("payment_details"))]
        sheet.append(append_list)
        for idx, item in enumerate(line_items[1:]):
            sheet.cell(row=idx + 5, column=11).value = item[0]
            sheet.cell(row=idx + 5, column=12).value = item[1]
            sheet.cell(row=idx + 5, column=13).value = item[2]
            sheet.cell(row=idx + 5, column=14).value = item[3]
            sheet.cell(row=idx + 5, column=15).value = item[4]
            sheet.cell(row=idx + 5, column=16).value = item[5]
            sheet.cell(row=idx + 5, column=17).value = item[6]

        # Saving worksheet
        wb.save(save_location)

    @staticmethod
    def create_wb_sheeted(data, save_location=None):
        pass

    @staticmethod
    def append_wb(data, workbook, save_location=None):
        pass

    @staticmethod
    def append_wb_sheeted(data, workbook, save_location=None):
        pass


fin_doc_data = {
    "document_type": "Expense Receipt",
    "locale": {
        "language": "en",
        "currency": "INR"
    },
    "invoice_number": 80456,
    "reference_numbers": ["AP10256", "UN5847", "AT548R"],
    "date": "02-03-2024",
    "time": "08:05 PM",
    "due_date": "06-04-2024",
    "total_net": 42000,
    "total_tax": 456.23,
    "total_amount": 42456.23,
    "tip": None,
    "taxes": [{"value": 456, "rate": 3.5}, {"value": 456, "rate": 3.5}],
    "supplier": {
        "payment_details": [{
            "iban": " GB29 NWBK 6016 1331 9268 19",
            "swift": "NWBKGB2L",
            "account_number": 1234567890,
            "routing_number": 123456789
        }, {
            "iban": " GB29 NWBK 6016 1331 9268 19",
            "swift": "NWBKGB2L",
            "account_number": 3658974106,
            "routing_number": 12569843
        }],
        "name": "John Doe Enterprises",
        "reg_info": [{
            "type": "Fake Business Registry",
            "value": "ABC123456"
        }],
        "address": "123 Fake Street, Faketown, FK1234",
        "phone_number": "+1 (555) 123-4567"
    },
    "customer": {
        "name": "Jane Smith Co.",
        "reg_info": [{
            "type": "Fake Business Registry",
            "value": "ABC123456"
        }],
        "address": "456 Imaginary Avenue, Fantasyville, FA5678"
    },
    "line_items": [
        {
            "product_code": "PRD001",
            "description": "Widget A",
            "quantity": 10,
            "unit_price": 25.99,
            "total_amount": 259.90,
            "tax_rate": 0.1,
            "tax_amount": 25.99
        },
        {
            "product_code": "PRD002",
            "description": "Widget B",
            "quantity": 5,
            "unit_price": 15.49,
            "total_amount": 77.45,
            "tax_rate": 0.08,
            "tax_amount": 6.20
        },
        {
            "product_code": "PRD003",
            "description": "Widget C",
            "quantity": 20,
            "unit_price": 8.75,
            "total_amount": 175.00,
            "tax_rate": 0.05,
            "tax_amount": 8.75
        }
    ]
}
ExcelWriter.create_wb(fin_doc_data, "../test_data/excel_main_test.xlsx")
