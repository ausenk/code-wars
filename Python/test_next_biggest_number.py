import pytest
from next_biggest_number import nextBiggestNumber

# Test cases
s1 = 245
s2 = 5467743
s3 = 112356
s4 = 123456789

@pytest.mark.parametrize(
    'num, biggest_num', [
        (s1, 542), 
        (s2, 7765443), 
        (s3, 653211), 
        (s4, 987654321)
    ]
)
def test_next_biggest_number(num, biggest_num):
    assert nextBiggestNumber(num) == biggest_num