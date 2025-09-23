def format_name(first_name, last_name):
    fn = first_name.title()
    ln = last_name.title()
    complete_name = (f"The complete name is {fn} {ln}")
    return complete_name

print(format_name("darshan", "prashanth"))

###########################################################

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("Hello"))    #passing function as an input to another function
print(output)

###########################################################
# more return values

def format_name_1(first_name, last_name):
    if first_name == "" or last_name == "":
        return ("Please enter the valid input.")
    fn = first_name.title()
    ln = last_name.title()
    complete_name = (f"The complete name is {fn} {ln}")
    return complete_name

print(format_name_1(input("What is your first name? "), input("What is your last name? ")))


