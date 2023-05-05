


import matplotlib.pyplot as plt
import numpy as np

option="-1"
while option!="2":
# 100 linearly spaced numbers
    option="-1"
    x = np.linspace(-5,5,100)
  
    # the function, which is y = x^2 here
    print("Please enter the polynomial function in the format of the following example(x**2 + 7*x + 6): ")
    y = input()
    y=eval(y)
    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x,y, 'r')

    # show the plot
    plt.show()
    while option!="1" and option!="2":
        print("Please choose one of the following options: ")
        print("1.- Would you like to enter another function?: ")
        print("2.- Exit the program")
        option=input()
