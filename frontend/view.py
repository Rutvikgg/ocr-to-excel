"""
This is where we implement our UI using tkinter
This file has the MainView class
"""
import os
from pathlib import Path
from tkinter import Tk, Label, ttk, Button, filedialog, LabelFrame, StringVar, Radiobutton, IntVar, Entry, Frame
from tkinter.constants import E, W

from PIL import Image, ImageTk
from fitz import fitz

import frontend.constants as c


class MainView:
    def __init__(self) -> None:
        # Components of Main GUI
        self.main_ui_root = Tk()
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
        self.main_ui_primary_heading = Label(self.main_ui_root, text=c.MAIN_UI_PRIMARY_HEADING, padx=10, pady=5,
                                             anchor=E)
        self.main_ui_primary_heading.grid(row=0, column=0, sticky="w")

        self.main_ui_heading_seperator = ttk.Separator(self.main_ui_root, orient="horizontal")
        self.main_ui_heading_seperator.grid(row=1, column=0, sticky="ew", columnspan=3)

        # Choose File
        self.document_choose_file_label = Label(self.main_ui_root, text=c.DOCUMENT_CHOOSE_LABEL_TEXT, padx=10, pady=5)
        self.document_choose_file_label.grid(row=2, column=0, sticky="w")

        self.document_choose_file_label_seperator = ttk.Separator(self.main_ui_root, orient="horizontal")
        self.document_choose_file_label_seperator.grid(row=4, column=0, sticky="ew", columnspan=3)

        self.document_choose_file_btn = Button(self.main_ui_root, text=c.DOCUMENT_CHOOSE_BTN_TEXT,
                                               command=self.open_file_for_ocr, borderwidth=5,
                                               activebackground="lightgreen")
        self.document_choose_file_btn.grid(row=2, column=1, padx=5, pady=5)

        # Image Preview
        self.image_preview_frame = LabelFrame(self.main_ui_root, bg=c.IMAGE_FRAME_COLOR, padx=10, pady=10,
                                              borderwidth=5)
        self.image_preview_frame.grid(row=5, column=0, columnspan=3)
        self.image_preview_inner_frame = LabelFrame(self.image_preview_frame, bg=c.IMAGE_FRAME_COLOR, borderwidth=1)
        self.image_preview_inner_frame.grid(row=2, column=0, columnspan=3)
        self.image_preview_path_label = Label(self.image_preview_frame, text=self.file_for_ocr, borderwidth=2,
                                              relief="solid", anchor="w")
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

        self.fd_radio_btn = Radiobutton(self.main_ui_root, text=c.FD_RADIO_BTN_TEXT,
                                        variable=self.document_radio_selection, value="fd")
        self.fd_radio_btn.grid(row=9, column=0, sticky="w")
        self.er_radio_btn = Radiobutton(self.main_ui_root, text=c.ER_RADIO_BTN_TEXT,
                                        variable=self.document_radio_selection, value="er")
        self.er_radio_btn.grid(row=9, column=1)
        self.in_radio_btn = Radiobutton(self.main_ui_root, text=c.IN_RADIO_BTN_TEXT,
                                        variable=self.document_radio_selection, value="in")
        self.in_radio_btn.grid(row=9, column=2)
        self.fd_radio_btn.select()

        self.document_radio_seperator = ttk.Separator(self.main_ui_root, orient="horizontal")
        self.document_radio_seperator.grid(row=10, column=0, sticky="ew", columnspan=3)

        # Start Button
        self.start_btn = Button(self.main_ui_root, text="Start Conversion", borderwidth=5,
                                activebackground="lightgreen", command=self.start_conversion)
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
            self.main_ui_root.destroy()  # Close the GUI


