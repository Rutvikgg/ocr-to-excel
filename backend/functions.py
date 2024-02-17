"""
This contains helper functions for ocr and excel reader & writer
"""

from datetime import datetime


def format_date(date: str):
    datetime_obj = datetime.strptime(date, "%Y-%m-%d")
    return datetime_obj.strftime("%d-%m-%Y")


def format_time(time: str):
    datetime_obj = datetime.strptime(time, "%H:%M")
    return datetime_obj.strftime("%I:%M %p")


def retrieve_taxes(taxes):
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


def retrieve_line_items(line_items):
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
