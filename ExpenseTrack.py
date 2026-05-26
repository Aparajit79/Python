import csv
import os
from datetime import datetime 

CSV_FILE = "expenses.csv"

def log_expense():
  category = input("Enter expense category(Food,rent,transport): ").strip()
  if not category:
    print("Category cannot be empty.")
    return
  try:
    amt = float(input("Enter amount : "))
  except ValueError:
    print("Invalid enter an amount.")
    return
  
  description = input("Enter a description to noted : ").strip()
  today = datetime.now().date().isoformat()

  with open(CSV_FILE, "a", newline="", encoding="utf-8")as f:
    writer = csv.writer(f)
    writer.writerow([today, category,f"{amt:.2f}",description])

  print("Expense logged Successfully..")



def view_expenses():
    """Read the CSV file and print each record nicely."""
    if not os.path.exists(CSV_FILE):
        print(" No expenses logged yet!")
        return
    print("\n--- ALL EXPENSES ---")
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader, start=1):
            date, category, amount, description = row
            print(f"{idx}. {date} | {category:<12} | ${float(amount):>7.2f} | {description}")
    print("-" * 40)

def expense_summary():
  if not os.path.exists(CSV_FILE):
    print("No expense logged yet - 0.00Rs ")
    return
  total = 0.0
  with open(CSV_FILE, "r",newline="",encoding="utf-8")as f:
    reader = csv.reader(f)
    for row in reader:
      total += float(row[2])
  print(f"\nTotal money spent : ${total:.2f}")


def main():
    while True:
        print("\n--- PERSONAL EXPENSE TRACKER ---")
        print("1. Log a New Expense")
        print("2. View All Expenses")
        print("3. Expense Summary (Total Spending)")
        print("4. Exit")
        try:
            choice = int(input("Select an option (1‑4): "))
        except ValueError:
            print(" Please enter a number between 1 and 4.")
            continue
        match choice:
            case 1:
                log_expense()
            case 2:
                view_expenses()
            case 3:
                expense_summary()
            case 4:
                print(" Thanks for using the tracker. Goodbye!")
                break
            case _:
                print(" Invalid choice – pick 1‑4.")
if __name__ == "__main__":
    main()  

        