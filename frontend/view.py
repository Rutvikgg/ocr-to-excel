"""
This is where we implement our UI using tkinter
This file has the View class
"""
from tkinter import Tk, Label, ttk, Button, filedialog, LabelFrame, StringVar, Radiobutton
from tkinter.constants import E

from PIL import Image, ImageTk
from fitz import fitz

import frontend.constants as c


class View:
    def __init__(self) -> None:
        self.main_ui_root = Tk()
        self.excel_ui_root = Tk()
        self.file_for_ocr = c.IMAGE_PATH_PLACEHOLDER
        self.image = ImageTk.PhotoImage(Image.open("frontend/images/image_placeholder.jpg"))
        self.document_radio_selection = StringVar()
        self.main_ui_warning_label = None
        self.document_radio_seperator = None
        self.start_btn = None
        self.in_radio_btn = None
        self.er_radio_btn = None
        self.fd_radio_btn = None
        self.document_description_label = None
        self.specify_document_label = None
        self.image_preview_seperator = None
        self.document_choose_file_label_seperator = None
        self.document_choose_file_label = None
        self.image_preview_path_label = None
        self.image_preview = None
        self.image_preview_inner_frame = None
        self.image_preview_frame = None
        self.document_choose_file_btn = None
        self.main_ui_heading_seperator = None
        self.main_ui_primary_heading = None

    def create_main_view(self) -> None:
        # Basic definitions of gui window
        self.main_ui_root.title(c.OCR_TITLE)
        self.main_ui_root.geometry(c.MAIN_WINDOW_SIZE)

        # Main Heading
        self.main_ui_primary_heading = Label(self.main_ui_root, text=c.MAIN_UI_PRIMARY_HEADING, padx=10, pady=5, anchor=E)
        self.main_ui_primary_heading.grid(row=0, column=0, sticky="w")

        self.main_ui_heading_seperator = ttk.Separator(self.main_ui_root, orient="horizontal")
        self.main_ui_heading_seperator.grid(row=1, column=0, sticky="ew", columnspan=3)

        # Choose File
        self.document_choose_file_label = Label(self.main_ui_root, text=c.DOCUMENT_CHOOSE_LABEL_TEXT, padx=10, pady=5)
        self.document_choose_file_label.grid(row=2, column=0, sticky="w")
        
        self.document_choose_file_label_seperator = ttk.Separator(self.main_ui_root, orient="horizontal")
        self.document_choose_file_label_seperator.grid(row=4, column=0, sticky="ew", columnspan=3)

        self.document_choose_file_btn = Button(self.main_ui_root, text=c.DOCUMENT_CHOOSE_BTN_TEXT, command=self.open_file_for_ocr, borderwidth=5,
                                               activebackground="lightgreen")
        self.document_choose_file_btn.grid(row=2, column=1, padx=5, pady=5)

        # Image Preview
        self.image_preview_frame = LabelFrame(self.main_ui_root, bg=c.IMAGE_FRAME_COLOR, padx=10, pady=10, borderwidth=5)
        self.image_preview_frame.grid(row=5, column=0, columnspan=3)
        self.image_preview_inner_frame = LabelFrame(self.image_preview_frame, bg=c.IMAGE_FRAME_COLOR, borderwidth=1)
        self.image_preview_inner_frame.grid(row=2, column=0, columnspan=3)
        self.image_preview_path_label = Label(self.image_preview_frame, text=self.file_for_ocr, borderwidth=2, relief="solid", anchor="w")
        self.image_preview_path_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.image_preview = Label(self.image_preview_inner_frame, image=self.image)
        self.image_preview.grid(row=0, column=0)
        
        self.image_preview_seperator = ttk.Separator(self.main_ui_root, orient="horizontal")
        self.image_preview_seperator.grid(row=6, column=0, sticky="ew", columnspan=3)

        # Radio Selection
        self.specify_document_label = Label(self.main_ui_root, text=c.SPECIFY_LABEL_TEXT)
        self.specify_document_label.grid(row=7, column=0, sticky="w")

        self.document_description_label = Label(self.main_ui_root, text=c.DOCUMENT_RADIO_DESCRIPTION_TEXT)
        self.document_description_label.grid(row=8, column=0)

        self.fd_radio_btn = Radiobutton(self.main_ui_root, text=c.FD_RADIO_BTN_TEXT, variable=self.document_radio_selection, value="fd")
        self.fd_radio_btn.grid(row=9, column=0, sticky="w")
        self.er_radio_btn = Radiobutton(self.main_ui_root, text=c.ER_RADIO_BTN_TEXT, variable=self.document_radio_selection, value="er")
        self.er_radio_btn.grid(row=9, column=1)
        self.in_radio_btn = Radiobutton(self.main_ui_root, text=c.IN_RADIO_BTN_TEXT, variable=self.document_radio_selection, value="in")
        self.in_radio_btn.grid(row=9, column=2)
        self.fd_radio_btn.select()

        self.document_radio_seperator = ttk.Separator(self.main_ui_root, orient="horizontal")
        self.document_radio_seperator.grid(row=10, column=0, sticky="ew", columnspan=3)

        # Start Button
        self.start_btn = Button(self.main_ui_root, text="Start Conversion", borderwidth=5, activebackground="lightgreen", command=self.start_conversion)
        self.start_btn.grid(row=11, column=2, columnspan=1, sticky="e", padx=10, pady=10)

        self.main_ui_warning_label = Label(self.main_ui_root, text="", fg=c.WARNING_TEXT_COLOR)
        self.main_ui_warning_label.grid(row=12, column=0, columnspan=3)

    def run_main_view(self) -> None:
        self.main_ui_root.mainloop()

    def open_file_for_ocr(self) -> None:
        # Resets Warning label if it is displayed
        self.main_ui_warning_label.config(text="")

        # File open and preview operation
        self.file_for_ocr = filedialog.askopenfilename(title=c.DOCUMENT_CHOOSE_FILE_DIALOG_TEXT)
        if self.file_for_ocr.lower().endswith(".pdf"):
            pdf_document = fitz.open(self.file_for_ocr)
            page = pdf_document.load_page(0)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            self.image = ImageTk.PhotoImage(img.resize(c.IMAGE_SIZE))
        else:
            img = Image.open(self.file_for_ocr)
            self.image = ImageTk.PhotoImage(img.resize(c.IMAGE_SIZE))
        self.image_preview_path_label.config(text=self.file_for_ocr)
        self.image_preview.config(image=self.image)

    def get_document_radio_selection(self) -> str:
        return self.document_radio_selection.get()

    def get_file_for_ocr(self) -> str:
        return self.file_for_ocr

    def start_conversion(self) -> None:
        # Check to determine if a file is chosen
        if self.file_for_ocr == c.IMAGE_PATH_PLACEHOLDER:
            self.main_ui_warning_label.config(text=c.MAIN_UI_WARNING_TEXT)
        else:
            self.main_ui_root.quit()     # Close the GUI

    def create_excel_view(self):
        pass

    def run_excel_view(self):
        pass

