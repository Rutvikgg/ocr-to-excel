"""
This is where we use pytesseract to implement text extraction from images
"""
import backend.constants as c
import backend.functions as f
from mindee import Client, PredictResponse, product


class OCR:
    mindee_client = Client(api_key=c.API_KEY)

    def __init__(self):
        pass

    @staticmethod
    def ocr_receipt(receipt: str) -> dict[str, dict | list | float | str | None]:
        input_doc = OCR.mindee_client.source_from_path(receipt)
        response: PredictResponse = OCR.mindee_client.parse(product.ReceiptV5, input_doc)
        result = response.document.inference.prediction
        receipt_data = {
            "document_type": result.document_type.value,
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
            "tip": result.tip.value,
            "taxes": f.retrieve_taxes_receipt(result.taxes),
            "supplier": {
                "name": result.supplier_name.raw_value,
                "reg_info": f.retrieve_registration_info(result.supplier_company_registrations),
                "address": result.supplier_address.value,
                "phone_number": result.supplier_phone_number.value
            },
            "line_items": f.retrieve_line_items_receipt(result.line_items)
        }
        return receipt_data

    @staticmethod
    def ocr_invoice(invoice: str) -> dict[str, dict | list | float | str | None]:
        input_doc = OCR.mindee_client.source_from_path(invoice)
        response: PredictResponse = OCR.mindee_client.parse(product.InvoiceV4, input_doc)
        result = response.document.inference.prediction
        invoice_data = {
            "document_type": result.document_type.value,
            "locale": {
                "language": result.locale.language,
                "currency": result.locale.currency
            },
            "category": result.category.value,
            "invoice_number": result.invoice_number.value,
            "reference_numbers": f.retrieve_reference_number(result.reference_numbers),
            "date": f.format_date(result.date.value),
            "due_date": f.format_date(result.due_date.value),
            "total_net": result.total_net.value,
            "total_tax": result.total_tax.value,
            "total_amount": result.total_amount.value,
            "taxes": f.retrieve_taxes_invoice(result.taxes),
            "supplier": {
                "payment_details": f.retrieve_supplier_payment_details(result.supplier_payment_details),
                "name": result.supplier_name.raw_value,
                "reg_info": f.retrieve_registration_info(result.supplier_company_registrations),
                "address": result.supplier_address.value
            },
            "customer": {
                "name": result.customer_name.raw_value,
                "reg_info": f.retrieve_registration_info(result.customer_company_registrations),
                "address": result.customer_address.value
            },
            "line_items": f.retrieve_line_items_invoice(result.line_items)
        }
        return invoice_data

    @staticmethod
    def ocr_fin_doc(fin_doc: str) -> dict[str, dict | list | float | str | None]:
        input_doc = OCR.mindee_client.source_from_path(fin_doc)
        response: PredictResponse = OCR.mindee_client.parse(product.FinancialDocumentV1, input_doc)
        result = response.document.inference.prediction
        fin_doc_data = {
            "document_type": result.document_type.value,
            "locale": {
                "language": result.locale.language,
                "currency": result.locale.currency
            },
            "invoice_number": result.invoice_number.value,
            "reference_numbers": f.retrieve_reference_number(result.reference_numbers),
            "date": f.format_date(result.date.value),
            "time": f.format_time(result.time.value),
            "due_date": f.format_date(result.due_date.value),
            "total_net": result.total_net.value,
            "total_tax": result.total_tax.value,
            "total_amount": result.total_amount.value,
            "tip": result.tip.value,
            "taxes": f.retrieve_taxes_receipt(result.taxes),
            "supplier": {
                "payment_details": f.retrieve_supplier_payment_details(result.supplier_payment_details),
                "name": result.supplier_name.raw_value,
                "reg_info": f.retrieve_registration_info(result.supplier_company_registrations),
                "address": result.supplier_address.value,
                "phone_number": result.supplier_phone_number.value
            },
            "customer": {
                "name": result.customer_name.raw_value,
                "reg_info": f.retrieve_registration_info(result.customer_company_registrations),
                "address": result.customer_address.value
            },
            "line_items": f.retrieve_line_items_invoice(result.line_items)
        }
        return fin_doc_data
