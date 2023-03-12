#
# Print "Hello World" if a is greater than b.
a = 50
b = 10
if a > b:
    print("Hello World")


# This example misses indentations to be correct.
# Insert the missing indentation to make the code correct:

if 5 > 2:
    print("Five is greater than two!")

# Use the correct short hand syntax to write the following conditional expression in one line:
if 5 > 2:
    print("Yes")
else:
    print("No")

print("Yes") if 5 > 2 else print("No")


i = 1
while i in range(1, 6):
    print(i)
    i += 1
else:
    print(f"i is no longer in range(1,6)")
