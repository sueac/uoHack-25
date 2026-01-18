import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_file():
    global words, word_index

    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text files", "*.txt")]
    )

    if file_path:
        status_label.config(text="AI is thinking...")
        root.update_idletasks()

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.split()
        word_index = 0
        text_box.delete("1.0", tk.END)

        root.after(2000, speak_words)

def speak_words():
    global word_index

    if word_index < len(words):
        text_box.insert(tk.END, words[word_index] + " ")
        text_box.see(tk.END)
        word_index += 1
        root.after(200, speak_words)
    else:
        status_label.config(text="AI finished speaking")

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("AI Reader")
root.geometry("500x300")

# ---------------- BACKGROUND (JPEG WORKS) ----------------
bg_image = Image.open("images/bruh.jpg")# JPEG is OK
bg_image = bg_image.resize((700, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()  # send to back

# ---------------- UI ----------------
upload_btn = tk.Button(root, text="Upload File", command=upload_file)
upload_btn.pack(pady=10)

status_label = tk.Label(
    root,
    text="No file selected",
    fg="white",
    bg="black"
)
status_label.pack()

text_box = tk.Text(
    root,
    wrap="word",
    height=5,
    bg="#003983",
    fg="white",
    insertbackground="white"
)
text_box.pack(padx=0, pady=0, fill="none", expand=False)

# ---------------- STATE ----------------
words = []
word_index = 0

root.mainloop()
