def get_key_value(my_dict, key):
    if key in my_dict   :
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

# check if key exists and return value.Currently error 

# my_dict[key] reference raises exception. We need to check if key is in dict first