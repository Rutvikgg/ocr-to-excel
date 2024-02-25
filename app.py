"""
This is the main file where the app will start.
"""
from frontend.view import View
from backend.ocr import OCR


def run():
    print("App is Starting...")
    v = View()
    v.create_main_view()
    v.run_main_view()
    print(v.get_filename())
    print(v.get_radio_selection())
    if v.get_radio_selection() == "er":
        result = OCR.ocr_receipt(v.get_filename())
        print(result)
    elif v.get_radio_selection() == "in":
        result = OCR.ocr_invoice(v.get_filename())
        print(result)
    else:
        result = OCR.ocr_fin_doc(v.get_filename())
        print(result)


if __name__ == '__main__':
    run()
