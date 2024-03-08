"""
This is the main file where the app will start.
"""
from backend.excel import ExcelWriter
from backend.ocr import OCR
from frontend.view import MainView, ExcelView, ExitView


def run() -> None:
    global result
    print("App is Starting...")

    # Main GUI start
    v = MainView()
    v.create_main_view()
    v.run_main_view()

    print("Your document is being converted....")
    # Extracting Data with OCR
    try:
        if v.get_document_radio_selection() == "er":
            result = OCR.ocr_receipt(v.get_file_for_ocr())
        elif v.get_document_radio_selection() == "in":
            result = OCR.ocr_invoice(v.get_file_for_ocr())
        else:
            result = OCR.ocr_fin_doc(v.get_file_for_ocr())
    except FileNotFoundError:
        print("App closed!")
        exit()

    # Excel GUI start
    v = ExcelView()
    v.create_excel_view()
    v.run_excel_view()

    # Converting Data into Excel
    try:
        if v.get_save_option_selection() == 1:
            if v.get_sheet_selection() == 1:
                ExcelWriter.create_wb(result, v.get_save_location())
            else:
                ExcelWriter.create_multi_sheet_wb(result, v.get_save_location())
        else:
            if ExcelWriter.is_wb_single_sheet(v.get_excel_file()):
                ExcelWriter.append_wb(result, v.get_excel_file(), v.get_new_save_location())
            else:
                ExcelWriter.append_multi_sheet_wb(result, v.get_excel_file(), v.get_new_save_location())
    except (TypeError, AttributeError):
        print("App closed!")
        exit()

    print("Your Excel file is saved successfully")
    v = ExitView()
    v.create_exit_view(run)
    v.run_exit_view()


if __name__ == '__main__':
    run()
