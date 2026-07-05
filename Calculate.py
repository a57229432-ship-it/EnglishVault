from pathlib import Path
import re

file_path = Path("IncomeTracker.md")

text = file_path.read_text(encoding="utf-8")

amounts = re.findall(r"\|\s*\d{2}/\d{2}\s*\|\s*\w+\s*\|\s*([\d,]+)\s*\|", text)

total = 0
for amount in amounts:
    total += int(amount.replace(",", ""))

new_text = re.sub(
    r"\*\*💰 Monthly Total:\*\* ₩[\d,]*",
    f"**💰 Monthly Total:** ₩{total:,}",
    text
)

file_path.write_text(new_text, encoding="utf-8")

print(f"Monthly Total updated: ₩{total:,}")