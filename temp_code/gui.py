from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from PIL import ImageTk, Image

root = Tk()
root.title("OCR To Excel")
root.geometry("600x725")

root.iconbitmap("../frontend/images/exit_ui_logo.ico")
def open():
    global my_image
    global my_image_label
    root.filename = filedialog.askopenfilename(title="Select a File", filetypes=(
    ("jpg files", ".jpg"), ("png files", ".png"), ("all files", ".*")))
    path_label = Label(frame, text=root.filename, borderwidth=2, relief="solid",anchor="w").grid(row=0, column=0, columnspan=2,
                                                                                      padx=5, pady=5, sticky="ew")
    #size_of_image will be 500x400
    img = Image.open(root.filename)
    my_image = ImageTk.PhotoImage(img.resize((500, 400)))
    # my_image = ImageTk.PhotoImage(img)
    my_image_label = Label(inner_frame, image=my_image).grid(row=0, column=0)


primary_heading = Label(root, text="OCR Your Document", anchor=E).grid(row=0, column=0, sticky="w")

separator1 = ttk.Separator(root, orient="horizontal")
separator1.grid(row=1, column=0, sticky="ew", columnspan=3)

# def open() for choose_file
choose_file_button = Button(root, text="Choose File", command=open, borderwidth=5, activebackground="lightgreen").grid(
    row=2, column=1, padx=5, pady=5)
root.filename = " Image path "

upload_label = Label(root, text="Upload Your File", pady=10).grid(row=2, column=0, sticky="w")

separator2 = ttk.Separator(root, orient="horizontal")
separator2.grid(row=4, column=0, sticky="ew", columnspan=3)

frame = LabelFrame(root, bg="#88d4ab", padx=10, pady=10, borderwidth=5)
frame.grid(row=5, column=0, columnspan=3)

path_label = Label(frame, text=root.filename, borderwidth=2, relief="solid",anchor="w").grid(row=0, column=0, columnspan=3, padx=5,
                                                                                  pady=5, sticky="ew")

separator_frame = ttk.Separator(frame, orient="horizontal")
separator_frame.grid(row=1, column=0, sticky="ew", columnspan=3, pady=10)

inner_frame = LabelFrame(frame, bg="#88d4ab", borderwidth=1)
inner_frame.grid(row=2, column=0, columnspan=3)

# my_button=Button(image_preview_frame,text="Open file").grid(row=0,column=0, pady=10)

separator3 = ttk.Separator(root, orient="horizontal")
separator3.grid(row=6, column=0, sticky="ew", columnspan=3)

specify_label = Label(root, text="Specify Document Type").grid(row=7, column=0, sticky="w")

description_label = Label(root, text="Specifying the document leads to better result and extraction of data").grid(
    row=8, column=0)

#radioButtons=>
selection = StringVar()

rad_btn1 = Radiobutton(root, text="Default(Any Financial Document)", variable=selection, value="fd")
rad_btn1.grid(row=9, column=0, sticky="w")
rad_btn2 = Radiobutton(root, text="Expense Receipt", variable=selection, value="er").grid(row=9, column=1)
rad_btn3 = Radiobutton(root, text="Invoice", variable=selection, value="in").grid(row=9, column=2)

rad_btn1.select()

#Buttons=>(Back & Start)
back_btn = Button(root, text="Back").grid(row=10, column=0, columnspan=1, sticky="w", padx=10, pady=10)
start_btn1 = Button(root, text="Start Conversion").grid(row=10, column=2, columnspan=1, sticky="e",padx=10, pady=10)

root.mainloop()
