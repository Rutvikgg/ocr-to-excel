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
        self.root = Tk()
        self.filename = c.IMAGE_PATH_PLACEHOLDER
        self.image = ImageTk.PhotoImage(Image.open("frontend/images/image_placeholder.jpg"))
        self.radio_selection = StringVar()
        self.warning_label = None
        self.radio_seperator = None
        self.start_btn = None
        self.radio_btn_3 = None
        self.radio_btn_2 = None
        self.radio_btn_1 = None
        self.description_label = None
        self.specify_label = None
        self.image_label_seperator = None
        self.choose_file_label_seperator = None
        self.choose_file_label = None
        self.path_label = None
        self.image_label = None
        self.inner_frame = None
        self.frame = None
        self.choose_file_btn = None
        self.heading_seperator = None
        self.primary_heading = None

    def create_main_view(self) -> None:
        # Basic definitions of gui window
        self.root.title(c.OCR_TITLE)
        self.root.geometry(c.MAIN_WINDOW_SIZE)

        # Main Heading
        self.primary_heading = Label(self.root, text=c.PRIMARY_HEADING, padx=10, pady=5, anchor=E)
        self.primary_heading.grid(row=0, column=0, sticky="w")

        self.heading_seperator = ttk.Separator(self.root, orient="horizontal")
        self.heading_seperator.grid(row=1, column=0, sticky="ew", columnspan=3)

        # Choose File
        self.choose_file_label = Label(self.root, text=c.CHOOSE_LABEL_TEXT, padx=10, pady=5)
        self.choose_file_label.grid(row=2, column=0, sticky="w")
        
        self.choose_file_label_seperator = ttk.Separator(self.root, orient="horizontal")
        self.choose_file_label_seperator.grid(row=4, column=0, sticky="ew", columnspan=3)

        self.choose_file_btn = Button(self.root, text=c.CHOOSE_BTN_TEXT, command=self.open_file, borderwidth=5,
                                      activebackground="lightgreen")
        self.choose_file_btn.grid(row=2, column=1, padx=5, pady=5)

        # Image Preview
        self.frame = LabelFrame(self.root, bg=c.IMAGE_FRAME_COLOR, padx=10, pady=10, borderwidth=5)
        self.frame.grid(row=5, column=0, columnspan=3)
        self.inner_frame = LabelFrame(self.frame, bg=c.IMAGE_FRAME_COLOR, borderwidth=1)
        self.inner_frame.grid(row=2, column=0, columnspan=3)
        self.path_label = Label(self.frame, text=self.filename, borderwidth=2, relief="solid", anchor="w")
        self.path_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.image_label = Label(self.inner_frame, image=self.image)
        self.image_label.grid(row=0, column=0)
        
        self.image_label_seperator = ttk.Separator(self.root, orient="horizontal")
        self.image_label_seperator.grid(row=6, column=0, sticky="ew", columnspan=3)

        # Radio Selection
        self.specify_label = Label(self.root, text=c.SPECIFY_LABEL_TEXT)
        self.specify_label.grid(row=7, column=0, sticky="w")

        self.description_label = Label(self.root, text=c.RADIO_DESCRIPTION_TEXT)
        self.description_label.grid(row=8, column=0)

        self.radio_btn_1 = Radiobutton(self.root, text=c.RADIO_BTN_1_TEXT, variable=self.radio_selection, value="fd")
        self.radio_btn_1.grid(row=9, column=0, sticky="w")
        self.radio_btn_2 = Radiobutton(self.root, text=c.RADIO_BTN_2_TEXT, variable=self.radio_selection, value="er")
        self.radio_btn_2.grid(row=9, column=1)
        self.radio_btn_3 = Radiobutton(self.root, text=c.RADIO_BTN_3_TEXT, variable=self.radio_selection, value="in")
        self.radio_btn_3.grid(row=9, column=2)
        self.radio_btn_1.select()

        self.radio_seperator = ttk.Separator(self.root, orient="horizontal")
        self.radio_seperator.grid(row=10, column=0, sticky="ew", columnspan=3)

        # Start Button
        self.start_btn = Button(self.root, text="Start Conversion", borderwidth=5, activebackground="lightgreen", command=self.start_conversion)
        self.start_btn.grid(row=11, column=2, columnspan=1, sticky="e", padx=10, pady=10)

        self.warning_label = Label(self.root, text="", fg=c.WARNING_TEXT_COLOR)
        self.warning_label.grid(row=12, column=0, columnspan=3)

    def run_main_view(self) -> None:
        self.root.mainloop()

    def open_file(self) -> None:
        # Resets Warning label if it is displayed
        self.warning_label.config(text="")

        # File open and preview operation
        self.filename = filedialog.askopenfilename(title=c.CHOOSE_FILE_DIALOG_TEXT)
        if self.filename.lower().endswith(".pdf"):
            pdf_document = fitz.open(self.filename)
            page = pdf_document.load_page(0)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            self.image = ImageTk.PhotoImage(img.resize(c.IMAGE_SIZE))
        else:
            img = Image.open(self.filename)
            self.image = ImageTk.PhotoImage(img.resize(c.IMAGE_SIZE))
        self.path_label.config(text=self.filename)
        self.image_label.config(image=self.image)

    def get_radio_selection(self) -> str:
        return self.radio_selection.get()

    def get_filename(self) -> str:
        return self.filename

    def start_conversion(self) -> None:
        # Check to determine if a file is chosen
        if self.filename == c.IMAGE_PATH_PLACEHOLDER:
            self.warning_label.config(text=c.WARNING_TEXT)
        else:
            self.root.quit()
