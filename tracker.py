# Project: Expense Tracker - Installment 5: The Menu Comes Alive
# Author: Danica Fay E. Mina
# Description: Interactive loop-driven expense tracker menu supporting logging, tracking totals, and graceful exit.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes...")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!\n")

subtotal = 0.0
count = 0

while True:
    print("MAIN MENU")
    print("[1] Add an expense")
    print("[2] View all expenses (coming soon)")
    print("[3] Show total spent")
    print("[4] Exit")
    
    choice = input("Choose 1-4: ")
    
    if choice == "1":
        amount = float(input("Amount? "))
        if amount > 200:
            print("  Huge expense — are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
        subtotal += amount
        count += 1
        print()
    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.\n")
    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        
        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent}%):\t${tax}")
        print(f"Grand total:\t${total}\n")
        
        if total > budget:
            over_amount = total - budget
            print(f"Over budget by ${over_amount}!")
        elif total > (0.90 * budget):
            careful_left = budget - total
            print(f"Careful: only ${careful_left} left.")
        else:
            left = budget - total
            print(f"Within budget. ${left} left.")
        print()
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Danica Fay E. Mina | Installment 5")
        print("=" * 40)
        break
    else:
        print("Please choose 1, 2, 3 or 4.\n")