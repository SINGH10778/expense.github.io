import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the CSV file containing monthly expenses
def load_expenses_data():
    file_path = "monthly_expenses.csv"  # Update with the correct path to your CSV file
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please check the file path.")
        return None

# Calculate total expenses and group by category
def calculate_expenses(df):
    total_expenses = df["Amount"].sum()
    category_expenses = df.groupby("Category")["Amount"].sum()
    return total_expenses, category_expenses

# Display expenses in a bar chart
def show_bar_chart(category_expenses):
    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create bar chart
    category_expenses.plot(kind="bar", ax=ax, color='cadetblue')
    
    # Add labels and title
    ax.set_xlabel('Category', fontsize=12, fontweight='bold')
    ax.set_ylabel('Amount Spent ($)', fontsize=12, fontweight='bold')
    ax.set_title('Expense Distribution by Category', fontsize=16, fontweight='bold')
    ax.tick_params(axis='x', rotation=45, labelsize=10)  # Rotate x-axis labels for better readability
    
    # Create a canvas for embedding the plot into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame_chart)  # Pass the frame to embed the plot
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Update total expenses and display chart
def update_expenses_display():
    df = load_expenses_data()
    if df is not None:
        # Calculate total expenses and expenses by category
        total_expenses, category_expenses = calculate_expenses(df)
        
        # Update total expenses label
        label_total_expenses.config(text=f"Total Expenses: ${total_expenses:,.2f}")
        
        # Show bar chart
        show_bar_chart(category_expenses)

# Create the main GUI window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("800x650")  # Slightly larger to accommodate the chart better
root.config(bg="#f4f4f9")

# Create a frame for total expenses and button
frame_top = tk.Frame(root, bg="#f4f4f9")
frame_top.pack(pady=20, padx=30, fill=tk.X)

# Title Label with Font Styling
title_label = tk.Label(frame_top, text="Monthly Expense Tracker", font=("Helvetica", 20, "bold"), bg="#f4f4f9", fg="#333333")
title_label.grid(row=0, column=0, pady=10, sticky="w")

# Total Expenses Label with Styling
label_total_expenses = tk.Label(frame_top, text="Total Expenses: $0.00", font=("Helvetica", 16), bg="#f4f4f9", fg="#333333")
label_total_expenses.grid(row=1, column=0, pady=10)

# Button with Hover Effect (style changes when hovered)
def on_enter(e):
    button_load_data.config(bg="#5A9EFC")

def on_leave(e):
    button_load_data.config(bg="#4A90E2")

button_load_data = tk.Button(frame_top, text="Load Expenses and Show Chart", font=("Helvetica", 14), bg="#4A90E2", fg="white", command=update_expenses_display, relief="flat")
button_load_data.grid(row=2, column=0, pady=15)
button_load_data.bind("<Enter>", on_enter)
button_load_data.bind("<Leave>", on_leave)

# Create a frame for the chart
frame_chart = tk.Frame(root, bg="#f4f4f9")
frame_chart.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

# Run the application
root.mainloop()
