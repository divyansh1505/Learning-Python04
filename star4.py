n = int(input("Enter an odd number: "))

if n % 2 == 0:
    print("Please enter an odd number.")
else:
    # Upper part (including the middle row)
    for i in range(1, (n // 2) + 2):
        print(" " * ((n // 2) + 1 - i) + "*" * (2 * i - 1))

    # Lower part
    for i in range((n // 2), 0, -1):
        print(" " * ((n // 2) + 1 - i) + "*" * (2 * i - 1))

# The expression n // 2 in Python is floor division. 
# It divides n by 2 and returns the quotient,
# discarding any remainder (or fractional part).