def validate_pin(pin):
    if(len(pin) != 4 and len(pin) != 6): return False

    for i in range(len(pin)):
        if '0' <= pin[i] <= '9':
            continue
        else:
            return False
    return True

"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""