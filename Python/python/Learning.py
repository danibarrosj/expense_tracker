import csv
import os

def add_expense(category, amount, date):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, date])
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists("expenses.csv"):
        print("No expenses found.")
        return
    
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
        if not expenses:
            print("No expenses recorded yet.")
            return
        
        print("\nExpenses:")
        for idx, (category, amount, date) in enumerate(expenses, start=1):
            print(f"{idx}. {category} - ${amount} on {date}")

def delete_expense(index):
    if not os.path.exists("expenses.csv"):
        print("No expenses found.")
        return
    
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
    
    if index < 1 or index > len(expenses):
        print("Invalid index.")
        return
    
    del expenses[index - 1]
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
    print("Expense deleted successfully!")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            category = input("Enter category (Food, Transport, etc.): ")
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_expenses()
            index = int(input("Enter the index of the expense to delete: "))
            delete_expense(index)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
