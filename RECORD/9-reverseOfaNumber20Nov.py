def read_number():
    while True:
        number = int(input("Enter a number (minimum 4 digits): "))
        if number >= 1000:
            return number
        else:
            print("Please enter a number with at least 4 digits.")

def reverse_number(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number 

def main():
    number = read_number()
    reversed_number = reverse_number(number)
    print("Original number:", number)
    print("Reversed number:", reversed_number)

main()
