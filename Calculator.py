print("Welcome to the Calculator: ")
cont=1
while (cont):
    print("Enter the First Number: ")
    num1=int(input())
    print("Choose the Operations ( + , - , * , / )")
    op=input()
    print("Enter the Second Number: ")
    num2=int(input())
    if op== "+":
        print(f"The sum of {num1} & {num2} is {num1+num2}.")
    elif op=="-":
        print(f"The difference of {num1} & {num2} is {num1-num2}")
    elif op=="*":
        print(f"The product of {num1} & {num2} is {num1*num2}")
    elif op=="/":
        print(f"The division of {num1} & {num2} is {num1/num2}")
    else:
        print("Invalid Operator!!")
    print("Wanna try again!(1 for Yes/0 for No)")
    cont=int(input())


