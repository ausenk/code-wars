import pytest
from sieve_of_eratosthenes import is_prime, sieve_of_eratosthenes

# Test cases
s1 = 2
s2 = 3
s3 = 13
s4 = 14

@pytest.mark.parametrize(
    'num, prime', [
        (s1, True), 
        (s2, True), 
        (s3, True), 
        (s4, False)
    ]
)
def test_is_prime(num, prime):
    assert is_prime(num) == prime


@pytest.mark.parametrize(
    'num, prime', [
        (s1, [2]), 
        (s2, [2, 3]), 
        (s3, [2, 3, 5, 7, 11, 13]), 
        (s4, [2, 3, 5, 7, 11, 13])
    ]
)
def test_sieve_of_eratosthenes(num, prime):
    assert sieve_of_eratosthenes(num) == prime