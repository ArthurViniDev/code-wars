def is_square(n):
    if(n < 0):
        return False
    for i in range(n+1):
        if i*i == n:
            return True
        elif i*i > n:
            break
    return False

"""
Task
Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
The tests will always use some integral number, so don't worry about that in dynamic typed languages.
"""