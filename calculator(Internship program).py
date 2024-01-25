#To write a program to perform calulator operations

#The input values for the calulation operation are obtained below 
inp1=int(input("Enter the first number : "))
inp2=int(input("Enter the first number : "))
#The choice for the operation is made 
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("press 4 for division")
#These all above print statements are printed as such
choice=int(input("Enter the choice for calculation : "))
if choice==1:
    print("The sum of given values is : ",inp1+inp2)
elif choice==2:
    print("The subtracted value is : ",inp1-inp2)
elif choice==3:
    print("The multiplied value is : ",inp1*inp2)
elif choice==4:
    print("The divided value is : ",inp1/inp2)
else:
    print("Choose a choice within the given options")

