"""This is a combination of functions to be able to try the correctness of math operation testing py.test
the mathematical function is described with the parameters and the matematical operation, 
as an example simple_div(a,b)=parameters, return(a/b)=mathematical function"""
"""first operation"""
def simple_add(a,b):
    return a+b
"""second operation"""
def simple_sub(a,b):
    return a-b
"""third operation"""
def simple_mult(a,b):
    return a*b
"""fourth operation"""
def simple_div(a,b):
    return a/b
"""Fifth operation"""
def poly_first(x, a0, a1):
    return a0 + a1*x
"""sixth operation"""
def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# ..

