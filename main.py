# This is Project 1/5 from the freeCodeCamp Scientific Computing with Python Course - The Arithmetic Arranger

###Test program, without a function

list = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
spaces = "    "  
op1 = op2 = op3 = op4 = ""

for i in range(0, len(list)):
    items = list[i].split()
    num1 = items[0]
    sign = items[1]
    num2 = items[2]


    ### Output conditionals

    if len(num1) > 3 or len(num2) > 3:

        print("{0:>6}".format(num1))
        print("{0:>0}".format(sign),"{0:>4}".format(num2))
        print("{0:>4}".format("-"*6))


    elif len(num1) > 2 or len(num2) > 2:
        print("{0:>5}".format(num1))
        print("{0:>0}".format(sign),"{0:>3}".format(num2))
        print("{0:>4}".format("-"*5))


    else:
        print("{0:>4}".format(num1))
        print("{0:>0}".format(sign),"{0:>2}".format(num2))
        print("{0:>4}".format("-"*4))












# for i in range(1,11):
#     print("{0:>6s}".format(str(i)))
#     print("{0:>6s}".format(str(i)*2))
#     print("{0:>6s}".format("-"*8))



### The eval() function is only to be used when the second argument of the arithmetic_arranger function is set to True, to display results

# def arithmetic_arranger(problems):
#     for i in range(0, len(the_list)):
#         compute = eval(the_list[i])
#         print(compute)