import tkinter as tk
from tkinter import messagebox
import os

# ---------------- FILES ----------------
BOOK_FILE = "books.txt"
MEMBER_FILE = "members.txt"
ISSUE_FILE = "issued.txt"

# ---------------- LOAD FILES ----------------
def load_files():
    for file in [BOOK_FILE, MEMBER_FILE, ISSUE_FILE]:
        if not os.path.exists(file):
            open(file, "w").close()

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Library Management System")
root.geometry("700x500")
root.config(bg="lightblue")

load_files()

# ---------------- LOGIN ----------------
def login():
    if entry_user.get() == "admin" and entry_pass.get() == "123":
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Login")

# ---------------- DASHBOARD ----------------
def open_dashboard():
    win = tk.Toplevel(root)
    win.title("Dashboard")
    win.geometry("600x400")
    win.config(bg="lightgreen")

    tk.Label(win, text="Library Dashboard", font=("Arial", 18), bg="lightgreen").pack(pady=20)

    tk.Button(win, text="Add Book", width=20, bg="green", command=add_book_ui).pack(pady=5)
    tk.Button(win, text="Register Member", width=20, bg="blue", fg="white", command=register_member_ui).pack(pady=5)
    tk.Button(win, text="Issue Book", width=20, bg="purple", fg="white", command=issue_book_ui).pack(pady=5)
    tk.Button(win, text="Return Book", width=20, bg="orange", command=return_book_ui).pack(pady=5)
    tk.Button(win, text="Inventory", width=20, bg="yellow", command=show_inventory).pack(pady=5)
    tk.Button(win, text="Fine Calculator", width=20, bg="red", fg="white", command=fine_ui).pack(pady=5)

# ---------------- ADD BOOK ----------------
def add_book_ui():
    win = tk.Toplevel(root)
    win.title("Add Book")
    win.geometry("300x200")
    win.config(bg="lightgreen")

    tk.Label(win, text="Book Name:", bg="lightgreen").pack(pady=5)
    entry = tk.Entry(win)
    entry.pack()

    def add():
        book = entry.get()
        with open(BOOK_FILE, "a") as f:
            f.write(book + "\n")
        messagebox.showinfo("Success", "Book Added")

    tk.Button(win, text="Add", bg="green", command=add).pack(pady=10)

# ---------------- REGISTER MEMBER ----------------
def register_member_ui():
    win = tk.Toplevel(root)
    win.title("Register Member")
    win.geometry("300x200")
    win.config(bg="lightblue")

    tk.Label(win, text="Member Name:", bg="lightblue").pack(pady=5)
    entry = tk.Entry(win)
    entry.pack()

    def register():
        with open(MEMBER_FILE, "a") as f:
            f.write(entry.get() + "\n")
        messagebox.showinfo("Success", "Member Registered")

    tk.Button(win, text="Register", bg="blue", fg="white", command=register).pack(pady=10)

# ---------------- ISSUE BOOK ----------------
def issue_book_ui():
    win = tk.Toplevel(root)
    win.title("Issue Book")
    win.geometry("300x250")
    win.config(bg="plum")

    tk.Label(win, text="Book Name:", bg="plum").pack()
    book_entry = tk.Entry(win)
    book_entry.pack()

    tk.Label(win, text="Member Name:", bg="plum").pack()
    member_entry = tk.Entry(win)
    member_entry.pack()

    def issue():
        book = book_entry.get()
        member = member_entry.get()

        with open(BOOK_FILE, "r") as f:
            books = [b.strip() for b in f.readlines()]

        if book in books:
            books.remove(book)

            with open(BOOK_FILE, "w") as f:
                for b in books:
                    f.write(b + "\n")

            with open(ISSUE_FILE, "a") as f:
                f.write(book + "," + member + "\n")

            messagebox.showinfo("Success", "Book Issued")
        else:
            messagebox.showerror("Error", "Book not available")

    tk.Button(win, text="Issue", bg="purple", fg="white", command=issue).pack(pady=10)

# ---------------- RETURN BOOK ----------------
def return_book_ui():
    win = tk.Toplevel(root)
    win.title("Return Book")
    win.geometry("300x200")
    win.config(bg="orange")

    tk.Label(win, text="Book Name:", bg="orange").pack()
    entry = tk.Entry(win)
    entry.pack()

    def return_book():
        book = entry.get()

        with open(ISSUE_FILE, "r") as f:
            records = f.readlines()

        new_records = []
        found = False

        for r in records:
            b, m = r.strip().split(",")
            if b == book:
                found = True
            else:
                new_records.append(r)

        if found:
            with open(ISSUE_FILE, "w") as f:
                f.writelines(new_records)

            with open(BOOK_FILE, "a") as f:
                f.write(book + "\n")

            messagebox.showinfo("Success", "Book Returned")
        else:
            messagebox.showerror("Error", "Book not found")

    tk.Button(win, text="Return", bg="darkorange", command=return_book).pack(pady=10)

# ---------------- INVENTORY ----------------
def show_inventory():
    win = tk.Toplevel(root)
    win.title("Inventory")
    win.geometry("300x300")
    win.config(bg="yellow")

    tk.Label(win, text="Available Books:", bg="yellow").pack()

    with open(BOOK_FILE, "r") as f:
        for line in f:
            tk.Label(win, text=line.strip(), bg="yellow").pack()

# ---------------- FINE ----------------
def fine_ui():
    win = tk.Toplevel(root)
    win.title("Fine Calculator")
    win.geometry("300x200")
    win.config(bg="lightcoral")

    tk.Label(win, text="Days Late:", bg="lightcoral").pack()
    entry = tk.Entry(win)
    entry.pack()

    def calc():
        try:
            fine = int(entry.get()) * 10
            messagebox.showinfo("Fine", f"Fine = {fine}")
        except:
            messagebox.showerror("Error", "Enter number")

    tk.Button(win, text="Calculate", bg="red", fg="white", command=calc).pack(pady=10)

# ---------------- LOGIN UI ----------------
tk.Label(root, text="Library Login", font=("Arial", 20), bg="lightblue").pack(pady=20)

tk.Label(root, text="Username", bg="lightblue").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password", bg="lightblue").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", bg="green", command=login).pack(pady=20)

root.mainloop()