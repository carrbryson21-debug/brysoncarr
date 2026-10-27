#goal is to make a really cool project date late did 10/26/2026
# goal 1 reached of making it reads word numbers as numbers 10/27/2026
#tommorws goal to handle input validation and make sure it will try again if they type random things 10/28/2026
import sys
from word2number import w2n
import sys

start_message=input("welcome to my inventory program if you want to enter type enter and if you want to exit type exit")
if start_message=="exit":
    print("goodbye")
    sys.exit(0)
name=input("enter your name")
print("welcome ",name)
items=["cups", "lids", "plates"]
quanities=[0,0,0]
while start_message!="exit":


    print("this is how manny items you have the items in this tracker are cups lids and plates and this is how manny you have of each in this tracker", quanities)
    choice=input("would you like to add or remover an item if so just put the name add or subtract? and the amount you would like to add or subtract?")
    if choice=="exit":
        choice=input("are you sure you want to exit? y/n")
        if choice=="y":
            print("goodbye", name)
            break

        elif choice=="n":
            print("okay then stay")

    elif choice == "add cups":
        choice=(input("how manny would you like to add?"))

        if quanities[0] <=5:
            print("you are in low stock")
        choice= w2n.word_to_num(choice)
        quanities[0]+= choice


    elif choice == "subtract cups":
        choice=(input("how manny would you like to subtract?"))
        if quanities[0] >0:
            choice = w2n.word_to_num(choice)
            quanities[0]-= choice
            if quanities[0] <=5:
                print("you are in low stock")

        else:
            print("you can't do that")




    if choice == "add lid":
        choice=(input("how manny would you like to add?"))
        choice= w2n.word_to_num(choice)
        quanities[1]+= choice
        if quanities[1] <=5:
            print("you are in low stock")


    elif choice == "subtract lid":
        choice=(input("how manny would you like to subtract?"))
        if quanities[1] >0:
            choice = w2n.word_to_num(choice)
            quanities[1]-= choice
            if quanities[1] <=5:
                print("you are low in stock")

        else:
            print("you can't do that")


    if choice == "add plate":
        choice=(input("how manny would you like to add?"))
        choice= w2n.word_to_num(choice)
        quanities[2]+= choice
        if quanities[2] <=5:
            print("you are in low stock")

    elif choice == "subtract plate":
        choice=(input("how manny would you like to subtract?"))
        if quanities[2] >0:
            if quanities[2] <0:
                print("you can't do that")
            choice= w2n.word_to_num(choice)
            quanities[2]-= choice
            if quanities[2] <=5:
                print("you are in low stock!!")

        else:
            print("you can't do that")

    def show_items():
        print("cups:",quanities[0])
        print("lids:",quanities[1])
        print("plates:",quanities[2])
        print("inventory total:",quanities[2] + quanities[1] + quanities[0])
    show_items()

