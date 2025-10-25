# Library Import
import os
import shutil
import customtkinter
import tkinter as tk
from tkinter import filedialog

# Setting up window utama
root = customtkinter.CTk()

customtkinter.set_appearance_mode("reddish")
customtkinter.set_default_color_theme("dark-blue")

# Setting Icon , Title, Geometri
root.iconbitmap("organize.ico")
root.title("File Organizer")
root.geometry("400x260")
label = customtkinter.CTkLabel(
    root, text="File Organizer", font=("Times New Roman", 24))
label.pack(pady=20, padx=10)  # label diatas tombol

frame = customtkinter.CTkFrame(root)
frame.pack(pady=0, padx=0, fill="y", expand=True)

# Funcuion FileDialog


def openFile():
    filepath = filedialog.askdirectory(title="Pilih Path")
    if filepath:
        entry1.delete(0, tk.END)
        entry1.insert(0, filepath)
        print(filepath)
        output_var.set("Path Selected")
    else:
        output_var.set("No Folder Selected")


# FileDialog
button = customtkinter.CTkButton(
    master=frame, text="dir    ", command=openFile)
button.pack(pady=10)

# Button1 Button2
entry1 = customtkinter.CTkEntry(frame, placeholder_text="Masukkan Path", font=(
    "Times New Roman", 14))  # entry untuk path
entry1.pack(pady=12, padx=10)

output_var = tk.StringVar()  # variabel untuk menyimpan output

entry2 = customtkinter.CTkEntry(
    master=frame, textvariable=output_var, state="readonly", font=("Times New Roman", 14)
)
entry2.pack(pady=12, padx=10)
output_var.set("Not Organized Yet")

# Fungsi untuk merapihkan file


def rapihkan(event=None):  # event = none biar bisa di panggil di bind [ENTER]
    path = entry1.get().strip()  # ambil path dari entry
    files = os.listdir(path)
    if not os.path.exists(path):
        entry2.delete(0, customtkinter.END)
        entry2.insert(0, "Invalid Path")
        return

    files = os.listdir(path)
    if not files:
        entry2.delete(0, customtkinter.END)
        entry2.insert(0, "No Files Found")
        return

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]
        if os.path.exists(path + '/' + extension):
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
        else:
            os.makedirs(path + '/' + extension)
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            label.configure(text="Berhasil di rapihkan")
            output_var.set("Organized Succesfully")


button = customtkinter.CTkButton(
    frame, text="Rapihkan", command=rapihkan)
button.pack(pady=12, padx=10)
# Fungsi untuk enter key
entry1.bind("<Return>", rapihkan)  # bind enter key ke fungsi rapihkan


root.mainloop()
