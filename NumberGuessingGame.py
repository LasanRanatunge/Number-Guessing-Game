#Built-in library
import random

#initializing and creating variables 
name = ""
secret_code = []
guess = []
attempt = 0
attempt_limit = 8
correct_guess = 0
choice = ""
game_active = 0
multiplier = 2.1
points = []
max_points = 0


#Game is active....
game_active = True

while game_active:

    #getting user input
    name = str(input("Enter your name: "))

    #Welcoming the user and giving instruction....
    print("                        ","HI",name,"Welcome to GameInt")
    print("\nNumber to Guess - XXXX","                              ","Color Mapping:")
    print("                                                             ", "1-White  2-Blue  3-Red")
    print("                                                             ", "4-Yellow  5-Green  6-Purple")

    #Generating random secret_code.....
    secret_code = [random.randrange(1, 6,) for i in range(4)]

    #Checking attempt count
    while attempt < attempt_limit:
        

        #Getting user inputs 
        guess.append(int(input("enter number 1: ") or -1))
        guess.append(int(input("enter number 2: ") or -1))
        guess.append(int(input("enter number 3: ") or -1))
        guess.append(int(input("enter number 4: ") or -1))
     

        #Checking whether the user wants to exit the game...
        
        if guess[0] == 0 and guess[1] == 0 and guess[2] == 0 and guess[3] == 0: 

          # Checking whether the length of points list is not 0...
          if len(points) != 0:             
     
            max_points = max(points)

          #If length of the points list is 0...set max points to 0
          else:
            max_points = 0

          #Calculating total points in each round by multiplying the max points from the max list with the mutltiplier
          total_points = multiplier*max_points
        
          print("\nYou have scored",round(total_points),"points!!")
          guess.clear()
          break

        #Checking whether the user inputs are in 0-6 range....
        elif guess[0] <= 6 and guess[0] >= 0 and guess[1] <= 6 and guess[1] >= 0 and guess[2] <= 6 and guess[2] >= 0 and guess[3] <= 6 and guess[3] >= 0:
            
            print(" ")
            #Incrementing attempts.....
            attempt = attempt+1

            #Reducing the multiplier by 0.1 on each attempt...
            multiplier = multiplier - 0.1
                

            #Checking whether guessed numbers are correct/ in randsom list/ wrong....
            if guess[0] == secret_code[0]:
                correct_guess = correct_guess+1 
                guess_0 = "1"
              
            elif guess[0] in secret_code:
                guess_0 = "0"
            elif guess[0] not in secret_code:
                guess_0 = "."

            if guess[1] == secret_code[1]:
                correct_guess = correct_guess+1
                guess_1 = "1"
                
            elif guess[1] in secret_code:
                guess_1 = "0"
            elif guess[1] not in secret_code:
                guess_1 = "."

            if guess[2] == secret_code[2]:
                correct_guess = correct_guess+1
                guess_2 = "1"
              
            elif guess[2] in secret_code:
                guess_2 = "0"
            elif guess[2] not in secret_code:
                guess_2 = "."

            if guess[3] == secret_code[3]:
                correct_guess = correct_guess+1
                guess_3 = "1"
        
            elif guess[3] in secret_code:
                guess_3 = "0"
            elif guess[3] not in secret_code:
                guess_3 = "."


            #Allocating points according to user input....
            if correct_guess == 4:
               points.append(50)
            elif correct_guess == 3:
               points.append(37.5)
            elif correct_guess == 2:
               points.append(25)
            elif correct_guess == 1:
               points.append(12.5)
            
   
            print(" ")

            #Printing the 3 coloumns
            print("Attempt No","                  ","Guess","        ","Result")

            #Printing the User inputs and the 2 Pegs above
            print(" ",attempt,"                        ",guess[0],guess[1],guess[2],guess[3],"        ", guess_2,guess_1)

            #Printing the Bottom 2 Pegs
            print("                                             ", guess_3,guess_0)

            #Printing the horizontal line
            print("____________________________________________________________________________________________")

            #Print congrats if the user guessed all 4 numbers...
            if correct_guess == 4:
              print(" ")
              
              print("Congratulations!!! You have won the game....")

              #Retrieving the max points of the user among his attempts...
              max_points = max(points)
              total_points = multiplier*max_points
            
              #display score....
              print("\nYou have scored",round(total_points),"points...")

              #Resetting attempt after successful guess
              attempt = 0
              guess.clear()
              correct_guess = 0
              points = []
              multiplier = 2.1
              break
              
            else:
              #If the user fails to guess continues to the next attempt
              if attempt != 8:
                  guess.clear()
                  correct_guess = 0
                  continue  
              else:
                if len(points) != 0:
                  max_points = max(points)
                else : 
                  max_points = 0;
                total_points = multiplier*max_points
                print("You have scored",round(total_points),"points...")
                print()
                guess.clear()
                correct_guess = 0
                points = []

        #Display message when user inputs invalid inputs
        else:
            print("\nInvalid inputs") 
            print("Reminder! =>> All inputs must be in 0-6 range <<=")
            print("\nEnter the inputs again")
            guess.clear()


    #Asking whether the player wants to play another game.....
    choice=input("\nDo you want to play another game? ( Yes/No ):")

    #Repeat    
    if choice=="Yes" or choice=="YES" or choice=="yes":
        print(" ")
        print(" ")
        #Resetting the variables
        attempt = 0
        multiplier = 2.1
        points = []
        max_points = 0
        continue
    
    #Exit 
    elif choice=="No" or choice=="NO" or choice=="no":
        print(" ")
        print("Exit......")        
        game_active = False

    #Termination due to invalid input    
    else:
        print("Game terminated....")
        break  

       



                    
    





        

       



                    
    





        
