"""
This contains helper functions for ocr and excel reader & writer
"""

from datetime import datetime


def format_date(date: str):
    try:
        datetime_obj = datetime.strptime(date, "%Y-%m-%d")
        return datetime_obj.strftime("%d-%m-%Y")
    except TypeError:
        return None


def format_time(time: str):
    try:
        datetime_obj = datetime.strptime(time, "%H:%M")
        return datetime_obj.strftime("%I:%M %p")
    except TypeError:
        return None


def retrieve_taxes_receipt(taxes):
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


def retrieve_taxes_invoice(taxes):
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


def retrieve_line_items_receipt(line_items):
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


def retrieve_line_items_invoice(line_items):
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


def retrieve_registration_info(reg_info):
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


def retrieve_reference_number(ref_nums):
    ref_nums_list = []
    for ref_num in ref_nums:
        ref_nums_list.append(ref_num.value)
    if not ref_nums_list:
        return None
    else:
        return ref_nums_list


def retrieve_supplier_payment_details(supplier_payment_details):
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
