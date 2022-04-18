import re
game = True
#playerName = ""

valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#while game:
    
def get_Name():
    playerName = input("What is your name: ").upper()
    
    if all(char in valid_char for char in playerName):
        print("Thank you " + playerName)
        
                
    else:
        print("Invalid character")
            
    

#get_Name()

#playerAge = int(input("What is your age: "))