###Test program, without a function


def error_handling(number1, number2, operator):


    try: 
        int(number1)
       
        
    except:
        return "Error: Numbers must only contain digits."

    try:
        int(number2)
    except:
        return "Error: Numbers must only contain digits."
        ### Tries to turn the numbers into integers, if fails, print error messag


    try:
        if len(number1) > 4 or len(number2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
         
       ### Checks the length of numbers
    try:
        if operator != "+" and operator != "-":
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
        
         ### Checks wether plus or minus sign is used, doesn't allow other signs

    
    return ""



def arithmetic_arranger(problems, results=False):

    start = True
    spaces = "    "  
    op1 = op2 = op3 = op4 = ""
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."

    for i in range(0, len(problems)):
        items = problems[i].split()
        num1 = items[0]
        sign = items[1]
        num2 = items[2]

        err = error_handling(num1, num2, sign)

        if err != "":
            return err
            
            
            
        
        space = max(len(num1), len(num2))
        num1_int = int(num1)
        num2_int = int(num2)

        if start == True:
            op1 += num1.rjust(space + 2)
            op2 += sign + " " + num2.rjust(space)
            op3 += "-" * (space + 2)
            start = False
            if results == True:
                if sign == "+":
                    op4 += str(num1_int + num2_int).rjust(space + 2)
                else:
                    op4 += str(num1_int - num2_int).rjust(space + 2)

        else:
            op1 += num1.rjust(space + 6)
            op2 += sign.rjust(5) + " " + num2.rjust(space)
            op3 += spaces + "-" * (space + 2)

            if results == True:
                if sign == "+":
                    op4 += spaces + str(num1_int + num2_int).rjust(space + 2)
                else:
                    op4 += spaces + str(num1_int - num2_int).rjust(space + 2)
    

            
    if results == True:
        return op1 + "\n" + op2 + "\n" + op3 + "\n" + op4
    return op1 + "\n" + op2 + "\n" + op3
    ## Output conditionals





    
