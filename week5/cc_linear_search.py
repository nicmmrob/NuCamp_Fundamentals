def linear_search_dictionary(a_dict, target):
    for value in a_dict:
        if a_dict[value] == target:
            print(f"Found at key: {value}.")
            return value
    print("Target is not in the dictionary.")
    return None

# another way to search, just not linear
    # if x in dict.values():
    #     print("Target found.")
    #     return x
    #print("Target was not found.")
    # return None


# Code Tests:
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
