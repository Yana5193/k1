import sys
sys.path.append('../src')

from math_demo import add, add_with_bug

def test_addition_basic():
    assert add(2,2) == 4, "Function didn't returned 4"
    print("Test BASIC ADDITION PASSED")

def test_bug_addition_notsufficent():
    assert add_with_bug(2,2) == 4, "Function didn't returned 4"
    print("Test BUG ADDITION PASSED")

def test_bug_addition_enough():
    assert add_with_bug(2,2) == 4, "Function didn't returned 4"
    assert add_with_bug(0,0) == 0, "Function didn't returned 0"
    #assert add_with_bug(5,6) == 11
    print("Test BUG ADDITION PASSED")
def test_addition_dublicated_logic():
    #bad test since it relies on absense of "+" in add()
    assert add(6,3) == 6+3
    print("Test DUBLICATED LOGIC PASSED (could get some bugs in)")
    #good test since input and output are independent in add()
    assert add(6,3) == 9
    print("Test DUBLICATED LOGIC PASSED")
def test_addition_overcomplicated():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i,j) == i+j
            assert add(-i, j) == -i + j
            assert add(i, -j) == i - j
            assert add(-i, -j) == -i - j

def test_addition_reasonable():
    assert add(6,3 ) == 9
    assert add(0, 3) == 3
    assert add(0, -3) == -3
    assert add(-7, 83) == 76
    assert add(-7, -83) == -90
    print("Test ADDITION REASONABLE PASSED")

def test_add_something_reasonable():
    assert add_something(6,3) == 9
    assert add_something(None,None) == 0
    assert add_something(None,"abc") == 0
    assert add_something(None, 10) == 0
    assert add_something("abc", "10") == "abc10"
    assert add_something("10", "abc") == "10abc"
    assert add_something("xyz", "abc") == "xyzabc"
    print("Test ANOTHER ADDITION REASONABLE PASSED")
if name == '__main__':
    test_addition_basic()
    test_bug_addition_notsufficent()
    test_bug_addition_enough()
    test_addition_dublicated_logic()
    test_addition_reasonable()
    test_add_something_reasonable()
