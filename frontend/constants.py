"""
Constants for use in MainView
"""

# UI scale
MAIN_WINDOW_SIZE: str = "600x725"
EXCEL_WINDOW_SIZE: str = "600x600"
EXIT_WINDOW_SIZE: str = "320x75"
IMAGE_SIZE: tuple[int, int] = (500, 400)

# colors
IMAGE_FRAME_COLOR: str = "#88D4AB"
WARNING_TEXT_COLOR: str = "#FF0F0F"
BTN_ACTIVE_BG_COLOR: str = "lightgreen"

OCR_TITLE: str = "Ocr to Excel"

# String used in Main GUI
MAIN_UI_PRIMARY_HEADING: str = "OCR Your Document"
CHOOSE_BTN_TEXT: str = "Choose File"
IMAGE_PATH_PLACEHOLDER: str = "Image Path"
CHOOSE_FILE_DIALOG_TEXT: str = "Select your file"
DOCUMENT_CHOOSE_LABEL_TEXT: str = "Choose Your File"
SPECIFY_LABEL_TEXT: str = "Specify Document Type"
DOCUMENT_RADIO_DESCRIPTION_TEXT: str = "Specifying the document leads to better result and extraction of data"
FD_RADIO_BTN_TEXT: str = "Default (Any Financial Document)"
ER_RADIO_BTN_TEXT: str = "Expense Receipt"
IN_RADIO_BTN_TEXT: str = "Invoice"
START_BTN_TEXT: str = "Start Conversion"
MAIN_UI_WARNING_TEXT: str = "Please choose a file before proceeding!"

# String used in Excel GUI
EXCEL_UI_PRIMARY_HEADING: str = "Excel Setting"
EXCEL_SUCCESS_MSG_TEXT: str = "Data Extracted Successfully!!!"
SAVE_OPTION_TEXT: str = "How Would you like to save it"
SAVE_NEW_RADIO_BTN_TEXT: str = "Save to new file"
APPEND_RADIO_BTN_TEXT: str = "Add Data to existing file"
SAVING_FORMAT_TEXT: str = "Select Saving Format"
SINGLE_SHEET_RADIO_BTN_TEXT: str = "Single Sheet (for mass data entry.)"
MULTI_SHEET_RADIO_BTN_TEXT: str = "Multiple Sheet (Cleaner format for user view)"
SAVE_FILENAME_TEXT: str = "Enter your File Name"
SELECT_SAVE_LOCATION_TEXT: str = "Select Save Location"
SELECT_SAVE_LOCATION_OPTIONAL_TEXT: str = "Select Save Location (optional)"
BROWSE_FOLDER_BTN_TEXT: str = "Browse Folder"
SAVE_BTN_TEXT: str = "Save"
SELECT_FILE_TO_APPEND_BTN_TEXT: str = "Select File To Add Data"
EXCEL_UI_SAVE_FILENAME_WARNING_TEXT: str = "Please enter your filename before proceeding."
EXCEL_UI_SAVE_FORMAT_WARNING_TEXT: str = "Please select a Saving Format to proceed!"
EXCEL_UI_APPEND_FILE_WARNING_TEXT: str = "Please select a excel file to append into."
EXCEL_UI_SAVE_OPTION_WARNING_TEXT: str = "Please select a Save option to proceed!"

# String used in Exit GUI
EXIT_UI_PRIMARY_HEADING: str = "Your Data is Converted into Excel Successfully!"
SCAN_MORE_BTN_TEXT: str = "Scan more..."
EXIT_BTN_TEXT: str = "Exit"
