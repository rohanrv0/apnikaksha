import random
top_of_range = input("enter top range of your game : ")
#method for asking number greater than 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time")
        quit()
else:
    print("please enter a number next time")
    quit()
#method ends
guess = 0
number = random.randint(0,top_of_range)
while True:
    guess +=1
    num1 = input ("enter your guess: ")
    if num1.isdigit():
        num1 = int(num1)
    else:
        print("Please type a number next time. ")
        continue
    if num1 == number:
        print("You got it correct.")
        print("you took " + str(guess) + " guess to find the answer..")
        break
    elif num1 > number:
        print("smaller")
    else:
        print("greater")
 
    
    







