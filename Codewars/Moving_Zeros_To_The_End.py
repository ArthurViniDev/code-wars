def move_zeros(lst: list[int]) -> list[int]:
    no_zeros: list[int]=[]
    zeros_list: list[int]=[]
    for i in range(len(lst)):
        if lst[i]!=0:
            no_zeros.append(lst[i])
    zeros_list = [0] * (len(lst) - len(no_zeros))
    return no_zeros + zeros_list