import csv
import matplotlib.pyplot as plt

def read_expenses(file_path="expenses.csv"):
    expenses = {}
    try:
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                category, amount = row
                expenses[category] = expenses.get(category, 0) + float(amount)
    except FileNotFoundError:
        print("No expenses.csv found, create one first!")
    return expenses

def add_expense(category, amount, file_path="expenses.csv"):
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([category, amount])

def plot_expenses(expenses):
    if not expenses:
        print("No data to plot.")
        return
    categories = list(expenses.keys())
    amounts = list(expenses.values())
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expense Breakdown")
    plt.show()

if __name__ == "__main__":
    print("\n=== Personal Finance Tracker ===")
    choice = input("1. Add Expense\n2. Show Report\nChoose: ").strip()

    if choice == "1":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        add_expense(cat, amt)
        print("Expense added.")
    elif choice == "2":
        data = read_expenses()
        print("Expense Summary:", data)
        plot_expenses(data)
    else:
        print("Invalid choice.")
