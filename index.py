first_number=int(input("please input any digit number "))
operation=input("please input the operation you'd want to use e.g. +, -, *, /  ")
second_number=int(input("please input any digit number "))
if operation=="+":
    print(f"{first_number} {operation}  {second_number}")
    result=first_number+second_number
    print(f"the result is {result}")
elif operation=="-":
    print(f"{first_number} {operation}  {second_number}")
    result=first_number-second_number
    print(f"the result is {result}")
elif operation=="*":
    print(f"{first_number} {operation}  {second_number}")
    result=first_number*second_number
    print(f"the result is {result}")
elif operation=="/":
    print(f"{first_number} {operation}  {second_number}")
    result=first_number/second_number
    print(f"the result is {result}")
else:
    print("invalid operation")
