import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Belajar Tkinter")
root.geometry("600x400")
root.configure(bg="white")


# =========================
# JUDUL
# =========================

judul = tk.Label(
    root,
    text="BELAJAR PYTHON TKINTER",
    font=("Arial", 20, "bold"),
    fg="red",
    bg="white"
)

judul.pack(pady=20)


# =========================
# FUNGSI TOMBOL 1
# =========================

def tombol_pertama():
    messagebox.showinfo(
        "Tombol 1",
        "Kamu menekan tombol pertama!"
    )


# =========================
# FUNGSI TOMBOL 2
# =========================

def tombol_kedua():
    messagebox.showwarning(
        "Tombol 2",
        "Kamu menekan tombol kedua!"
    )


# =========================
# FUNGSI TOMBOL 3
# =========================
def tombol_ketiga():
    messagebox.showerror(
        "Error",
        "Kamu menekan tombol ke tiga!"
    )


# =========================
# TOMBOL 1
# =========================

tombol1 = tk.Button(
    root,
    text="Tombol 1",
    command=tombol_pertama
)

tombol1.pack(side="left", padx=5)


# =========================
# TOMBOL 2
# =========================

tombol2 = tk.Button(
    root,
    text="Tombol 2",
    command=tombol_kedua
)

tombol2.pack(side="left", padx=5)

# =========================
# TOMBOL 3
# =========================

tombol3 = tk.Button(
    root,
    text="Tombol 3",
    command=tombol_ketiga
)

tombol3.pack(side="left", padx=5)


root.mainloop()