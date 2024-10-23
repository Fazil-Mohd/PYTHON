my_list= list(map(int,input("Enter The Elemets Two the List Sepate it by space").split()))

minimum = min(my_list)
maximum = max(my_list)

count_num = int(input("Enter The Number To Count"))
count = my_list.count(count_num)

total = sum(my_list)
my_list.reverse()

my_list.sort()

print("Minimum value:", minimum)
print("Maximum value:", maximum)
print("Count of ",count_num,":", count)
print("Total sum:", total)
print("Reversed list:", my_list)
print("Sorted list:", my_list)
