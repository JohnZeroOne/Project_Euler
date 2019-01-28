##def calcFib(x):
##    """ x is how many times we want to calc fib"""
##
##    assert isinstance(x, int)
##
##    if x <= 0:
##        return None
##    elif x == 1 or x == 2:
##        return 1
##    else:
##        return calcFib(x-1) + calcFib(x-2)
##        

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

##while n < 40000000:
##    if n % 2 == 0:
##        y += n
##return y

#4.mil is somewhere between f 33 and f 34

def f(n, r, y):
    """
    n is fib to calculate
    r is the sum of fib
    y is the sum of even numbers in fib
    """
    a, b = 0, 1
    while c < 40000000:
        c = a + b
        if r % 2 == 0:
            y += n
        
    return y
        
