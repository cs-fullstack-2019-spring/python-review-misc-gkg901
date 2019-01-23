def main():
    # ex1()
    ex2()


# Create a function that has a loop that quits with q. If the user doesn't enter q, ask them to input another string.
# BONUS: Make sure the code can handle whatever case the User enters the q as (uppercase or lowercase).


def ex1():

    passW = "code"

    while (True):
        ask = input("enter password. q to quit")
        if ask == passW:
            print("Access Granted")
            break
        elif ask == "q".upper():
            break

        elif ask == "Q".lower():
            break




def ex2():






    def ex2Helper(num1,num2,num3,operation):
        if operation == "add":
            print("The SUM of "+ str(num1),str(num2),str(num3)+ " is "+str((num1+num2+num3)))

        elif operation == "prod":
            print("The PROD of "+ str(num1),str(num2),str(num3)+ " is " + str((num1*num2*num3)))
        elif operation == "avg":
            print("The AVG of "+ str(num1),str(num2),str(num3)+ " is " + str((num1+num2+num3)/3))
        elif operation != "add" or operation !="prod" or operation !="avg":
            print("INVALID OPERATION")




    ex2Helper(2,3,4,"add")
    ex2Helper(2,3,4,"prod")
    ex2Helper(2,3,4,"avg")

























if __name__ == '__main__':
    main()