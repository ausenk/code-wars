

def nextBiggestNumber(num: int):
    '''
    This function takes a positive integer and returns 
    the next bigger number that can be formed by rearranging its digits.
    '''

    for x in iter(str(num)):
        print(x)


nextBiggestNumber(1245)