#!usr/bin/env python2.7


class calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

    def printself(self):
        print "youNeedTotakeSelf as variable1"

    def safe_sum(a, b):
        if type(a) is not type(b):
            print ("Non-addable")
            return
        else:
            result = a + b
            return result


class SonCalc(calculator):
    def __init__(self):
        print "This is son class of calc"

    def calcpow(self):
        a = input("a^b of a")
        b = input("a^b of b")
        self.result = (a * b)
        return self.result

    def adder(self, num):
        if num < 0:
            print "you are adding negative num"
            print "Method overriding"


class dataProcess:
    def __init__(self, data):
        self.tmpData = data.split("|")
        self.name = self.tmpData[0]
        self.age = self.tmpData[1]


if __name__ is '__main__':

    cal2 = SonCalc()
    cal2_res = cal2.calcpow()
    print cal2_res

    cal1 = calculator()
    print type(cal1)
    print type(calculator())
    print(cal1.adder(10))
    data = dataProcess("Hong|45")
    print data.name
