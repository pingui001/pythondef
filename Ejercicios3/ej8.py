wallet = {}

def add_expense():
    cat = input("Category: ").title()
    try:
        amount = float(input("Amount: $"))
        wallet[cat] = wallet.get(cat, 0) + amount
    except: print("Invalid input.")

def total_spent():
    print(f"Total spent: ${sum(wallet.values()):.2f}")

def percentage_by_category():
    total = sum(wallet.values())
    for cat, amt in wallet.items():
        print(f"{cat}: ${amt:.2f} ({(amt / total) * 100:.1f}%)")

def menu():
    while True:
        choice = input("1. Add expense\n2. Total spent\ 3. Percentage\n4. Exit: ")
        if choice == '1': add_expense()
        elif choice == '2': total_spent()
        elif choice == '3': percentage_by_category()
        elif choice == '4': break

menu()
