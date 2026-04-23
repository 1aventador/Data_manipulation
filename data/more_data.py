import csv
import random
from datetime import datetime, timedelta
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_name = "payments.csv"

headers = ["payment_id", "user_id", "amount", "currency", "payment_date"]

currencies = ["USD", "EUR", "PLN"]

start_date = datetime(2024, 1, 1)

with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for i in range(1, 11):
        writer.writerow([
            i,
            random.randint(1000, 2000),
            round(random.uniform(10, 500), 2),
            random.choice(currencies),
            (start_date + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        ])

print(f"Файл {file_name} создан")
