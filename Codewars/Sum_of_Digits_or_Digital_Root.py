def digital_root(n: int) -> int:
    while(n>=10):
        strn=str(n)
        nums=[int(d) for d in strn]
        n = sum(nums)
    return n
"""
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
"""