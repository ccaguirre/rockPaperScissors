'''
Created on Apr 25, 2020

@author: ITAUser
'''
'''
Created on Apr 25, 2020

@author: ITAUser
'''
import random

#set computer to zero
#set player to zero
print("welcome to Vitrual Rock Paper Scissors Bruhhhhh!"   )


def usermv():
    move = input("Yo Bra Make Ya Move:")
   
    return move.strip()

def computers(): 
    A = ["rock", "scissors", "paper"]
   
    commv = random.choice(A).strip()
    
    return commv



def wincheck():
    
    if (commv == "paper"):
       
        if (player == "paper"):
          
            return "you tied bruv"
       
        elif (player == "scissors"):
           
            return "you won bruv"
       
        elif (player == "rock"):
           
            return "you lost bruv"
        
        else:
         
            return "bruh you gotta  type 'rock', 'paper', or 'scissors' it's not that hard"   
   
    elif (commv == "rock"):
        
        if (player == "scissors"):
           
            return "You lost again bro"
        
        elif (player == "rock"):
            
            return "you tied again bro"
        
        elif (player == "paper"):
           
            return "You won again bro" 
        
        
        else:
          
            return "bruh you gotta  type 'rock', 'paper', or 'scissors' it's not that hard" 
    
    elif (commv == "scissors"):
        
        if (player == "scissors"):
            
            return "Bruu you done diddily tied Again"
        elif (player == "rock"):
           
            
            return "Bruu you done didilly won Again"
        elif (player == "paper"):
            
           
            return "Bruu you done diddily lost again"
        else:
           
            return "bruu you gotta  type 'rock', 'paper', or 'scissors' it's not that hard" 
        

keep = 2


while keep == 2:

    player = usermv()

    commv = computers()
   
    print("Yo breh the computer chose " + commv)    
    
    print(wincheck())
    
    


