def sieve_of_eratosthenes(limit: int):
    ''' Finds all the prime numbers up to a given limit '''
    primes = []
    for k in range(2, limit):
        if is_prime(k):
            primes.append(k)
    
    print(primes)
    return primes



def is_prime(num: int) -> bool:
    ''' Returns boolean based on if the input integer is prime'''
    sum = 0
    for k in range(2, num-1):
        if (num % k == 0):
            sum += 1

    if sum == 0:
        return True
    else:
        return False