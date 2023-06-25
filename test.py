# Test First TDD cycle 1


def test1():
    assert multiply(1, 1) == 1  # first test for TDD cycle 1 has failed.


# Get the test to pass by writing the multiply function.

def multiply(a, b):
 return a * b


# Test first TDD cycle2.
# Test first TDD cycle2 test1.
def test2():
    assert multiply(2, 2) == 4  # first test of cycle 2 failed.


# TDD cycle1 and cycle2 should pass the test.
def multiply(a, b):
    return a * b

#Test first TDD cycle3.
def test3():
    assert multiply(3,3)==9 #TDD cycle3 test1 failed.

#get test to pass by writing multiply function.
def multiply(a, b):
    return a * b #TDD cycle3 test2 passed.

#TDD test cycle4.
def test4():
    assert multiply(4,4)==16 #TDD cycle4 test1 failed

def multiply(a,b):
    return a * b #cycle4 test2 passed

#Fifth test cycle.
def test5():
    assert multiply(23,45)==1035 #fifth cycle test 1 failed

def multiply (a,b):
    return a * b# fifth cycle test2 passed


