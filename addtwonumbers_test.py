import addtwonumbers;

def test_case1():
    assert addtwonumbers.getSomeOfTwoNumbers(2,5) == 7;
     
def test_case2():
    assert addtwonumbers.getSomeOfTwoNumbers(2,6) == 8;    
    
def test_case3():
    assert addtwonumbers.getSomeOfTwoNumbers(0,0) == 0;

def test_case4():
    assert addtwonumbers.getSomeOfTwoNumbers(-2,3) == 1;
