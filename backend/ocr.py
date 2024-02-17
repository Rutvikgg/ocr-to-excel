"""
This is where we use pytesseract to implement text extraction from images
"""
import constants as c
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
            "date": result.date.value
        }

    @staticmethod
    def ocr_invoice(invoice):
        pass

    @staticmethod
    def ocr_fin_doc(fin_doc):
        pass
