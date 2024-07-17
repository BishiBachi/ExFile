import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Function to categorize files
def categorize_files(path, folder_names):
    try:
        file_names = os.listdir(path)
        total_files = len(file_names)
        progress_bar['maximum'] = total_files

        for folder in folder_names.values():
            if not os.path.exists(os.path.join(path, folder)):
                os.makedirs(os.path.join(path, folder))

        for index, file in enumerate(file_names):
            if file.endswith(".csv"):
                shutil.move(os.path.join(path, file), os.path.join(path, folder_names['csv'], file))
                log_listbox.insert(tk.END, f"Moved {file} to {folder_names['csv']}")
            elif file.endswith(".png"):
                shutil.move(os.path.join(path, file), os.path.join(path, folder_names['image'], file))
                log_listbox.insert(tk.END, f"Moved {file} to {folder_names['image']}")
            elif file.endswith(".txt"):
                shutil.move(os.path.join(path, file), os.path.join(path, folder_names['text'], file))
                log_listbox.insert(tk.END, f"Moved {file} to {folder_names['text']}")
            elif file.endswith(".pdf"):
                shutil.move(os.path.join(path, file), os.path.join(path, folder_names['pdf'], file))
                log_listbox.insert(tk.END, f"Moved {file} to {folder_names['pdf']}")
            progress_bar['value'] = index + 1
            root.update_idletasks()

        messagebox.showinfo("Success", "Files have been categorized successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to select folder
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder_selected)

# Function to start categorization
def start_categorization():
    folder_names = {
        'csv': csv_entry.get(),
        'image': image_entry.get(),
        'text': text_entry.get(),
        'pdf': pdf_entry.get()
    }
    path = path_entry.get()
    if os.path.exists(path):
        log_listbox.delete(0, tk.END)
        categorize_files(path, folder_names)
    else:
        messagebox.showerror("Error", "The selected path does not exist.")

# Main GUI window
root = tk.Tk()
root.title("File Management Program")
root.geometry("600x450")

# Folder Selection
path_label = tk.Label(root, text="Select a folder to organize:")
path_label.pack(pady=5)

path_frame = tk.Frame(root)
path_frame.pack(pady=5)

path_entry = tk.Entry(path_frame, width=50)
path_entry.pack(side=tk.LEFT, padx=5)

path_button = tk.Button(path_frame, text="Browse", command=select_folder)
path_button.pack(side=tk.LEFT)

# Folder Name Customization
custom_label = tk.Label(root, text="Customize Folder Names:")
custom_label.pack(pady=10)

csv_frame = tk.Frame(root)
csv_frame.pack(pady=5)

csv_label = tk.Label(csv_frame, text="CSV Files Folder:")
csv_label.pack(side=tk.LEFT, padx=5)
csv_entry = tk.Entry(csv_frame, width=30)
csv_entry.insert(0, "csv files")
csv_entry.pack(side=tk.LEFT, padx=5)

image_frame = tk.Frame(root)
image_frame.pack(pady=5)

image_label = tk.Label(image_frame, text="Image Files Folder:")
image_label.pack(side=tk.LEFT, padx=5)
image_entry = tk.Entry(image_frame, width=30)
image_entry.insert(0, "image files")
image_entry.pack(side=tk.LEFT, padx=5)

text_frame = tk.Frame(root)
text_frame.pack(pady=5)

text_label = tk.Label(text_frame, text="Text Files Folder:")
text_label.pack(side=tk.LEFT, padx=5)
text_entry = tk.Entry(text_frame, width=30)
text_entry.insert(0, "text files")
text_entry.pack(side=tk.LEFT, padx=5)

pdf_frame = tk.Frame(root)
pdf_frame.pack(pady=5)

pdf_label = tk.Label(pdf_frame, text="PDF Files Folder:")
pdf_label.pack(side=tk.LEFT, padx=5)
pdf_entry = tk.Entry(pdf_frame, width=30)
pdf_entry.insert(0, "pdf files")
pdf_entry.pack(side=tk.LEFT, padx=5)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

# Log Display
log_label = tk.Label(root, text="Log:")
log_label.pack(pady=5)

log_frame = tk.Frame(root)
log_frame.pack(pady=5)

log_scrollbar = tk.Scrollbar(log_frame)
log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

log_listbox = tk.Listbox(log_frame, width=70, height=10, yscrollcommand=log_scrollbar.set)
log_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
log_scrollbar.config(command=log_listbox.yview)

# Start Button
start_button = tk.Button(root, text="Start", command=start_categorization)
start_button.pack(pady=20)


root.mainloop()