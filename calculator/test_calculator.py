import calculator

#def test_calculator():
    #assert calculator.add(0,0) == 0
    #assert calculator.add(-1, -1) == -2
    #assert calculator.add(4, 5) == 9

def test_calculator():
    manyadds = (1, 2, 3, 4)
    assert calculator.add(manyadds) == 10

#def test_multipy():
    #manynumbers = (1, 2, 3)
    #assert calculator.multiply(manynumbers) == 6
