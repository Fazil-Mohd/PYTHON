n=input("Enter The String")

vowels_count=0
vowels = ['a','e','i','o','u']
for char in n:
    if char in vowels:
        vowels_count+=1
print("vowelss=",vowels_count)
    
