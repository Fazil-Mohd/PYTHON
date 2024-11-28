def menu():
    print("\nMenu:")
    print("1. Check if the lists are of the same length")
    print("2. Check if the lists sum to the same value")
    print("3. Check if any value occurs in both lists")
    print("4. Exit")
    return int(input("Enter your choice: "))

def check_same_length(list1, list2):
    return len(list1) == len(list2)

def check_same_sum(list1, list2):
    return sum(list1) == sum(list2)

def check_common_values(list1, list2):
    common = set(list1) & set(list2)
    return common if common else None

def main():
    list1 = list(map(int, input("Enter the integers for List 1 separated by spaces: ").split()))
    list2 = list(map(int, input("Enter the integers for List 2 separated by spaces: ").split()))

    while True:
        choice = menu()

        match choice:
            case 1:
                if check_same_length(list1, list2):
                    print("The lists are of the same length.")
                else:
                    print("The lists are of different lengths.")
            case 2:
                if check_same_sum(list1, list2):
                    print("The lists sum to the same value.")
                else:
                    print("The lists do not sum to the same value.")
            case 3:
                common_values = check_common_values(list1, list2)
                if common_values:
                    print("Common values:", common_values)
                else:
                    print("No common values found.")
            case 4:
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please try again.")
main()
