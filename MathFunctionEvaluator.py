import math

def holder():
   option=input('Press enter key to continue')
   return option

def ceil(args,size):
    print("Using ceil to round to smallest integer not less than x")
    for i in range(size):
     print(math.ceil(args[i]))
    holder()

def floor(args, size):
    print("Using floor to round to the largest integer not greater than x")
    for i in range(size):
     print(math.floor(args[i]))
    holder()

def sin(args, size):
    print("Using the sin function to calculate the Trigonometric sin of x")
    for i in range(size):
     print(math.sin(args[i]))
    holder()

def cos(args, size):
    print("Using the cos function to calculate the Trigonometric cos of x")
    for i in range(size):
     print(math.cos(args[i]))
    holder()

def tan(args, size):
    print("Using the tan function to calculate the Trigonometric tan of x")
    for i in range(size):
     print(math.tan(args[i]))
    holder()

def exp(args, size):
    print("Using the exp function to calculate calculate the e of x")
    for i in range(size):
     print(math.exp(args[i]))
    holder()

def log(args, size):
    print("Using the log(x) function to calculate the natural lograithm of x")
    for i in range(size):
     print(math.log(args[i]))
    holder()

def log10(args, size):
    print("Using the log10(x) function to calculate the lopgarithm of x base 10")
    for i in range(size):
     print(math.log10(args[i]))
    holder()

def pow(args, size):
    print("Using the pow function to calculate x raised tp the power of x")
    for i in range(size):
     print(math.pow(args[i],args[i]))
    holder()

def sqrt(args, size):
    print("Using the sqrt function to calculate the square root of x")
    for i in range(size):
     print(math.sqrt(args[i]))
    holder()

def fabs(args, size):
    print("Using the fabs function to calculate the absolute value of x")
    for i in range(size):
     print(math.fabs(args[i]))
    holder()

def Evaluator(args):
    size=len(args)
    ceil(args,size)
    floor(args, size)
    sin(args, size)
    cos(args, size)
    tan(args, size)
    exp(args, size)
    log(args, size)
    log10(args, size)
    pow(args, size)
    sqrt(args, size)
    fabs(args, size)

    return None

"""This program accepts as input a list of numbers that will then be evaluated to a set of commonly used functions of the math module"""


arr=[]
arr2=[]
MainOption="-1"
inp=" "
print("-----------------Main Menu-----------------")
while MainOption!="n":
    MainOption='-1'
    print("Input a list of values that you wish to evaluate separated by space")
    inp=input()
    arr=inp.split()
    try:
        for i in range(len(arr)):
            arr2.append(int(arr[i]))  
        Evaluator(arr2)
    except BaseException:
        print("Error most likely due to wrong input, please enter numbers only and separated by space")
    print()
    print()
    while MainOption!="y" and MainOption!="n":
     print("Do you wish to evaluate more numbers y/n")
     MainOption=input()



