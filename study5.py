#!/usr/bin/env python2.7

try:
    r = file.open('DoesntExist')

except:  # do not use bare except
    print "Doesn't Exist"

try:
    inNum = raw_input("OnlyNumber : ")
    r = open('DoesntExist', 'r')

except IOError as e:
    print str(e)
    pass

else:
    data = r.read()

if __name__ is '__main__':
    print "Error passed"
print"Error Passed"


class myError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def say_nick(nickN):
    if nickN is 'idiot':
        raise myError("Not Available Nickname")
    print (nickN)


try:
    say_nick("idiot")

except myError as e:
    print e
