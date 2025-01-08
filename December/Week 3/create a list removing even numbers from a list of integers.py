# Input a list of integers from the user
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

# Create a new list with only odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Display the result
print("List after removing even numbers:", odd_numbers)
