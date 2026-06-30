import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- Window ---------------- #
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("650x700")
root.configure(bg="#EAF4FC")
root.resizable(False, False)

history = []

# ---------------- Title ---------------- #
title = tk.Label(
    root,
    text="🔐 Random Password Generator",
    font=("Segoe UI", 22, "bold"),
    bg="#EAF4FC",
    fg="#0D47A1"
)
title.pack(pady=15)

# ---------------- Length ---------------- #
length_frame = tk.Frame(root, bg="#EAF4FC")
length_frame.pack()

tk.Label(
    length_frame,
    text="Password Length",
    font=("Segoe UI", 12, "bold"),
    bg="#EAF4FC"
).grid(row=0, column=0, padx=10)

length_spin = tk.Spinbox(
    length_frame,
    from_=8,
    to=30,
    width=6,
    font=("Segoe UI", 12)
)
length_spin.grid(row=0, column=1)

# ---------------- Options ---------------- #
option_frame = tk.LabelFrame(
    root,
    text="Character Options",
    font=("Segoe UI", 12, "bold"),
    bg="#EAF4FC",
    padx=15,
    pady=10
)
option_frame.pack(pady=20)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    option_frame,
    text="Uppercase Letters",
    variable=upper_var,
    font=("Segoe UI", 11),
    bg="#EAF4FC"
).grid(row=0, column=0, sticky="w")

tk.Checkbutton(
    option_frame,
    text="Lowercase Letters",
    variable=lower_var,
    font=("Segoe UI", 11),
    bg="#EAF4FC"
).grid(row=1, column=0, sticky="w")

tk.Checkbutton(
    option_frame,
    text="Numbers",
    variable=number_var,
    font=("Segoe UI", 11),
    bg="#EAF4FC"
).grid(row=2, column=0, sticky="w")

tk.Checkbutton(
    option_frame,
    text="Symbols",
    variable=symbol_var,
    font=("Segoe UI", 11),
    bg="#EAF4FC"
).grid(row=3, column=0, sticky="w")

# ---------------- Output Box ---------------- #
output_frame = tk.Frame(
    root,
    bg="#1565C0",
    width=500,
    height=120,
    relief="ridge",
    bd=4
)
output_frame.pack(pady=20)
output_frame.pack_propagate(False)

password_label = tk.Label(
    output_frame,
    text="Click Generate Password",
    font=("Consolas", 16, "bold"),
    bg="#1565C0",
    fg="white",
    wraplength=450
)
password_label.pack(pady=15)

strength_label = tk.Label(
    output_frame,
    text="Strength: --",
    font=("Segoe UI", 11, "bold"),
    bg="#1565C0",
    fg="white"
)
strength_label.pack()

# ---------------- Buttons Frame ---------------- #
button_frame = tk.Frame(root, bg="#EAF4FC")
button_frame.pack(pady=10)
# ---------------- Generate Password ---------------- #
def generate_password():
    try:
        length = int(length_spin.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid password length.")
        return

    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase

    if lower_var.get():
        characters += string.ascii_lowercase

    if number_var.get():
        characters += string.digits

    if symbol_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror(
            "Selection Error",
            "Please select at least one character type."
        )
        return

    # Generate Password
    password = "".join(random.choice(characters) for _ in range(length))

    # Display Password
    password_label.config(text=password)

    # Password Strength
    score = sum([
        upper_var.get(),
        lower_var.get(),
        number_var.get(),
        symbol_var.get()
    ])

    if length >= 12 and score == 4:
        strength = "🟢 Strong Password"
        strength_label.config(text=strength, fg="#00FF7F")

    elif length >= 8 and score >= 2:
        strength = "🟡 Medium Password"
        strength_label.config(text=strength, fg="#FFD700")

    else:
        strength = "🔴 Weak Password"
        strength_label.config(text=strength, fg="#FF5252")

    # Save History
    history.insert(0, password)

    if len(history) > 5:
        history.pop()

    history_box.delete(0, tk.END)

    for i, item in enumerate(history, start=1):
        history_box.insert(tk.END, f"{i}. {item}")


# ---------------- Copy Password ---------------- #
def copy_password():
    password = password_label.cget("text")

    if password == "" or password == "Click Generate Password":
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )


# ---------------- Clear History ---------------- #
def clear_history():
    history.clear()
    history_box.delete(0, tk.END)
    # ---------------- Buttons ---------------- #

generate_btn = tk.Button(
    button_frame,
    text="Generate Password",
    command=generate_password,
    font=("Segoe UI",12,"bold"),
    bg="#1976D2",
    fg="white",
    width=18
)
generate_btn.grid(row=0,column=0,padx=10)

copy_btn = tk.Button(
    button_frame,
    text="Copy",
    command=copy_password,
    font=("Segoe UI",12,"bold"),
    bg="#388E3C",
    fg="white",
    width=10
)
copy_btn.grid(row=0,column=1,padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear History",
    command=clear_history,
    font=("Segoe UI",12,"bold"),
    bg="#D32F2F",
    fg="white",
    width=12
)
clear_btn.grid(row=0,column=2,padx=10)

# ---------------- History ---------------- #

history_title = tk.Label(
    root,
    text="Last 5 Generated Passwords",
    font=("Segoe UI",13,"bold"),
    bg="#EAF4FC",
    fg="#0D47A1"
)

history_title.pack(pady=(20,5))

history_box = tk.Listbox(
    root,
    width=55,
    height=6,
    font=("Consolas",11)
)

history_box.pack()

# ---------------- Footer ---------------- #

footer = tk.Label(
    root,
    text="Developed using Python & Tkinter",
    font=("Segoe UI",10,"italic"),
    bg="#EAF4FC",
    fg="gray"
)

footer.pack(side="bottom",pady=10)

root.mainloop()