# Author: Caleb Nelson
# Create empty array variable to hold expenses
expense = []

# Gather user input for expenses until the user enters 0
while True:
    entered_expense = float(input("Enter an expense amount (or 0 to quit): "))
    
    if entered_expense < 0:
        print("Expense cannot be negative.")
        continue

    if entered_expense == 0:
        break

    expense.append(entered_expense)

# Create a variable to hold the category of the expense
category = []

# Categorize each expense
for i in range(len(expense)):
    if expense[i] < 25:
        category.append("Small")
    elif expense[i] <= 100:
        category.append("Moderate")
    else:
        category.append("Large")

# Check whether any expenses were entered
if len(expense) == 0:
    print("Congratulations! You have no expenses. What a wonderful way to live.")
else:
    # Calculate: count, sum, average, max, min, count of each category
    total_expenses = sum(expense)
    count_expenses = len(expense)
    average_expense = sum(expense) / len(expense)
    max_expense = max(expense)
    min_expense = min(expense)
    small_count = category.count("Small")
    moderate_count = category.count("Moderate")
    large_count = category.count("Large")

    # Print an expense report
    print(
        "Expense Report\n"
        "---------------\n"
        f"Total Expenses: ${total_expenses:,.2f}\n"
        f"Number of Expenses: {count_expenses}\n"
        f"Average Expense: ${average_expense:,.2f}\n"
        f"Maximum Expense: ${max_expense:,.2f}\n"
        f"Minimum Expense: ${min_expense:,.2f}\n"
        f"Small Expenses: {small_count}\n"
        f"Moderate Expenses: {moderate_count}\n"
        f"Large Expenses: {large_count}"
    )
