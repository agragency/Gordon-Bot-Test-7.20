import time
from datetime import datetime

def check_price():
    # Dummy placeholder for actual $PIZZA price check logic
    fake_price = 0.000347
    print(f"[{datetime.now()}] 🧠 Gordon says: $PIZZA is {fake_price} SOL")

def main():
    print(f"[{datetime.now()}] 🚀 Gordon Bot started... watching $PIZZA.")
    while True:
        check_price()
        time.sleep(10)  # Wait 10 seconds before next check

if __name__ == "__main__":
    main()
