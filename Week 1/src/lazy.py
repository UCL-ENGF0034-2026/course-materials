x = 0
y = 3

# Short-circuit evaluation (lazy evaluation of logical operators):
# In an 'and' expression, if the left operand evaluates to False, Python immediately
# stops evaluating further operands because the whole expression cannot be True.
# This prevents a ZeroDivisionError (y // x) when x == 0.

if x != 0 and y // x > 2:
    print("Hello")

x = 1
if x != 0 and y // x > 2:
    print("World")