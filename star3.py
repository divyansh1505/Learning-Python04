""" Write a program to print the following star pattern.
* * *
*   *            for n = 3
* * *  """

n = int(input("Enter a number : "))
i = 1
for i in range(1, n+1):
    if (i==1 or i == n):
       print("*"*n)
    else:
       print("*", end="")
       print(" "*(n-2), end="")
       print("*")

# python automatically prints the next thing in the next 
# line, to change that (make it like default C), we Use
# end = ()