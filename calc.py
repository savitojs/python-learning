# Python program to find the sum of first n numbers

number = int(raw_input("Sum of first number(s): "))
result = 0
for num in range(number):
    result = result + num

print"Sum of first",number," number is:",result