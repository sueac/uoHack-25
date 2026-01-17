import tkinter as tk
from tkinter import filedialog

def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All files", "*.*")]
    )
    if file_path:
        label.config(text=f"Selected file:\n{file_path}")

# Create main window
root = tk.Tk()
root.title("File Upload")
root.geometry("400x200")

# Upload button
upload_btn = tk.Button(root, text="Upload File", command=upload_file)
upload_btn.pack(pady=20)

# Label to show selected file
label = tk.Label(root, text="No file selected", wraplength=350)
label.pack(pady=10)

# Run the app
root.mainloop()
