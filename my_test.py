from bytest.decorations import testcase

@testcase
def test_a():
    assert 1 == 1

@testcase
def test_b():
    assert 1 == 1
    

@testcase
def test_c():
    assert 1 == 2