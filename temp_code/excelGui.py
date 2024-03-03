from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from PIL import ImageTk, Image

root = Tk()
root.title("OCR To Excel")
root.geometry("600x725")


def open():
    global my_image
    global my_image_label
    root.filename = filedialog.askopenfilename(title="Select a File", filetypes=(
    ("jpg files", ".jpg"), ("excel files", ".xlsx"), ("all files", ".*")))
    path_label = Label(root, text=root.filename, borderwidth=2, relief="solid",anchor="w").grid(row=7, column=0, columnspan=2,
                                                                                      padx=5, sticky="ew")

primary_heading = Label(root, text="Excel Setting", anchor=E).grid(row=0, column=0, sticky="w",pady=5)

separator1 = ttk.Separator(root, orient="horizontal")
separator1.grid(row=1, column=0, sticky="ew", columnspan=2 ,pady=5)

label2 = Label(root, text="Data Extracted Successfully!!!", anchor=E).grid(row=2, column=0, sticky="w")

label3 = Label(root, text="How Would you like to save it", anchor=E).grid(row=3, column=0, sticky="w")

#radioButtons=>
selection = StringVar()

rad_btn1 = Radiobutton(root, text="Save to new file", variable=selection, value="fd")
rad_btn1.grid(row=4, column=0, sticky="w",padx=5)
rad_btn2 = Radiobutton(root, text="Add Data to existing file", variable=selection, value="er").grid(row=5, column=0, sticky="w",padx=5)

rad_btn1.select()
#if rad_btn1 is clicked
# label_saving_format =Label(root, text="Select Saving Format", anchor=E).grid(row=6, column=0, sticky="w")
#
# selection = StringVar()
#
# rad_btn_1 = Radiobutton(root, text="Single Sheet(for mass evaluation)", variable=selection, value="fd")
# rad_btn_1.grid(row=7, column=0, sticky="w",padx=5)
# rad_btn_2 = Radiobutton(root, text="Multiple Sheet(Cleaner format for user view)", variable=selection, value="er").grid(row=7, column=1, sticky="w",padx=5)
# rad_btn_1.select()
#
# label_enter_filename =Label(root, text="Select Saving Format", anchor=E).grid(row=8, column=0, sticky="w")
# entry_filename = Entry(root, width=50, borderwidth=5).grid(row=9, column=0, sticky="w",padx=5, columnspan=2)
#
# label_select_save_location =Label(root, text="Select Save Location", anchor=E).grid(row=10, column=0, sticky="w")
# button_browse_folder = Button(root, text="Browse Folder", command=open, borderwidth=5, activebackground="lightgreen").grid(
#     row=10, column=1, padx=5, pady=5)

#if rad_btn2 is clicked

label_select_file_to_add_data =Label(root, text="Select File To Add Data", anchor=E).grid(row=6, column=0, sticky="w")

choose_file_button = Button(root, text="Choose File", command=open, borderwidth=5, activebackground="lightgreen").grid(row=6, column=1, padx=5, pady=5)
root.filename = ""
path_label = Label(root, text=root.filename, borderwidth=2, relief="solid",anchor="w").grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

label_specify_new_save_location =Label(root, text="Specify New Save Location(optional)", anchor=E).grid(row=8, column=0, sticky="w")
button_browse_folder = Button(root, text="Browse Folder", command=open, borderwidth=5, activebackground="lightgreen").grid(row=8, column=1, padx=5, pady=5)

root.filename = ""
path_label = Label(root, text=root.filename, borderwidth=2, relief="solid",anchor="w").grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="ew")


root.mainloop()