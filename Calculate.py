from pathlib import Path
import re

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
    r"\*\*💰 Monthly Total:\*\* ₩[\d,]*",
    f"**💰 Monthly Total:** ₩{total:,}",
    text
)

new_text = re.sub(
    r"\*\*.*Best Day:\*\*.*",
    f"**☑️ Best Day:** {best_date} (₩{best_amount:,})",
    new_text
)


file_path.write_text(new_text, encoding="utf-8")

print(f"Monthly Total updated: ₩{total:,}")
print(f"Best Day updated: {best_date} (₩{best_amount:,})")