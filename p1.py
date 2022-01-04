

# A. Given an array A of N integers, write a function missing_int(A) that returns the smallest
# positive integer (greater than 0) that does not occur in A.
# ● A = [1, 3, 6, 4, 1, 2] should return 5
# ● A = [1, 2, 3] should return 4
# ● A = [-1, -1, -1, -5] should return 1
# ● A = [1, 3, 6, 4, 1, 7, 8, 10] should return 2

# Problem A Solution
from typing import List


def missing_int(A: List[int]) -> int:
    for i in range(1, len(A) + 2):
        if i not in A:
            return i


# print(
#     missing_int([1, 3, 6, 4, 1, 7, 8, 10])
# )

# B. Write a function find_divisible(a, b, k) that accepts three integers: a, b and k, and returns
# the total count of the numbers between a and b (inclusive) that are divisible by k
# ● find_divisible(6,11,2) should return 3. 6, 8, and 10 are all divisible by 2.
# ● find_divisible(0,12,3) should return 5. 0, 3,6, 9, and 12 are all divisible by 3.


# Problem B solution
def find_divisible(a:int, b:int, k:int) -> str:
    num_range = list(range(min(a, b), max(a, b) + 1))
    nums = [i for i in num_range if i % k == 0]

    return len(nums)

print(
    find_divisible(0, 12, 3)
)    

# C. Write a rotate(A, k) function which returns a rotated array A, k times; that is, each
# element of A will be shifted to the right k times
# ● rotate([3, 8, 9, 7, 6], 3) returns [9, 7, 6, 3, 8]
# ● rotate([0, 0, 0], 1) returns [0, 0, 0]
# ● rotate([1, 2, 3, 4], 4) returns [1, 2, 3, 4]


