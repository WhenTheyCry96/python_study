#!usr/bin/env python2.7


def input_ex():
    in1 = raw_input("Raw Input = ")
    print "Raw Input = what you input : %s" % (in1)
    in2 = input("Input- only int/float = ")
    print "Input = what you input : %s" % (in2)


# if __name__ is '__main__':
input_ex()
print ("Quotation_mark" "uses")
print ("You" + "can" + "add by +")
print ("You", "can", "add by ,")

"""
f = open("text.txt", "w")

for i in range(1, 11):
    f.write("%dth line \n" % (i))

f.close()
"""

f2 = open('text.txt', 'a')
f2.write("added line")
f2.close()

f1 = open("text.txt", "r")
lines = f1.readlines()
for line in lines:
    print line

f1.close()
