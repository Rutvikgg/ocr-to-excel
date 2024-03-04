"""
This is the main file where the app will start.
"""
from backend.ocr import OCR
from frontend.view import View


def run() -> None:
    print("App is Starting...")

    # Main GUI start
    v = View()
    v.create_main_view()
    v.run_main_view()
    print(v.get_file_for_ocr())
    print(v.get_document_radio_selection())

    # Extracting Data with OCR
    try:
        if v.get_document_radio_selection() == "er":
            result = OCR.ocr_receipt(v.get_file_for_ocr())
            print(result)
        elif v.get_document_radio_selection() == "in":
            result = OCR.ocr_invoice(v.get_file_for_ocr())
            print(result)
        else:
            result = OCR.ocr_fin_doc(v.get_file_for_ocr())
            print(result)
    except FileNotFoundError:
        print("App closed!")

    # Excel GUI start

    # Converting Data into Excel
    """
    Example code
    if option_1:
        if format_single_sheet:
            ExcelWriter.create_wb(data, save_location)
        else:
            ExcelWriter.create_multi_sheet_wb(data, save_location)
    else:
        if ExcelWriter.is_wb_single_sheet(wb_location):
            ExcelWriter.append_wb(data, wb_location, save_location)
        else:
            ExcelWriter.append_multi_sheet_wb(data, wb_location, save_location)  
    """


if __name__ == '__main__':
    run()
