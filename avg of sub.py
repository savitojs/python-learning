# Program to take in the marks of three subjects and display the grade

sub1 = int(input("Enter the marks of first subject: "))
sub2 = int(input("Enter the marks of second subject: "))
sub3 = int(input("Enter the marks of third subject: "))

avg = (sub1 + sub2 + sub3)/3
print "DEBUG: Vaule of AVG is:",avg
if(avg>=90):
    print "Grade : A"
elif(avg>=75 and avg<90):
    print "Grade : B"
elif(avg>=60 and avg<75):
    print "Grade : C"
else:
    print" FAIL"