import csv
import random
import uuid
from datetime import datetime, timedelta

# ==================== SETTINGS ====================
NUM_ROWS = 10
OUTPUT_FILE = "orders.csv"
# =================================================

print("Starting generation of orders.csv...")

with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["order_id", "customer_id", "product_id",
                    "amount", "order_date", "status"])

    statuses = ["completed", "pending", "shipped", "cancelled"]

    for i in range(NUM_ROWS):
        order_id = f"ORD-{uuid.uuid4().hex[:8]}-{i:04d}"
        customer_id = f"CUST-{random.randint(10000, 99999)}"
        product_id = f"PROD-{random.randint(1000, 9999)}"
        amount = round(random.uniform(49.99, 999.99), 2)

        # Random date in last 30 days
        order_date = (
            datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        status = random.choice(statuses)

        writer.writerow([order_id, customer_id, product_id,
                        amount, order_date, status])

print(f"File successfully created: {OUTPUT_FILE}")
print(f"Rows generated: {NUM_ROWS}")
print("Ready to upload to GCS!")
