import tkinter as tk
from tkinter import filedialog, Text


root = tk.Tk()

def calculate(income, expenses, savings):
	yearly_income = income*12
	yearly_expenses = expenses*12
	true_income = yearly_income - yearly_expenses

	years = 1
	rate = 7
	total = 0
	dividend_income = 0


	while dividend_income < yearly_expenses:
		savings = savings + true_income
		interest = savings*(rate/100)
		savings = savings + interest
		dividend_income = 0.04*savings
		years = years + 1
		if years == 100:
			print("Error: You can't retire")
			break

	results['text'] = "You can retire in " + str(years) + " years. You will have $" + str(round(savings, 2)) + " in savings."


canvas = tk.Canvas(root, height=500, width=600, bg="gray")
canvas.pack()

income_frame = tk.Frame(root, bg="white", bd=5)
income_frame.place(relwidth = 0.8, relheight=0.1, relx=0.1, rely=0.1)

income = tk.Label(income_frame, text="Monthly Income")
income.place(relwidth=0.25, relheight=1)

income_entry = tk.Entry(income_frame)
income_entry.place(relx=1, relwidth=0.70, relheight=1, anchor="ne")

expenses_frame = tk.Frame(root, bg="white", bd=5)
expenses_frame.place(relwidth = 0.8, relheight=0.1, relx=0.1, rely=0.25)

expenses = tk.Label(expenses_frame, text="Monthly Expenses")
expenses.place(relwidth=0.25, relheight=1)

expenses_entry = tk.Entry(expenses_frame)
expenses_entry.place(relx=1, relwidth=0.70, relheight=1, anchor="ne")

savings_frame = tk.Frame(root, bg="white", bd=5)
savings_frame.place(relwidth = 0.8, relheight=0.1, relx=0.1, rely=0.4)

savings = tk.Label(savings_frame, text="Current Savings")
savings.place(relwidth=0.25, relheight=1)

savings_entry = tk.Entry(savings_frame)
savings_entry.place(relx=1, relwidth=0.70, relheight=1, anchor="ne")

calculate_frame = tk.Frame(root)
calculate_frame.place(relwidth = 0.3, relheight=0.1, relx=0.5, rely=0.55, anchor="n")

calculate_button = tk.Button(calculate_frame, text="Calculate Retirement Date", 
	command= lambda: calculate(int(income_entry.get()), int(expenses_entry.get()), int(savings_entry.get())))
calculate_button.place(relwidth=1, relheight=1)

results_frame = tk.Frame(root, bd=5)
results_frame.place(relwidth = 0.8, relheight=0.2, relx=0.1, rely=0.7)

results = tk.Label(results_frame)
results.pack()

root.mainloop()