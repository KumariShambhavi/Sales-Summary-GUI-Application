Sales Summary GUI Application
A simple Python-based GUI application that connects to a SQLite database, allows users to input sales data (product name, quantity, price), and displays the sales summary in both tabular and graphical formats (bar charts). This app uses the Tkinter library for the GUI and matplotlib for the bar charts.

Features
Insert Sales Data: Input product name, quantity, and price.

Sales Summary Table: Displays total quantity sold and total revenue per product.

Interactive Charts: Visualizes sales data with bar charts for quantity sold and revenue.

SQLite Integration: Uses SQLite for data storage, which is lightweight and does not require an external database server.

Simple Error Handling: Provides input validation and error messages for incorrect data.

Libraries Used
Tkinter: For creating the graphical user interface (GUI).

SQLite3: Built-in Python module for interacting with the SQLite database.

Pandas: For data manipulation and querying the database.

Matplotlib: For creating bar charts to visualize sales data.

ttk: For styling the treeview table.

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/sales-summary-app.git
Navigate to the project directory:

bash
Copy
Edit
cd sales-summary-app
Install required libraries:

bash
Copy
Edit
pip install pandas matplotlib
Run the Python script:

bash
Copy
Edit
python sales_gui.py
Usage
When you run the app, a window will open allowing you to:

Enter Sales Data: Type the product name, quantity, and price, then click Add Sale to add the entry to the database.

View Sales Summary: The summary table will update automatically, showing the total quantity and revenue per product.

View Charts: Click the Show Charts button to visualize the total quantity sold and total revenue in bar charts.

Output
1. Sales Data Input
The user can enter:

Product Name (e.g., "Product A")

Quantity (e.g., 10)

Price (e.g., 15.99)

2. Sales Summary Table
Displays the total quantity sold and total revenue per product.

Product	Total Quantity	Total Revenue
Product A	50	$799.50
Product B	30	$479.70

3. Bar Charts
The charts will display:

Total Quantity Sold: A bar chart showing the total quantity sold per product.

Total Revenue: A bar chart showing the total revenue generated per product.
