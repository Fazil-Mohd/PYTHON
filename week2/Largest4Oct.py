n1=int(input("ENTER THE FIRST NUMBER"))
n2=int(input("ENTER THE SECOND NUMBER"))
n3=int(input("ENTER THE THIRD NUMBER"))

if n1>n2 and n1>n3 :
       largest = n1
elif n2>n1 and n2 >n3:
         largest = n2
else:
        largest =n3

print ("Larest Number Is ",largest)
