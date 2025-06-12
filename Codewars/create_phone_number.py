def create_phone_number(a):
    numb = ''
    for i in range(len(a)):
        if i == 0:
            numb += '('
        if i == 3:
            numb += ') '
        if i == 6:
            numb += '-'
        numb += str(a[i])
    return numb