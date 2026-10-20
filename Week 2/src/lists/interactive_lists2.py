days = ["mon", "tues", "weds", "thurs", "fri"]
print(f"Initial days: {days}")

# I don't like Mondays: delete first item
del days[0]
print(f"After 'del days[0]': {days}")

# OK, add Monday back at the beginning
days.insert(0, "mon")
print(f"After 'days.insert(0, \"mon\")': {days}")

# In-place item mutation at index 4
days[4] = "FRIDAY!!!"
print(f"After 'days[4] = \"FRIDAY!!!\"': {days}")

