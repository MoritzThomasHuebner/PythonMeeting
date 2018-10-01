import numpy as np
a = [1, 2, 4]



def func1():
    print('a')

def func2():
    print('b')

def mutable_list(c=func1):
    c()
    global func1
    func1 = func2

mutable_list()
mutable_list()
mutable_list()
mutable_list()
mutable_list()
func1()
