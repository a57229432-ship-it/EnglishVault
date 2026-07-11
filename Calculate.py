from pathlib import Path
import re


def calculate_income():
    file_path = Path("IncomeTracker.md")
    text = file_path.read_text(encoding="utf-8")

    rows = re.findall(
       r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\w+)\s*\|\s*([\d,]+)\s*\|.*",
        text
    )

    total = 0
    best_date = ""
    best_amount = 0

    for date, day, amount in rows:
        money = int(amount.replace(",", ""))
        total += money

        if money > best_amount:
            best_amount = money
            best_date = date

    new_text = re.sub(
        r"\*\*.*Monthly Total:\*\* ₩[\d,]*",
        f"**💰 Monthly Total:** ₩{total:,}",
        text
    )

    new_text = re.sub(
        r"\*\*.*Best Day:\*\*.*",
        f"**☑️ Best Day:** {best_date} (₩{best_amount:,})",
        new_text
    )

    file_path.write_text(new_text, encoding="utf-8")

    print(f"Income Total updated: ₩{total:,}")
    print(f"Income Best Day updated: {best_date} (₩{best_amount:,})")

def calculate_expense():
    file_path = Path("ExpenseTracker.md")
    text = file_path.read_text(encoding="utf-8")

    amounts = re.findall(
        r"\|\s*\d{4}-\d{2}-\d{2}\s*\|\s*\w+\s*\|.*?\|\s*([\d,]+)\s*\|",
        text
    )

    total = 0

    for amount in amounts:
        total += int(amount.replace(",", ""))

    new_text = re.sub(
        r"##.*Total Variable Expenses:.*",
        f"## 📒 Total Variable Expenses: {total:,} KRW",
        text
    )

    file_path.write_text(new_text, encoding="utf-8")

    print(f"Expense Total updated: ₩{total:,}")
def calculate_net_income():
    income_text = Path("IncomeTracker.md").read_text(encoding="utf-8")
    expense_text = Path("ExpenseTracker.md").read_text(encoding="utf-8")

    income_match = re.search(
        r"Monthly Total:.*?₩?\s*([\d,]+)",
        income_text
    )

    fixed_match = re.search(
        r"Total Fixed Expenses:.*?([\d,]+)",
        expense_text
    )

    variable_match = re.search(
        r"Total Variable Expenses:.*?([\d,]+)",
        expense_text
    )

    if not income_match or not fixed_match or not variable_match:
        print("Net Income calculation failed: totals not found.")
        return

    income = int(income_match.group(1).replace(",", ""))
    fixed_expense = int(fixed_match.group(1).replace(",", ""))
    variable_expense = int(variable_match.group(1).replace(",", ""))

    total_expense = fixed_expense + variable_expense
    net_income = income - total_expense

    print(f"Total Income: ₩{income:,}")
    print(f"Total Fixed Expenses: ₩{fixed_expense:,}")
    print(f"Total Variable Expenses: ₩{variable_expense:,}")
    print(f"Net Income: ₩{net_income:,}")
def update_readme():
    print("Updating README...")
calculate_income()
calculate_expense()
calculate_net_income()
update_readme()