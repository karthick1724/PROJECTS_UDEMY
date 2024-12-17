#Calculator_project

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def calculator():
    symbols = {"+":add, "-":subtract, "*":multiply, "/":divide}
    n1 = int(input("Type the first number: "))
    repeat = True
    while repeat:
        operation = input("Type a mathematical operator as follows:  '+','-', '*', '/'")
        n2 = int(input("Type the second number: "))
        if operation == "+":
            answer = symbols["+"](n1,n2)
        elif operation == "-":
            answer = symbols["-"](n1,n2)
        elif operation == "*":
            answer = symbols["*"](n1,n2)
        elif operation == "/":
            answer = symbols["/"](n1,n2)

        print(answer)


        should_continue = input("Do you want to continue with existing answer or new one?: ").lower()

        if should_continue == "yes":
            n1 = answer   
        else:
            repeat = False
            calculator()
    


calculator()


    