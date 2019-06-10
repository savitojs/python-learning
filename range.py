#Python program to print all numbers in range divisible by a given number

lower = int(input("Enter the lower range limit: "))
upper = int(input("Enter the upper range limit: "))
n = int(input("Enter the number to be divided by: "))
for i in range(lower, upper+1):
    if(i%n==0):
        print(i)