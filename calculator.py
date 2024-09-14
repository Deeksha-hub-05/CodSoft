# task-2 CALCULATOR

print("---CALCULATOR---")

num1= int(input("Enter the first number here: "))
num2= int(input("Enter the second number here: "))

print("press 1 for addition\n press 2 for subtraction\n press 3 for multiplication\n press 4 for division")

choice=int(input("Enter your choice from 1-4: "))

if choice==1:
  print("The addition of above two numbers is",num1+num2)

elif choice==2:
  print("The subtraction of above two numbers is",num1-num2)

elif choice==3:
  print("The multiplication of above two numbers is",num1*num2)

elif choice==4:
  print("The division of above two numbers is",num1/num2)
  
else:
  print("Invalid Input")