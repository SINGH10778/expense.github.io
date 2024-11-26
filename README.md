# expense.github.io

Expense Tracker with Professional GUI: Description, Instructions, and Requirements
Description:
This Expense Tracker is a Python application designed to track and visualize monthly expenses. It uses Tkinter for the graphical user interface (GUI) and Matplotlib for displaying a bar chart of expenses by category.

Features:
Expense Tracking: You can track monthly expenses across multiple categories such as Food, Housing, Utilities, and more.
Total Expenses: The application calculates and displays the total amount spent for the month.
Bar Chart Visualization: A professional bar chart is generated to show the distribution of expenses by category.
User-friendly Interface: The GUI is modern and professional, with intuitive controls and a visually appealing design.
The user can interact with the application by loading the expense data from a CSV file and viewing the total spending along with a graphical representation.

Requirements:
To run the Expense Tracker application, the following Python libraries are required:

Pandas: For handling and manipulating the expense data stored in the CSV file.
Matplotlib: For generating the bar chart that displays the distribution of expenses.
Tkinter: For creating the graphical user interface (GUI).
Install Dependencies:
Make sure to install the required libraries using the following commands:

Note: Tkinter is included with most standard Python installations, so you may not need to install it separately. If you encounter issues, make sure it's properly installed for your Python version.

Instructions for Usage:
Prepare Your Data:

The application requires a CSV file containing your monthly expenses. Make sure your CSV file is structured in the following format:
Date	Description	Amount	Category
2024-11-01	Groceries	120.50	Food
2024-11-02	Rent	1500.00	Housing
2024-11-03	Electricity Bill	60.00	Utilities
2024-11-04	Water Bill	35.00	Utilities
2024-11-05	Internet	45.00	Utilities
Save the data as expanded_monthly_expenses.csv or modify the file path in the script to match your dataset location.

Running the Application:

After preparing your data, save the Python script and the CSV file in the same folder.
Run the Python script:
python expense_tracker.py
Using the GUI:

When the application window opens, click the "Load Expenses and Show Chart" button.
The total expenses will be displayed at the top.
A bar chart will appear below showing how expenses are distributed across different categories.

Interacting with the Application:

The button will load the data from the CSV file and display:
The total expenses for the month.
A bar chart showing the expenses distribution by category.
The bar chart will update each time you click the button, providing a fresh visualization based on the data.
