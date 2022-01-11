def reverse(x: int) -> int:
    if x == 0:
        return 0
        
    digits = int(math.log10(abs(x))) + 1
    number = 0
    for i in range(digits-1, -1, -1):
        curr = (abs(x)//10**i) % 10
        number += curr * 10**(digits-1-i)
        
    if abs(number) > 2**31 and number != 2**31 - 1:
        return 0

    return int(number * math.copysign(1, x))