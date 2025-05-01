import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt


# ======== Database Setup ========
def init_db():
    conn = sqlite3.connect('sales_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# ======== Insert Sale Entry ========
def insert_sale():
    product = product_entry.get()
    try:
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Quantity must be an integer and Price a float.")
        return

    if not product:
        messagebox.showerror("Input Error", "Product name cannot be empty.")
        return

    conn = sqlite3.connect('sales_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", (product, quantity, price))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Sale entry added!")
    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    refresh_summary()


# ======== Load Summary into Treeview ========
def refresh_summary():
    for row in summary_table.get_children():
        summary_table.delete(row)

    conn = sqlite3.connect('sales_data.db')
    query = '''
        SELECT 
            product, 
            SUM(quantity) AS total_quantity, 
            ROUND(SUM(quantity * price), 2) AS total_revenue
        FROM sales
        GROUP BY product
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()

    for _, row in df.iterrows():
        summary_table.insert('', tk.END, values=(row['product'], row['total_quantity'], f"${row['total_revenue']:.2f}"))


# ======== Plot Bar Charts ========
def plot_charts():
    conn = sqlite3.connect('sales_data.db')
    query = '''
        SELECT 
            product, 
            SUM(quantity) AS total_quantity, 
            SUM(quantity * price) AS total_revenue
        FROM sales
        GROUP BY product
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()

    if df.empty:
        messagebox.showinfo("No Data", "No sales data to plot.")
        return

    
    df.plot(kind='bar', x='product', y='total_quantity', color='skyblue', title='Total Quantity Sold')
    plt.ylabel('Quantity')
    plt.tight_layout()
    plt.show()

    
    df.plot(kind='bar', x='product', y='total_revenue', color='orange', title='Total Revenue')
    plt.ylabel('Revenue ($)')
    plt.tight_layout()
    plt.show()


# ======== GUI Setup ========
init_db()
root = tk.Tk()
root.title("Sales Summary App")
root.geometry("600x500")
root.resizable(False, False)


input_frame = tk.LabelFrame(root, text="Add New Sale", padx=10, pady=10)
input_frame.pack(padx=10, pady=10, fill="x")

tk.Label(input_frame, text="Product:").grid(row=0, column=0)
product_entry = tk.Entry(input_frame, width=20)
product_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Quantity:").grid(row=1, column=0)
quantity_entry = tk.Entry(input_frame, width=20)
quantity_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Price:").grid(row=2, column=0)
price_entry = tk.Entry(input_frame, width=20)
price_entry.grid(row=2, column=1)

add_button = tk.Button(input_frame, text="Add Sale", command=insert_sale, bg="#4CAF50", fg="white")
add_button.grid(row=3, columnspan=2, pady=5)


summary_frame = tk.LabelFrame(root, text="Sales Summary", padx=10, pady=10)
summary_frame.pack(padx=10, pady=10, fill="both", expand=True)

summary_table = ttk.Treeview(summary_frame, columns=("Product", "Quantity", "Revenue"), show="headings")
summary_table.heading("Product", text="Product")
summary_table.heading("Quantity", text="Total Quantity")
summary_table.heading("Revenue", text="Total Revenue")
summary_table.pack(fill="both", expand=True)


chart_button = tk.Button(root, text="📊 Show Charts", command=plot_charts, bg="#2196F3", fg="white")
chart_button.pack(pady=10)

refresh_summary()
root.mainloop()
