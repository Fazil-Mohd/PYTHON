def input_dict(prompt):
    print(prompt)
    n = int(input("Enter the number of key-value pairs: "))
    result = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        result[key] = value
    return result

dict1 = input_dict("Input the first dictionary:")
dict2 = input_dict("Input the second dictionary:")

merged_dict = {**dict1, **dict2}

print("Merged Dictionary:", merged_dict)
