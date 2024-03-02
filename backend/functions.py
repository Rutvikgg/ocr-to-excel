"""
This contains helper functions for ocr and excel reader & writer
"""

from datetime import datetime


# Functions for OCR
def format_date(date: str) -> str | None:
    try:
        datetime_obj = datetime.strptime(date, "%Y-%m-%d")
        return datetime_obj.strftime("%d-%m-%Y")
    except (TypeError, ValueError):
        return None


def format_time(time: str) -> str | None:
    try:
        datetime_obj = datetime.strptime(time, "%H:%M")
        return datetime_obj.strftime("%I:%M %p")
    except (TypeError, ValueError):
        return None


def retrieve_taxes_receipt(taxes: list) -> list[dict[str, float | str]] | None:
    tax_list = []
    for tax in taxes:
        tax_list.append({
            "value": tax.value,
            "base": tax.base,
            "rate": tax.rate,
            "code": tax.code
        })

    if not tax_list:
        return None
    else:
        return tax_list


def retrieve_taxes_invoice(taxes: list) -> list[dict[str, float | str]] | None:
    tax_list = []
    for tax in taxes:
        tax_list.append({
            "value": tax.value,
            "rate": tax.rate
        })

    if not tax_list:
        return None
    else:
        return tax_list


def retrieve_line_items_receipt(line_items: list) -> list[dict[str, float | str]] | None:
    line_items_list = []
    for line_item in line_items:
        line_items_list.append({
            "description": line_item.description,
            "quantity": line_item.quantity,
            "unit_price": line_item.unit_price,
            "total_amount": line_item.total_amount
        })

    if not line_items_list:
        return None
    else:
        return line_items_list


def retrieve_line_items_invoice(line_items: list) -> list[dict[str, float | str]] | None:
    line_items_list = []
    for line_item in line_items:
        line_items_list.append({
            "product_code": line_item.product_code,
            "description": line_item.description,
            "quantity": line_item.quantity,
            "unit_price": line_item.unit_price,
            "total_amount": line_item.total_amount,
            "tax_rate": line_item.tax_rate,
            "tax_amount": line_item.tax_amount
        })

    if not line_items_list:
        return None
    else:
        return line_items_list


def retrieve_registration_info(reg_info: list) -> list[dict[str, str]] | None:
    reg_info_list = []
    for info in reg_info:
        reg_info_list.append({
            "type": info.type,
            "value": info.value
        })

    if not reg_info_list:
        return None
    else:
        return reg_info_list


def retrieve_reference_number(ref_nums: list) -> list[str] | None:
    ref_nums_list = []
    for ref_num in ref_nums:
        ref_nums_list.append(ref_num.value)
    if not ref_nums_list:
        return None
    else:
        return ref_nums_list


def retrieve_supplier_payment_details(supplier_payment_details: list) -> list[dict[str, float | str]] | None:
    supplier_payment_details_list = []
    for detail in supplier_payment_details:
        supplier_payment_details_list.append({
            "iban": detail.iban,
            "swift": detail.swift,
            "account_number": detail.account_number,
            "routing_number": detail.routing_number
        })

    if not supplier_payment_details_list:
        return None
    else:
        return supplier_payment_details_list


# Functions for Excel Writer
def get_line_items(items):
    formatted_list = []
    for item in items:
        product_code = item.get("product_code")
        description = item.get("description")
        quantity = item.get("quantity")
        unit_price = item.get("unit_price")
        total_amount = item.get("total_amount")
        tax_rate = item.get("tax_rate")
        tax_amount = item.get("tax_amount")
        formatted_list.append([product_code, description, quantity, unit_price, total_amount, tax_rate, tax_amount])
    return formatted_list


def get_reg_info(reg_info):
    str_list = []
    for info in reg_info:
        str_list.append(f'{info.get("type")}: {info.get("value")}')
    return ", ".join(str_list)


def get_payment_details(pay_details):
    str_list = []
    for info in pay_details:
        str_list.append(f'iban: {info.get("iban")}, swift: {info.get("swift")}, acc_num: {info.get("account_number")}, rt_num: {info.get("routing_number")}')
    return "; ".join(str_list)
