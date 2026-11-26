import csv
import os
import subprocess
from datetime import date

DATA_FILE = "expenses.csv"
C_PROGRAM = "./expense"  # Windows: "expense.exe"

def setup():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            csv.writer(f).writerow(["date", "category", "amount", "note"])

def add_expense():
    category = input("Category (food/travel/college/bills/shopping/other): ").strip()
    amount = float(input("Amount in ₹: "))
    note = input("Note (optional): ").strip()
    if amount <= 0:
        print("Amount must be positive.")
        return
    with open(DATA_FILE, "a", newline="") as f:
        csv.writer(f).writerow([date.today().isoformat(), category, amount, note])
    print("Expense saved!")

def get_month_total():
    month = date.today().strftime("%Y-%m")
    total = 0.0
    with open(DATA_FILE, newline="") as f:
        for row in csv.DictReader(f):
            if row["date"].startswith(month):
                total += float(row["amount"])
    return total

def report():
    budget = float(input("Enter your monthly budget (₹): "))
    total = get_month_total()
    # C program performs the calculation; Python handles input, storage and display.
    result = subprocess.check_output([C_PROGRAM, str(budget), str(total)], text=True)
    total_c, remaining, percent = map(float, result.split())
    print("\\n--- Monthly Report ---")
    print(f"Total spent: ₹{total_c:.2f}")
    print(f"Budget remaining: ₹{remaining:.2f}")
    print(f"Budget used: {percent:.1f}%")
    if remaining < 0:
        print("ALERT: You have exceeded your budget!")
    elif percent >= 80:
        print("Warning: You have used 80% or more of your budget.")

def list_expenses():
    with open(DATA_FILE, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("No expenses recorded yet.")
        return
    print("\\nDate          Category       Amount       Note")
    for r in rows:
        print(f'{r["date"]:<14}{r["category"]:<15}₹{float(r["amount"]):<11.2f}{r["note"]}')

def main():
    setup()
    while True:
        print("\\n=== Smart Daily Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Monthly budget report")
        print("4. Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                add_expense()
            elif choice == "2":
                list_expenses()
            elif choice == "3":
                report()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Choose 1, 2, 3 or 4.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
