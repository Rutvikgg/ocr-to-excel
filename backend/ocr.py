"""
This is where we use pytesseract to implement text extraction from images
"""
import constants as c
import functions as f
from mindee import Client, PredictResponse, product


class OCR:
    mindee_client = Client(api_key=c.API_KEY)

    def __init__(self):
        pass

    @staticmethod
    def ocr_receipt(receipt: str):
        input_doc = OCR.mindee_client.source_from_path(receipt)
        response: PredictResponse = OCR.mindee_client.parse(product.ReceiptV5, input_doc)
        result = response.document.inference.prediction
        data = {
            "locale": {
                "country": result.locale.country,
                "language": result.locale.language,
                "currency": result.locale.currency
            },
            "category": result.category.value,
            "date": f.format_date(result.date.value),
            "time": f.format_time(result.time.value),
            "total_net": result.total_net.value,
            "total_tax": result.total_tax.value,
            "total_amount": result.total_amount.value,
            "taxes": f.retrieve_taxes(result.taxes),
            "supplier": {
                "name": result.supplier_name.raw_value,
                "reg_info": f.retrieve_registration_info(result.supplier_company_registrations),
                "address": result.supplier_address.value,
                "phone_number": result.supplier_phone_number.value
            },
            "line_items": f.retrieve_line_items(result.line_items)
        }
        return data

    @staticmethod
    def ocr_invoice(invoice):
        pass

    @staticmethod
    def ocr_fin_doc(fin_doc):
        pass


data = OCR.ocr_receipt("../test_data/receipt_7.png")
print(data)
