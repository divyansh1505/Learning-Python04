# Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

n = int(input("Enter the number : "))

i=1
for i in range(n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print(" ")

