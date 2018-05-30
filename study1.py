#!/usr/bin/env python2.7


def calc_ex(choice, *args):
    if choice is "sum":
        result = 0
        for i in args:
            result += i
        return result

    elif choice is "mul":
        result = 1
        for i in args:
            result *= i
        return result

    else:
        raise Exception("Invalid command")


def dict_ex(**kwards):
    for key, value in kwards.iteritems():
        print "%s = %s" % (key, value)


def sayName(name, old, gender=True):  # (name, gender=True, old)-> compileError
    if gender is True:
        print "My name is %s, I'm %d years old and I'm man" % (name, old)
    else:
        print "My name is %s, I'm %d years old and I'm woman" % (name, old)


a_ex = 1


def global_ex():
    global a_ex
    a_ex = a_ex + 1
    print(a_ex)
    a_ex = 11


if __name__ == '__main__':
    res1 = calc_ex("sum", 1, 2, 3, 4, 5)
    res2 = calc_ex("mul", 1, 2, 3, 4, 5)
    print (res1)
    print (res2)
    # res3 = calc_ex("div", 1, 5)
    dict_ex(age=30)
    sayName("park", 23)
    sayName("kim", 22, False)
    global_ex()
    print(a_ex)

    sum_lambda = lambda a, b : a + b
    res_lamb = sum_lambda(3, 4)
    print res_lamb
    list_lambda = [lambda a, b : a + b, lambda a, b : a * b]
    print list_lambda[0](4, 5)
    print list_lambda[1](2, 5)

# end
