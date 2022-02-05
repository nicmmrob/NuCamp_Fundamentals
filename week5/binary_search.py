def binary_search(the_list, target):
    lower_bound = 0  # setting the parameters for the start and the end of the binary search
    # since it's a zero index list, we need to deduct 1 from the length
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:  # if the lower_bound becomes greater than the upper,
        # then that means the target is not in the list and will exit the loop
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot  # we have found the target
        if pivot_value > target:
            upper_bound = pivot - 1  # we are discarding the upper bound and moving the pivot
        else:
            lower_bound = pivot + 1  # we are discarding the lower bound and moving the pivot

    # will return -1 as the list is a zero index list and -1 doesn't exist as an index.
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 10))
print(binary_search(my_list, 4))
print(binary_search(my_list, 33))
