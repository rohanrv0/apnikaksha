import random

user_wins = 0
com_wins = 0

option = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type rock/paper/scissors or Q to quit : ").lower()
    if user_input == "q":
        print("Thanks for playing..")
        print("your points are",str(user_wins),(".."))
        print("computer's points are", str(com_wins),(".."))
        quit()
        

    if user_input not in option:
        print("Type a valid option..")

        continue

    
    
    else:
        num = random.randint(0,2)
    
        #rock=0,,paper=1,,scissors=2..
        com_pick = option[num]
        print("you chose "+ user_input+ "..")
        print("computer chose "+ com_pick + "..")
        

        if com_pick == option[0]:
            if user_input=="rock":
                print("It's a draw..")

            elif user_input=="paper":

                print("You won")
                user_wins+=1
            else:
                print("You lost..")
                com_wins+=1
        elif com_pick == option[1]:
            if user_input=="paper":
                print("It's a draw..")
                
            elif user_input=="scissors":

                print("You won")
                user_wins+=1
            else:
                print("You lost..")
                com_wins+=1


        elif com_pick== option[2]:
            if user_input=="scissors":
                print("It's a draw..")
                
            elif user_input=="rock":

                print("You won")
                user_wins+=1
            else:
                print("You lost..")
                com_wins+=1

            

        
    
        


    



    


