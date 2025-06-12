def solution(a):
    if len(a) % 2 != 0:
        a += '_'
    pairs = []

    for i in range(0, len(a), 2):
        pair = a[i:i+2]
        pairs.append(pair)
    return pairs
print(solution("abcde"))

'''
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
'''