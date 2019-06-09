# Python program to reverse a string

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s = raw_input("Type any string: ")
print "Original string :", s

print "New string :", reverse(s) 
