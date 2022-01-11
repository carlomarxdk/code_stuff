def multiples(number):
    div3 = 3 * ((number-1)//3) * (((number-1)//3) + 1) / 2
    div5 = 5 * ((number-1)//5) * (((number-1)//5) + 1) / 2
    div3_5 = 15 * ((number-1)//15) * (((number-1)//15) + 1) / 2
    sum =  div3 + div5 - div3_5
    if number < 0:
        return 0
    return sum
        