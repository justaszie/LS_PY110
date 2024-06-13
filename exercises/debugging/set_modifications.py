# We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?

data_set = {1, 2, 3, 4, 5}

new_set = set() 

for item in data_set:
    if item % 2 != 0:
        new_set.add(item)

print(new_set)