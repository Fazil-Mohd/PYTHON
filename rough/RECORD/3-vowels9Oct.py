n=input("Enter The String: ")

vowels_count=0
vowels = ['a','e','i','o','u','A','E','I','O','U']

for char in n:
    if char in vowels:
        vowels_count+=1
        print(char)
print("vowels=",vowels_count)


     