class ExcelView:
    def __init__(self):
        self.excel_ui_root = Tk()
        self.save_option_selection = IntVar()
        self.sheet_selection = IntVar()
        self.append_option_frame = None
        self.save_new_option_frame = None
        self.excel_primary_heading = None
        self.excel_primary_heading_seperator = None
        self.success_msg_label = None
        self.save_option_label = None
        self.save_new_radio_btn = None
        self.append_radio_btn = None
        self.save_filename = None
        self.saving_format_label = None
        self.single_sheet_radio_btn = None
        self.multi_sheet_radio_btn = None
        self.save_filename_label = None
        self.save_filename_field = None
        self.browse_folder_btn = None
        self.select_save_location_label = None
        self.new_save_location_path_label = None
        self.excel_file = None
        self.save_location_path_label = None
        self.file_to_append_path_label = None
        self.choose_file_to_append_btn = None
        self.select_file_to_append_label = None
        self.save_option_seperator = None
        documents_path = Path.home() / "Documents"
        self.folder_path = str(documents_path)
        self.new_folder_path = None
        self.save_btn = None
        self.excel_ui_warning_label = None

    def create_excel_view(self):
        self.excel_ui_root.title(c.OCR_TITLE)
        self.excel_ui_root.geometry(c.EXCEL_WINDOW_SIZE)

        self.excel_primary_heading = Label(self.excel_ui_root, text="Excel Setting", anchor=E)
        self.excel_primary_heading.grid(row=0, column=0, sticky="w", pady=5)

        self.excel_primary_heading_seperator = ttk.Separator(self.excel_ui_root, orient="horizontal")
        self.excel_primary_heading_seperator.grid(row=1, column=0, sticky="ew", columnspan=2, pady=5)

        self.success_msg_label = Label(self.excel_ui_root, text="Data Extracted Successfully!!!", anchor=E)
        self.success_msg_label.grid(row=2, column=0, sticky="w")

        self.save_option_label = Label(self.excel_ui_root, text="How Would you like to save it", anchor=E)
        self.save_option_label.grid(row=3, column=0, sticky="w")

        self.save_new_radio_btn = Radiobutton(self.excel_ui_root, text="Save to new file",
                                              variable=self.save_option_selection, value=1,
                                              command=self.save_option_command)
        self.save_new_radio_btn.grid(row=4, column=0, sticky="w", padx=5)
        self.append_radio_btn = Radiobutton(self.excel_ui_root, text="Add Data to existing file",
                                            variable=self.save_option_selection, value=2,
                                            command=self.save_option_command)
        self.append_radio_btn.grid(row=5, column=0, sticky="w", padx=5)

        self.save_option_seperator = ttk.Separator(self.excel_ui_root, orient="horizontal")
        self.save_option_seperator.grid(row=6, column=0, sticky="ew", columnspan=2, pady=5)

        self.excel_ui_warning_label = Label(self.excel_ui_warning_label, text="", fg=c.WARNING_TEXT_COLOR)
        self.excel_ui_warning_label.grid(row=8, column=0, columnspan=3)

        # Different GUI depending on Save option

        # Save in new file option
        self.save_new_option_frame = Frame(self.excel_ui_root)
        self.saving_format_label = Label(self.save_new_option_frame, text="Select Saving Format", anchor=E)
        self.saving_format_label.grid(row=0, column=0, sticky="w")

        self.single_sheet_radio_btn = Radiobutton(self.save_new_option_frame, text="Single Sheet(for mass evaluation)",
                                                  variable=self.sheet_selection, value=1)
        self.single_sheet_radio_btn.grid(row=1, column=0, sticky="w", padx=5)

        self.multi_sheet_radio_btn = Radiobutton(self.save_new_option_frame,
                                                 text="Multiple Sheet(Cleaner format for user view)",
                                                 variable=self.sheet_selection, value=2)
        self.multi_sheet_radio_btn.grid(row=1, column=1, sticky="w", padx=5)

        self.save_filename_label = Label(self.save_new_option_frame, text="Enter File Name", anchor=E)
        self.save_filename_label.grid(row=2, column=0, sticky="w")

        self.save_filename_field = Entry(self.save_new_option_frame, width=50, borderwidth=5)
        self.save_filename_field.grid(row=3, column=0, sticky="w", padx=5, columnspan=2)

        self.select_save_location_label = Label(self.save_new_option_frame, text="Select Save Location", anchor=E)
        self.select_save_location_label.grid(row=4, column=0, sticky="w")
        self.browse_folder_btn = Button(self.save_new_option_frame, text="Browse Folder", borderwidth=5,
                                        activebackground="lightgreen", command=self.browse_folder)
        self.browse_folder_btn.grid(row=4, column=1, padx=5, pady=5)
        self.save_location_path_label = Label(self.save_new_option_frame, text=self.folder_path, borderwidth=2,
                                              relief="solid", anchor="w")
        self.save_location_path_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.save_btn = Button(self.save_new_option_frame, text="Save", borderwidth=5,
                               activebackground="lightgreen", padx=10, command=self.save_btn_command)
        self.save_btn.grid(row=6, column=1, padx=5, pady=5, sticky="e")

        # Append to existing file option
        self.append_option_frame = Frame(self.excel_ui_root)

        self.select_file_to_append_label = Label(self.append_option_frame, text="Select File To Add Data", anchor=E)
        self.select_file_to_append_label.grid(row=0, column=0, sticky="w")

        self.choose_file_to_append_btn = Button(self.append_option_frame, text="Choose File", borderwidth=5,
                                                activebackground="lightgreen", command=self.open_excel_file)
        self.choose_file_to_append_btn.grid(row=0, column=1, padx=5, pady=5)
        self.file_to_append_path_label = Label(self.append_option_frame, borderwidth=2, relief="solid", anchor="w")
        self.file_to_append_path_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.select_save_location_label = Label(self.append_option_frame, text="Select Save Location (optional)",
                                                anchor=E)
        self.select_save_location_label.grid(row=2, column=0, sticky="w")
        self.browse_folder_btn = Button(self.append_option_frame, text="Browse Folder", borderwidth=5,
                                        activebackground="lightgreen", command=self.browse_folder)
        self.browse_folder_btn.grid(row=2, column=1, padx=5, pady=5)
        self.new_save_location_path_label = Label(self.append_option_frame, text=self.new_folder_path, borderwidth=2,
                                                  relief="solid", anchor="w")
        self.new_save_location_path_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.save_btn = Button(self.append_option_frame, text="Save", borderwidth=5,
                               activebackground="lightgreen", padx=10, command=self.save_btn_command)
        self.save_btn.grid(row=4, column=1, padx=5, pady=5, sticky="e")

    def run_excel_view(self):
        self.excel_ui_root.mainloop()

    def save_option_command(self):
        if self.get_save_option_selection() == 1:
            self.save_new_option_frame.grid(row=7, column=0, padx=10, pady=10)
            self.append_option_frame.grid_forget()
        elif self.get_save_option_selection() == 2:
            self.append_option_frame.grid(row=7, column=0, padx=10, pady=10)
            self.save_new_option_frame.grid_forget()

    def browse_folder(self):
        self.folder_path = self.new_folder_path = filedialog.askdirectory()
        if self.get_save_option_selection() == 1:
            self.save_location_path_label.config(text=self.folder_path)
        elif self.get_save_option_selection() == 2:
            self.new_save_location_path_label.config(text=self.new_folder_path)

    def open_excel_file(self):
        self.excel_file = filedialog.askopenfilename(title="Select a File",
                                                     filetypes=(("Excel files", "*.xlsx;*.xls"),))
        self.file_to_append_path_label.config(text=self.excel_file)

    def get_save_option_selection(self):
        return self.save_option_selection.get()

    def get_excel_file(self):
        return self.excel_file

    def get_sheet_selection(self):
        return self.sheet_selection.get()

    def get_save_filename(self):
        return self.save_filename.strip()

    def get_folder(self):
        return self.folder_path

    def get_new_folder(self):
        return self.new_folder_path

    def get_save_location(self):
        return f'{self.get_folder()}/{self.get_save_filename()}.xlsx'

    def get_new_save_location(self):
        if self.get_new_folder() is None:
            return None
        else:
            file_name = os.path.basename(self.get_excel_file())
            return f'{self.get_new_folder()}/{file_name}'

    def store_save_filename(self):
        self.save_filename = self.save_filename_field.get()

    def save_btn_command(self):
        self.store_save_filename()
        self.excel_ui_warning_label.config(text="")

        if self.get_save_option_selection() == 1:
            if self.get_sheet_selection() == 1 or self.get_sheet_selection() == 2:
                if self.get_save_filename().strip():
                    self.excel_ui_root.destroy()
                else:
                    self.excel_ui_warning_label.config(text="Please enter your filename before proceeding.")
            else:
                self.excel_ui_warning_label.config(text="Please select a Saving Format to proceed!")
        elif self.get_save_option_selection() == 2:
            if self.get_excel_file() is None:
                self.excel_ui_warning_label.config(text="Please select a excel file to append into.")
            else:
                self.excel_ui_root.destroy()
        else:
            self.excel_ui_warning_label.config(text="Please select a Save option to proceed!")
