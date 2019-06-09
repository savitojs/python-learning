# Python program to calculate the average of numbers in a given list

n = int(input("enter the total number of elements: "))
a = []
for i in range (0,n):
    elem = float(input("enter the element(s): "))
    a.append(elem)
    avg = sum(a)/n
    
print "Average of element(s) in list is:",round(avg,2)

