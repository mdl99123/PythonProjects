""" Roll dice simulator """

import random
option="-1"


while option!="n":
    option="-1"
    frequency=[0,0,0,0,0,0]
    print("Enter amount of dice rolls for the simulation")
    total=input()

    for i in range(int(total)):
        face=random.randrange(1,7)
        frequency[face-1]+=1

    for i in range(6):
        print("Face "+str(i+1)+" appears a total of "+str(frequency[i])+" times")
    
    while option!="y" and option!="n":
        print("Do you wish to retry the simulation y/n")
        option=input()