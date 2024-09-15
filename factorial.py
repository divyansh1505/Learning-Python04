# n = int(input("Enter : "))

# i=1
# fact = 1
# while i<n+1:
#     fact=fact*i
#     if (n==0):
#         print("1")
# else:
#     print(fact)



n = int(input("Enter : "))

# Handle the case where n is 0
if n == 0:
    print("1")  # 0! is 1
else:
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    print(fact)