import math
def narcissistic( value ):
    digits = int(math.log10(value)) + 1
    res = 0
    for i in range(digits):
        res+= (value // 10**i % 10)**digits
    if value == res:
        return True
    return False