#!/usr/bin/env python 2.7

abs_ex = abs(-5)
print "abs() is %d" % abs_ex

all_ex1 = all([1, 2, 3, 4])
print "all([]) is %s" % all_ex1

all_ex2 = all([1, 2, 0])
print "all([]) returns false when False is in iterable data: %s" % all_ex2

any_ex1 = any([1, 0])
print "any() returns if True exists %s" % any_ex1

chr1 = chr(97)
print "chr() returns char. matches to ASCII codes ex. 97 %s" % chr1
ord1 = ord('a')
print "ord() returns ASCII code which matches to char. ex 'a' %d" % ord1

divmod1 = divmod(11, 3)
print "divmod() returns tuple form of quotient/remainder " + str(divmod1)

for i, name in enumerate(['1st', '2nd', '3rd', '4th']):
    print "enumerate returns index and the variable %d index / %s data" % (i, name)


def positive(x):
    return x > 0


print "filter func: "
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

a1 = 3
b1 = a1
print "id returns reference of variable. a1 = %d, b1 = %d, 3 = %d" % (id(a1), id(b1), id(3))


class person:
    pass


a = person()
print "isinstance returns if it is the instance of the class ex. a = person() %s" %isinstance(a, person)

print "len of python %d" % len("python")
print "len of [1,2,3,4,5] %d" % len([1, 2, 3, 4, 5])

print "list makes iterable data into list ex. 'python' and 1, 2, 5, 6, 8"
print list("python")
print list((1, 2, 5, 6, 8))

print "max() min() of [1, 4, 5, 100, -55] %d/ %d" %(max([1, 4, 5, 100, -55]), min([1, 4, 5, 100, -55]))

print "pow(a,b) = a^b"

for i in range(5):
    print "range(5)-> index %d" % i

for i in range(5, 11):
    print "range(5, 11) -> index %d" % i

for i in range(0, -10, -2):
    print "range(0, -10, -2) -> index %d" % i

print "round((5.6789, 2) %f" % round(5.6789, 2)

print "sortted([3, 1, 2])"
print sorted([3, 1, 2])
print "a.sort() -> sort() of list doesnt have return value."
