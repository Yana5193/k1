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
if name == '__main__':
    test_addition_basic()
    test_bug_addition_notsufficent()
    test_bug_addition_enough()
