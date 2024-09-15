# Initialize an empty list to store the numbers
number = []

for i in range(4):
       a = int(input("Enter your number: "))
       number.append(a)

# Unpack the list elements into variables a, b, c, d
a, b, c, d = number 

# Find the greatest number using if-elif statements
if(a>b and a>c and a>d):
         print(a)
elif(b>a and b>c and b>d):
        print(b)
elif(c>a and c>b and c>d):
        print(c)
else :
        print(d)

print("Above number is the greatest of all those entered")