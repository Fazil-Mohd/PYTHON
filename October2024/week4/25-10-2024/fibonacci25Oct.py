n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    first = 0
    second = 1
    print("Fibonacci Series:")
    for i in range(n):
        if i <= 1:
            result = i
        else:
            result = first + second
            first = second
            second = result
        print(result)
