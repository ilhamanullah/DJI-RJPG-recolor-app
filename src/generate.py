import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import recolor as re

def select_input_file():
    input_path.set(filedialog.askopenfilename(title="Select input file"))

def select_output_folder():
    output_path.set(filedialog.askdirectory(title="Select output folder"))

def generate():
    input_file = input_path.get()
    output_folder = output_path.get()
    if input_file and output_folder:
        messagebox.showinfo("Paths", f"Input File: {input_file}\nOutput Folder: {output_folder}")
        re.detect_and_replace_red(input_file, output_folder)
    else:
        messagebox.showwarning("Missing Information", "Please select both input file and output folder.")

root = tk.Tk()
root.title("Simple GUI")

input_path = tk.StringVar()
output_path = tk.StringVar()

tk.Label(root, text="Input Picture Path:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Output Folder Path:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_path, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Generate!", command=generate).grid(row=2, columnspan=3, pady=20)


root.mainloop()
