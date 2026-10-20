days = ["mon", "tues", "weds", "thurs", "FRIDAY!!!"]
print(f"Initial 'days': {days}")

# Another name for the same list: aliasing (both refer to the same object)
moredays = days
print(f"'moredays' is an alias: id(days) == id(moredays) is {id(days) == id(moredays)}")

# Mutating through the alias
moredays[4] = "fri"
print(f"After 'moredays[4] = \"fri\"':")
print(f"  moredays: {moredays}")
print(f"  days:     {days}  <-- mutated as well due to aliasing!")

# Creating an independent shallow copy
yetmoredays = days.copy()  # an actual copy, not an alias
yetmoredays[0] = "YAWN!"
print(f"After 'yetmoredays[0] = \"YAWN!\"':")
print(f"  yetmoredays: {yetmoredays}")
print(f"  days:        {days}  <-- unchanged because yetmoredays is a copy!")
print(f"  id(days) == id(yetmoredays): {id(days) == id(yetmoredays)}")

