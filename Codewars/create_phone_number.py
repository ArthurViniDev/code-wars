def solution(a):
    numb = ''
    for i in range(len(a)):
        if(i == 0):
            numb += '('
            numb += str(a[i])
        elif(i == 3):
            numb += ')'
            numb += ' '
            numb += str(a[i])
        elif(i == 6):
            numb += '-'
            numb += str(a[i])
        else:
            numb += str(a[i])
    return numb

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(solution(numbers))