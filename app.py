import tkinter as tk
from tkinter import filedialog, Text


root = tk.Tk()

def calculate(income, expenses, savings):

	if isinstance(income, int) == False or isinstance(expenses, int) == False or isinstance(savings, int) == False:
		results['text'] = "Oops! Please enter integer values."
		

	#format input values for calculations
	yearly_income = income*12
	yearly_expenses = expenses*12
	true_income = yearly_income - yearly_expenses

	years = 1
	rate = 7
	total = 0
	dividend_income = 0

	#assumed dividend income rate: 4% anually
	#assumed interest rate: 7% anually

	#calculate interest earned each year + yearly savings.
	while dividend_income < yearly_expenses:
		savings = savings + true_income
		interest = savings*(rate/100)
		savings = savings + interest
		dividend_income = 0.04*savings
		years = years + 1
		if savings <= 0:
			results['text'] = "You can't retire. With your current finances,\n you will run out of money in " + str(years) + " years."
			return 1
		if years == 100:
			results['text'] = "You can't retire. Lower your expense ratio."
			return 1

	results['text'] = "You can retire in " + str(years) + " years. You will have $" + str(round(savings, 2)) + " in savings.\n\nThis calculation assumes a 7 percent annual return\nand a dividend income rate of 4 percent."


#initialize and format GUI
canvas = tk.Canvas(root, height=500, width=600, bg="white")
canvas.pack()
root.title("FIRE Calculator")

#income input field
income_frame = tk.Frame(root, bg="white", bd=5)
income_frame.place(relwidth = 0.8, relheight=0.1, relx=0.1, rely=0.1)

income = tk.Label(income_frame, text="Monthly Income")
income.place(relwidth=0.3, relheight=1)

income_entry = tk.Entry(income_frame)
income_entry.place(relx=1, relwidth=0.65, relheight=1, anchor="ne")

#expenses input field
expenses_frame = tk.Frame(root, bg="white", bd=5)
expenses_frame.place(relwidth = 0.8, relheight=0.1, relx=0.1, rely=0.25)

expenses = tk.Label(expenses_frame, text="Monthly Expenses")
expenses.place(relwidth=0.3, relheight=1)

expenses_entry = tk.Entry(expenses_frame)
expenses_entry.place(relx=1, relwidth=0.65, relheight=1, anchor="ne")

#savings input field
savings_frame = tk.Frame(root, bg="white", bd=5)
savings_frame.place(relwidth = 0.8, relheight=0.1, relx=0.1, rely=0.4)

savings = tk.Label(savings_frame, text="Current Investments")
savings.place(relwidth=0.3, relheight=1)

savings_entry = tk.Entry(savings_frame)
savings_entry.place(relx=1, relwidth=0.65, relheight=1, anchor="ne")

#button init and formatting
calculate_frame = tk.Frame(root)
calculate_frame.place(relwidth = 0.3, relheight=0.1, relx=0.5, rely=0.55, anchor="n")

calculate_button = tk.Button(calculate_frame, text="Calculate Retirement Date", 
	command= lambda: calculate(int(income_entry.get()), int(expenses_entry.get()), int(savings_entry.get())))
calculate_button.place(relwidth=1, relheight=1)

#user results field
results_frame = tk.Frame(root, bd=5)
results_frame.place(relwidth = 0.8, relheight=0.2, relx=0.1, rely=0.7)

results = tk.Label(results_frame)
results.pack()

root.mainloop()