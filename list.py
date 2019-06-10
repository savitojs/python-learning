# python program for list

a = [1,2,3,4,5,6]
print a[1]

b = [1,'a',2,'b',3]
print b[2]

c = ["apple",[1,2,3,4,5],[9,8,7,6,5]]
print c[0][2]
print c[1][3]
print c[2][1]

d = ['a','b','c','d','e','f','g','h','i','j']
print d[1:3]
print d[3:]
print d[:5]
print d[:]

e = [1,2,3]
e.append(4)# for adding one value
print e

e.extend([5,6,7])# for adding more elements
print e

print(e+[8,9])#'+'can also used for adding elements

print '[a]'*5
print [4]*5

f = [1,2,3,4,5]
f.insert(1,9)
print f

g = [1,2,3,4,5]
g[1] = 9
print g
g[2:4] = [7,8]
print g
g[2:2] = [7,8]
print g
g[3:3] = [3,3,3]
print g

h = [1,2,3,4,5,1,1,2]
del h[2]
print h
del h[2:4]
print h

h.remove(1)
print h
h.remove(2)
print h


i = [1,2,3,4,5,6,7]
print i.pop(1)
print i.pop()
print i.pop()
print i

j = [4,3,6,2,8,9,1]
print j.index(6)
print j.count(6)
j.sort()
print j
j.reverse()
print j