def flatten(arr, depth = -1):

    if depth == 0:
        return arr
    
    ret_arr = []

    for x in arr:
        if isinstance(x, list):
            ret_arr += flatten(x, depth - 1)

        else:
            ret_arr += [x]

    return ret_arr



print(flatten([1, 2, 4, [[5]]], 1))                                 #   [1, 2, 4, [5]]

print(flatten([1, 2, 3, [[[4, 5, [6]]], 7]], 2))                    #   [1, 2, 3, [4, 5, [6]], 7]

print(flatten([1, 2, [[[[[[[[[[[[[[[[[[[4]]]]]]]]]]]]]]]]]]]]))     #   [1, 2, 4]
