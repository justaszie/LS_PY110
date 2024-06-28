"""
PROBLEM
- Input: list
- Output: sorted list
- Rules:
    - List will contain at least 2 eleemnts
    - Sorting is done in-place, doesn't return new object
    - List can contain numeric values or strings. The elements will be compared using standard Python comparison logic


ALGORITHM
1. Keep on iterating over the input list. On each iteration:
    1. Iterate over each pair of elements in the list. (from pair of indexes 0 - 1 to indexes -2 -1)
    For each pair:
        - if the 1st element is greater than the 2nd element of the pair, swap their positions
    (to swap, use a temp variable)
    2. If none of the pairs were swapped, stop iterating over the lists and return it

Iterate over elements from index 0 to index - 2, incl. Each iteration compare elements current, current + 1
"""


def bubble_sort(lst):
    while True:
        swapped = False
        for idx in range(0, len(lst) - 1):
            if lst[idx] > lst[idx + 1]:
                swapped = True

                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]

        if not swapped:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True