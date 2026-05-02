from main import add

# osnovni
def test_add_positive():
    assert add(2, 3) == 5

# negativna
def test_add_negative():
    assert add(-2, -3) == -5

# kombinacija
def test_add_mixed():
    assert add(-2, 5) == 3

# decimalna števila
def test_add_float():
    assert add(2.5, 3.5) == 6.0