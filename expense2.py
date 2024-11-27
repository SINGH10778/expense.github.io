import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the CSV file containing monthly expenses (and daily expenses)
def load_expenses_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please check the file path.")
        return None

# Add a new daily expense to the CSV
def add_daily_expense():
    category = entry_category.get()
    amount = entry_amount.get()
    date = entry_date.get()

    if category == "" or amount == "" or date == "":
        messagebox.showerror("Input Error", "Please fill in all fields")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a valid number")
        return

    # Save the new daily expense to the CSV
    try:
        df = load_expenses_data("daily_expenses.csv")  # Load daily expenses file
        if df is None:
            df = pd.DataFrame(columns=["Category", "Amount", "Date"])  # Create new DataFrame if empty
        
        # Append the new expense
        new_expense = pd.DataFrame([[category, amount, date]], columns=["Category", "Amount", "Date"])
        df = pd.concat([df, new_expense], ignore_index=True)
        df.to_csv("daily_expenses.csv", index=False)
        
        messagebox.showinfo("Success", "Expense added successfully!")
        
        # Clear entry fields
        entry_category.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        
        update_expenses_display()
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the expense: {e}")

# Calculate total expenses and group by category
def calculate_expenses(df):
    total_expenses = df["Amount"].sum()
    category_expenses = df.groupby("Category")["Amount"].sum()
    return total_expenses, category_expenses

# Display expenses in a bar chart
def show_bar_chart(category_expenses):
    fig, ax = plt.subplots(figsize=(10, 6))
    category_expenses.plot(kind="bar", ax=ax, color='cadetblue')
    ax.set_xlabel('Category', fontsize=12, fontweight='bold')
    ax.set_ylabel('Amount Spent ($)', fontsize=12, fontweight='bold')
    ax.set_title('Expense Distribution by Category', fontsize=16, fontweight='bold')
    ax.tick_params(axis='x', rotation=45, labelsize=10)
    
    canvas = FigureCanvasTkAgg(fig, master=frame_chart)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Update total expenses and display chart
def update_expenses_display():
    df_monthly = load_expenses_data("monthly_expenses.csv")  # Monthly expenses
    df_daily = load_expenses_data("daily_expenses.csv")  # Daily expenses
    
    if df_monthly is not None and df_daily is not None:
        total_expenses_monthly, category_expenses_monthly = calculate_expenses(df_monthly)
        total_expenses_daily, category_expenses_daily = calculate_expenses(df_daily)
        
        # Calculate the combined expenses
        total_expenses = total_expenses_monthly + total_expenses_daily
        category_expenses = category_expenses_monthly.add(category_expenses_daily, fill_value=0)
        
        label_total_expenses.config(text=f"Total Expenses: ${total_expenses:,.2f}")
        show_bar_chart(category_expenses)

# Create the main GUI window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("800x700")  # Adjusted for better spacing
root.config(bg="#F5F5F5")

# Create a frame for total expenses and button
frame_top = tk.Frame(root, bg="#F5F5F5")
frame_top.pack(pady=30, padx=30, fill=tk.X)

# Title Label with Font Styling
title_label = tk.Label(frame_top, text="Expense Tracker", font=("Helvetica", 24, "bold"), bg="#F5F5F5", fg="#2C3E50")
title_label.grid(row=0, column=0, pady=10, sticky="w")

# Total Expenses Label with Styling
label_total_expenses = tk.Label(frame_top, text="Total Expenses: $0.00", font=("Helvetica", 16), bg="#F5F5F5", fg="#2C3E50")
label_total_expenses.grid(row=1, column=0, pady=10)

# Button with Hover Effect (style changes when hovered)
def on_enter(e):
    button_load_data.config(bg="#5A9EFC")

def on_leave(e):
    button_load_data.config(bg="#4A90E2")

button_load_data = tk.Button(frame_top, text="Load Expenses and Show Chart", font=("Helvetica", 14), bg="#4A90E2", fg="white", command=update_expenses_display, relief="flat", width=25)
button_load_data.grid(row=2, column=0, pady=15)
button_load_data.bind("<Enter>", on_enter)
button_load_data.bind("<Leave>", on_leave)

# Create a frame for the daily expense form
frame_add_expense = tk.Frame(root, bg="#F5F5F5")
frame_add_expense.pack(pady=30, padx=30, fill=tk.X)

# Daily Expense Form (Category, Amount, Date)
label_category = tk.Label(frame_add_expense, text="Category", font=("Helvetica", 12), bg="#F5F5F5")
label_category.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_category = tk.Entry(frame_add_expense, font=("Helvetica", 12))
entry_category.grid(row=0, column=1, padx=10, pady=5)

label_amount = tk.Label(frame_add_expense, text="Amount", font=("Helvetica", 12), bg="#F5F5F5")
label_amount.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_amount = tk.Entry(frame_add_expense, font=("Helvetica", 12))
entry_amount.grid(row=1, column=1, padx=10, pady=5)

label_date = tk.Label(frame_add_expense, text="Date (YYYY-MM-DD)", font=("Helvetica", 12), bg="#F5F5F5")
label_date.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_date = tk.Entry(frame_add_expense, font=("Helvetica", 12))
entry_date.grid(row=2, column=1, padx=10, pady=5)

# Button to add daily expense
button_add_daily_expense = tk.Button(frame_add_expense, text="Add Daily Expense", font=("Helvetica", 14), bg="#4A90E2", fg="white", command=add_daily_expense, relief="flat", width=25)
button_add_daily_expense.grid(row=3, columnspan=2, pady=15)

# Create a frame for the chart
frame_chart = tk.Frame(root, bg="#F5F5F5")
frame_chart.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

# Run the application
root.mainloop()
