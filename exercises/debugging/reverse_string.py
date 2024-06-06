def reverse_string(string):
    result = ''
    for char in string:
        # print(f'{}')
        result = char + result

    return result

print(reverse_string("hello"))
print(reverse_string("hello") == "olleh")

# Reverse a string passed as an argument

