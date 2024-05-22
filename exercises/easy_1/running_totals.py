"""
PROBLEM
- Inputs: list of integer numbers (N elements)
- Outputs: list of N elements, with each element - running total of the input list, starting from corresponding element (
    e.g. 2nd element in output is sum of 1st and 2nd element of the input list).
- Explicit Requirements:
    - Output list has same number of eleemnts as input list
    - In output list, each element of input list is replaced with running total up to the element's position.
    
    - 
- Implicit Requirements:
    - Empty list returns empty list 
    - Output for one number is the same as input 
    - The element itself is included in the running total calculation (e.g. 2nd element running total is 1st + 2nd elements)

- Questions:
    - Assumption that the input will always be a list of integers (no input validation)
    - Assumption that we return a new object (new lsit with same number of elements)

- Sequence: 
[2, 5, 13]
[2, 2 + 5, 2 + 5 + 13]
[pos 0, pos 0 + pos 1, pos 0 + pos 1 + pos 2]. 

EXAMPLES:
- [2, 5, 13]) ==> [2, 7, 20]
- [14, 11, 7, 15, 20]) ==> [14, 25, 32, 47, 67]
- [] => []
- [3] => [3]


DATA STRUCTURES
List

Algorithm:
initialize totals list to empty list 
Outer loop  - iterate through each element of input list. For each:
    initialize total to element in index 0 
    Inner loop - iterate from element index 1 until current element, included. 
        for each iteration, add the current element to the total
    end inner loop
    add the total to the list. 
end outer loop
return the list 

"""

def running_total(numbers):
    totals = []

    for index, number in enumerate(numbers):
        total = 0
        
        for preceding_number in numbers[:index+1]:
            total += preceding_number 
        
        totals.append(total)

    return totals


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True


""" ALTERNATIVE LS STAFF SOLUTION 

1. Keep a running total that starts at 0 and is incremented by going through 
each number. 
2. By going through each number, add the new total to the list. 

result_list = []
    total = 0

    for num in nums:
        total += num
        result_list.append(total)

    return result_list

This solution is much simpler. I wonder why I haven't thought about it.

I should have seen it in my sequence mapping that previous element is being repeated (first 2, then 2+5, etc. )

[2, 5, 13]
[2, 2 + 5, 2 + 5 + 13]

"""