days = ["mon", "tues", "weds", "thurs", "fri"]

print("--- 1. Iteration using an index (C-style) ---")
for day_num in range(0, len(days)):
    print(f"Index {day_num}: {days[day_num]}")

print("\n--- 2. Direct iteration over elements (more Pythonic) ---")
for day in days:
    print(day)

print("\n--- 3. Using enumerate() to get both index and element (idiomatic Python) ---")
for day_num, day in enumerate(days):
    print(f"Index {day_num}: {day}")
