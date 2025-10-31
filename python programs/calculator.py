a = float(input("enter the first number"))
b = float(input("enter the second number"))
c = input("Write the operation you want to perform") 

calc_dict = {
    "Multiply" : a*b,
    "Divide" : a/b,
    "Subtract" : a-b,
    "Add" : a+b,
    "Exponent" : a**b,
    "Remainder": a%b,
    "Square of first number": a*a,
    "Square of second number": b*b,
        }

if b == 0:
    if c == "Divide":
        print("Cannot divide by 0")
    else:
        if c == "Multply":
           print(calc_dict["Multply"])
        elif c == "Divide":
            print(calc_dict["Divide"])
        elif c == "Subtract":
            print(calc_dict["Subtract"])
        elif c == "Add":
            print(calc_dict["Add"])
        elif c == "Exponenet":
            print(calc_dict["Exponent"])
        elif c == "Remainder":
            print(calc_dict["Remainder"])
        
        else:
            print("not calculabel")

    
    

