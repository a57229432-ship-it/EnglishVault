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

    readme_path = Path("README.md")
    income_path = Path("IncomeTracker.md")
    expense_path = Path("ExpenseTracker.md")

    readme_text = readme_path.read_text(encoding="utf-8")
    income_text = income_path.read_text(encoding="utf-8")
    expense_text = expense_path.read_text(encoding="utf-8")

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

    best_day_match = re.search(
        r"Best Day:.*?(\d{4}-\d{2}-\d{2}).*?₩?\s*([\d,]+)",
        income_text
    )

    if not income_match or not fixed_match or not variable_match:
        print("README update failed: totals not found.")
        return

    income = int(income_match.group(1).replace(",", ""))
    fixed_expense = int(fixed_match.group(1).replace(",", ""))
    variable_expense = int(variable_match.group(1).replace(",", ""))

    total_expense = fixed_expense + variable_expense
    net_income = income - total_expense

    readme_text = re.sub(
        r"(?m)^(\*\*💰 Income:\*\*).*$",
        rf"\1 ₩{income:,}",
        readme_text
    )

    readme_text = re.sub(
        r"(?m)^(\*\*💸 Expense:\*\*).*$",
        rf"\1 ₩{total_expense:,}",
        readme_text
    )

    readme_text = re.sub(
        r"(?m)^(\*\*💎 Net Income:\*\*).*$",
        rf"\1 ₩{net_income:,}",
        readme_text
    )

    if best_day_match:
        best_date = best_day_match.group(1)
        best_amount = int(best_day_match.group(2).replace(",", ""))

        readme_text = re.sub(
            r"(?m)^(\*\*☑️ Best Day:\*\*).*$",
            rf"\1 {best_date} (₩{best_amount:,})",
            readme_text
        )

    readme_path.write_text(readme_text, encoding="utf-8")

    print("README updated successfully.")


calculate_income()
calculate_expense()
calculate_net_income()
update_readme()