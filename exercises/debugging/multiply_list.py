def multiply_list(lst):
    for idx, item in enumerate(lst):
        lst[idx] = item * 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# Multiple all elements in the list by 2 

