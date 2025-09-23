def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

'''
# we can store the function "add" (say) in a variable by just assigning it to a variable
addition_operator = add
addition_operator(2, 5)    # this will call add function now(passing the arguments to it as well)
'''

operator_dict = {
    "+": add, "-": sub,
    "*": mul, "/": div
}

def calculator():
    calculate = True
    n1 = float(input("What's the first number? "))

    while calculate:
        for key in operator_dict:
            print(key)
        operator = input("Pick an operator: ")
        n2 = float(input("What's the next number? "))

        solution = operator_dict[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {solution}")
    
        wants_to_continue = input("Do you want to continue calculating?\nType 'Yes' to continue with previous value.\nType 'No' to start from the beginning.\nType 'Exit' to exit the program. ").lower()
        if wants_to_continue == 'no':
            #n1 = float(input("What's the first number? "))
            calculator()
        elif wants_to_continue == 'yes':
            n1 = solution
        else:
            calculate = False
            print("Thanks for using the calculator.\nRerun the program to calculate more.")
            exit(0)

calculator()
