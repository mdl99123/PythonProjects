import math

def holder():
   option=input('Press any key to continue')
   return option

def Evaluator(args):
    size=len(args)
    print("Using ceil to round to smallest integer not less than x")
    for i in range(size):
     print(math.ceil(args[i]))
    holder()

    print("Using floor to round to the largest integer not greater than x")
    for i in range(size):
     print(math.floor(args[i]))
    holder()

    print("Using the sin function to calculate the Trigonometric sin of x")
    for i in range(size):
     print(math.sin(args[i]))
    holder()

    print("Using the cos function to calculate the Trigonometric cos of x")
    for i in range(size):
     print(math.cos(args[i]))
    holder()

    print("Using the tan function to calculate the Trigonometric tan of x")
    for i in range(size):
     print(math.tan(args[i]))
    holder()

    print("Using the exp function to calculate calculate the e of x")
    for i in range(size):
     print(math.exp(args[i]))
    holder()

    print("Using the log(x) function to calculate the natural lograithm of x")
    for i in range(size):
     print(math.log(args[i]))
    holder()

    print("Using the log10(x) function to calculate the lopgarithm of x base 10")
    for i in range(size):
     print(math.log10(args[i]))
    holder()

    print("Using the pow function to calculate x raised tp the power of x")
    for i in range(size):
     print(math.pow(args[i],args[i]))
    holder()

    print("Using the sqrt function to calculate the square root of x")
    for i in range(size):
     print(math.sqrt(args[i]))
    holder()

    print("Using the fabs function to calculate the absolute value of x")
    for i in range(size):
     print(math.fabs(args[i]))
    holder()

    return None

"""This program accepts as input a list of numbers that will then be evaluated to a set of commonly used functions of the math module"""


arr=[]
arr2=[]
MainOption="-1"
inp=" "
print("-----------------Main Menu-----------------")
while MainOption!="n":
    print("Input a list of values that you wish to evaluate separated by space")
    inp=input()
    arr=inp.split()
    for i in range(len(arr)):
        arr2.append(int(arr[i]))

    Evaluator(arr2)
    print()
    print()
    while MainOption!="y" and MainOption!="n":
     print("Do you wish to evaluate more numbers y/n")
     MainOption=input()


