

print("=== Monthly Expenses ===")

rent = float(input("Enter Rent Amount: "))
food = float(input("Enter Food Expense: "))
transport = float(input("Enter Transport Expense: "))
electricity = float(input("Enter Electricity Bill: "))
other = float(input("Enter Other Expenses: "))

total = rent + food + transport + electricity + other

print("\n----- Expense Summary -----")
print(f"Rent         : ₹{rent:.2f}")
print(f"Food         : ₹{food:.2f}")
print(f"Transport    : ₹{transport:.2f}")
print(f"Electricity  : ₹{electricity:.2f}")
print(f"Other        : ₹{other:.2f}")
print("---------------------------")
print(f"Total Monthly Expense : ₹{total:.2f}")