from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from PIL import ImageTk,Image

root=Tk()
root.title("OCR To Excel")
# root.iconbitmap("")
def open():
    pass

primary_heading=Label(root, text="OCR Your Document",pady=5, anchor=E).grid(row=0,column=0)



separator1 = ttk.Separator(root, orient="horizontal")
separator1.grid(row=1,column=0,sticky="ew",columnspan=2)

# def open() for choose_file
choose_file_button=Button(root, text="Choose File",command=open, borderwidth=5,activebackground="lightgreen").grid(row=2,column=1,padx=5,pady=5)
root.filename=filedialog.askopenfile(title="Choose File",filetypes=(("jpg files",".jpg"),("png files",".png"),("all files",".*")))

upload_label=Label(root, text="Upload Your File",pady=10).grid(row=2,column=0)

path_label=Label(root,text=root.filename,borderwidth=2,relief="solid").grid(row=3,column=0,columnspan=2,padx=5,pady=5)

separator2 = ttk.Separator(root, orient="horizontal")
separator2.grid(row=4,column=0,sticky="ew",columnspan=2)

frame = LabelFrame(root,bg="#88d4ab", padx=10,pady=10,borderwidth=5)
frame.grid(row=5,column=0,padx=25,pady=25, columnspan=3)

my_button=Button(frame,text="Open file").grid(row=0,column=0, pady=10)

back_btn=Button(root,text="Back").grid(row=6,column=0, columnspan=1,sticky="w",padx=10)
back_btn1=Button(root,text="Start Conversion").grid(row=6,column=1, columnspan=1,sticky="e")

root.mainloop()
