days = ["mon", "tues", "weds", "thurs", "fri"]
print(f"Initial weekdays: {days}")

# How many weekdays are there?
count = len(days)
print(f"Count of days: {count}")

# What's the second day of the week?
day2 = days[2]  # "weds"
print(f"days[2] returns: {day2!r} (third element due to 0-based indexing)")

# Oops, indices start at zero!
# What's the second day of the week?
day2 = days[1]  # "tues"
print(f"days[1] returns: {day2!r} (second element)")

# Add the weekend
days.append("sat")
days.append("sun")
# days is now ["mon", "tues", "weds", "thurs", "fri", "sat", "sun"]
print(f"After appending weekend: {days}")
