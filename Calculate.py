from pathlib import Path
import re


def calculate_income():
    file_path = Path("IncomeTracker.md")
    text = file_path.read_text(encoding="utf-8")

    rows = re.findall(
        r"\|\s*(\d{2}/\d{2})\s*\|\s*(\w+)\s*\|\s*([\d,]+)\s*\|",
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
    income = 1775000
    expense = 136300
    net_income = income - expense

    print(f"Net Income: ₩{net_income:,}")
calculate_income()
calculate_expense()
calculate_net_income()