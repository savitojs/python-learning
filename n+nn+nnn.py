# Python program to read a number n+nn+nnn.

n = int(input("enter the number: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print "The value is :" , comp