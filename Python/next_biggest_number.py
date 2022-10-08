import math

def nextBiggestNumber(num: int):
    '''
    This function takes a positive integer and returns 
    the next bigger number that can be formed by rearranging its digits.
    '''
    digits = []
    for x in iter(str(num)):
        digits.append(x)

    digits.sort()
    
    k = 0
    biggest_num = 0
    for x in digits:
        biggest_num += int(x) * 10 ** k
        k += 1
    
    return biggest_num

