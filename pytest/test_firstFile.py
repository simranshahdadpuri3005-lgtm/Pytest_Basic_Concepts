import pytest



def test_function1(firstfixture):  # to link fixture and fucntion, we need to pass fixture as parameter in the function
    print("inside function1")

def test_function2():
    print("inside function2")

def test_function3(firstfixture):
    print("inside function3")