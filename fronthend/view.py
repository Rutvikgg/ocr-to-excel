"""
This is where we implement our UI using tkinter
This file has the View class
"""
import time
from tkinter import Tk, Label, ttk, Button, filedialog
from tkinter.constants import E

import constants as c


class View:
    def __init__(self):
        self.root = Tk()
        self.filename = None

    def create_main_view(self):
        self.root.title(c.OCR_TITLE)
        primary_heading = Label(self.root, text=c.PRIMARY_HEADING, pady=5, anchor=E)
        heading_seperator = ttk.Separator(self.root, orient="horizontal")
        choose_file_btn = Button(self.root, text=c.CHOOSE_BTN_TEXT, command=self.open_file, borderwidth=5, activebackground="lightgreen")

        primary_heading.grid(row=0, column=0, sticky="w")
        heading_seperator.grid(row=1, column=0, sticky="ew", columnspan=3)
        choose_file_btn.grid(row=2, column=1, padx=5, pady=5)

    def run_main_view(self):
        self.root.mainloop()

    def open_file(self):
        self.filename = filedialog.askopenfilename(title=c.CHOOSE_FILE_DIALOG_TEXT)
        print(self.filename)


v = View()
v.create_main_view()
v.run_main_view()
