print("Welcome to this Fun game of MATHS. ")
name = input("enter your name : ")
score = int(0)
print("Here is first question for you. ")
print("How many prime numbers are there in first 100 natural numbers.")
answer1 = int(input("enter your answer : "))
if answer1 != 25 :
    print("Incorrect") 
    
else:
    print("You are correct :)")
    score += 1
print("Next question.")
answer2 = int(input("20+(7*4/2)*2: "))
if answer2 != 48 :
    print("Incorrect.  ")
    
else: 
    print("Brilliant,   ")
    score +=1
print("Next question.")
answer3= int(input("What is the answer if we multiply 2 to itself 10 times: "))
if answer3 != 1024 :
    print("Incorrect. ")
    
else: 
    print("Brilliant,   ")
    score +=1



print("Next question.")
answer4 = (input("which common shape has no edges and corners: "))
if answer4 != "circle" :
    print("Incorrect.")
    
else: 
    print("Brilliant,   ")
    score +=1

print("Next question.")
answer5 = int(input("(25*9)/3: "))
if answer5 != 75 :
    print("Incorrect.")
    
    
else: 
    print("Brilliant,   ")
    score +=1

print("Next question.")
answer6 = int(input("Area of square of side length 8: "))
if answer6 != 64 :
    print("Incorrect.")
    
else: 
    print("Brilliant,   ")
    score += 1

print("Next question.")
answer7= int(input("Perimeter of rectangle of l= 9, b=5: "))
if answer7 != 28 :
    print("Incorrect.")
    
    
else: 
    print("Brilliant, one more to go..  ")
    score +=1
print("Next question.")
answer8 = int(input("Calculate the cost of painting upper rectangle if rate is 4rs/1 unit sq.: "))
if answer8 != 112 :
    print("Incorrect.")
    
    
else: 
    print("Fabulous")
    score+=1
print("YOU HAVE Finished THIS GAME ..  ")
   
print("Your score is '" + str(score) + "' out of 8")
    