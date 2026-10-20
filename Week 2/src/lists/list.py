days = ["mon", "tues", "weds", "thurs", "fri"]

# Index-based iteration
for day_num in range(0, len(days)):
    print(day_num, days[day_num])

# Direct element iteration
for day in days:
    print(day)

# Idiomatic iteration using enumerate()
for day_num, day in enumerate(days):
    print(f"Day {day_num + 1} ({day_num}): {day}")
