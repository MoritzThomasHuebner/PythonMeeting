# A short demonstration as to what can go wrong with mutable default arguments


def do_something(a = [1, 2, 3]):
    print(a)
    a[2] = 0

do_something()
do_something()
