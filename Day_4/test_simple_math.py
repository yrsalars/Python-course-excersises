#%%
import simple_math

def test_simple_add():
    assert simple_math.simple_add(0,7) == 7

def test_simple_sub():
    assert simple_math.simple_sub(0,7) == -7

def test_simple_mult():
    assert simple_math.simple_mult(0,7) == 0

def test_simple_div():
    assert simple_math.simple_div(2,1) == 2

def test_poly_first():
    assert simple_math.poly_first(0,0,7) == 5

def test_poly_second():
    assert simple_math.poly_second(0,0,7) == 5
