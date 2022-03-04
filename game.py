import random

def rockPaperScissor(user):
    
    # using random funciton for choosing option randomly
    option = ["Rock","Paper","Scissor"]
    computer = random.choice(option)
    
    # Rock part
    if user == 1 :
        if computer == "Paper" :
            print("Computer choose",computer,"you lost !","\U0001f915")
        elif computer == "Rock" :
            print("Computer choose",computer,"Draw no one win the match :(")
        else:
            print("Computer choose",computer,"You Win the game Hurray ! \U0001f929")
     
    #Paper part 
    elif user == 2:
        if computer == "Scissor" :
            print("Computer choose",computer,"you lost!","\U0001f915")
        elif computer == "Paper" :
            print("Computer choose",computer,"Draw no one win the match :(")
        else:
            print("Computer choose",computer,"You Win the game Hurray ! \U0001f929")
            
    # Scissor part
    elif user == 3:
        if computer == "Rock" :
            print("Computer choose",computer," you lost !","\U0001f915")
        elif computer == "Scissor" :
            print("Computer choose",computer,"Draw no one win the match :(")
        else:
            print("Computer choose",computer,"You Win the game Hurray ! \U0001f929")
    else:
        print('INVALID OPTION!!!!!')
      

user = int(input("Please choose any option for game \n 1.Rock \n 2.Paper \n 3.Scissor :-"))
rockPaperScissor(user)


