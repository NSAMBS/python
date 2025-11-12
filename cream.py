import tkinter as tk
from tkinter import ttk
import csv
def view_registered_members():
    viewer = tk.Toplevel()
    viewer.title("Registered Members")
    viewer.geometry("650x450")

    # Search Frame
    search_frame = tk.Frame(viewer)
    search_frame.pack(pady=10)

    search_var = tk.StringVar()
    tk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
    search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
    search_entry.pack(side=tk.LEFT, padx=5)

    # Treeview setup
    columns = ("Full Name", "Role/Position", "Email", "Phone Number")
    tree = ttk.Treeview(viewer, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    vsb = ttk.Scrollbar(viewer, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)

    # Load data from CSV
    def load_data(filter_text=""):
        tree.delete(*tree.get_children())
        try:
            with open("club_members.csv", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if filter_text.lower() in " ".join(row).lower():
                        tree.insert("", "end", values=row)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No member data found.")

    # Search trigger
    def on_search(*args):
        load_data(search_var.get())

    search_var.trace_add("write", on_search)
    load_data()