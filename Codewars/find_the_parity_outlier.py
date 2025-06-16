def find_outlier(integers):
    pair_count: list[int] = []
    odd_count: list[int] = []
    for i in integers:
        if(i % 2 == 0):
            pair_count.append(i)
        else:
            odd_count.append(i)
        if(len(odd_count)>1 and len(pair_count)>0):
            return pair_count[0]
        elif(len(pair_count)>1 and len(odd_count)>0):
            return odd_count[0]
            

"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
 The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
   Write a method that takes the array as an argument and returns this "outlier" N.
"""