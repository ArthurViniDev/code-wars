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
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.