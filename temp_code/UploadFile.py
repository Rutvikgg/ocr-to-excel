"""
This is where we implement our UI using tkinter
This file has the MainView class
"""

import tkinter as tk
from tkinter import filedialog

class UploadFile:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice Data Extraction into Excel Using OCR")
        self.root.geometry("700x400")

        # Variable to store file location
        self.file_location_var = tk.StringVar()

        # Label to display file manager location
        file_location_label = tk.Label(root, textvariable=self.file_location_var, wraplength=300, bg="lightgrey")
        file_location_label.pack(pady=10)

        # Button to open file manager
        click_me_button = tk.Button(root, text="Upload File", command=self.open_file_manager, bg="blue", fg="white")
        click_me_button.pack(pady=10)

    def open_file_manager(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select File")
        self.file_location_var.set(file_path)

        # Replace with your actual backend logic, handling potential errors
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    # Replace with more elaborate file processing/backend logic
                    pass
            except FileNotFoundError:
                print("Error: File not found!")
            except PermissionError:
                print("Error: Insufficient permissions to read the file!")
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UploadFile(root)
    root.mainloop()

