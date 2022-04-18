import mysql.connector
import logging



name = ""
fairy = ""
babyDragon = ""   
babyDragonDamage = ""
goldUnicorn = ""
goldUnicornDamage = ""
playerName = ""
playerAge = ""
endGameHealth = 0
playerHealth = 3
valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
game = True

       

playerName = input("What is your name: ").upper()
playerAge = int(input("What is your age: ")) 

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "ProgramWithNoFears920",
database = "python_game_with_mysql",
)
#print(mydb)

# Create Cursor Instance
my_cursor = mydb.cursor()

#Create A Database
#my_cursor.execute("CREATE DATABASE python_game_with_mysql") 

# Show Database
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)

#Create Table
#my_cursor.execute("CREATE TABLE Players ( user_id INT AUTO_INCREMENT PRIMARY KEY, playerName VARCHAR(255) NOT NULL, playerAge INT NOT NULL, playerHealth INT, fairy VARCHAR(255), babyDragon VARCHAR(255), goldUnicorn VARCHAR(255), endGameHealth INT)")

def set_player_health():
    global playerHealth
    print("")
    print( playerName + " has taken damage!!!")
    playerHealth -= 1
    #print("")
    #print(playerName + " your health level is " + playerHealth)
    #print("")


#pet baby dragon
def goldUnicornDamage():
    print("")
    print("Why would anyone pet a baby dragon. The mommy dragon could have eaten you")
    print("")
    print("The final creature in your test is a Gold Unicorn. pet it or do not pet")
    print("")
    goldUnicornDamage1 = input("Type yes Pet it or no Not to Pet: ").lower()
    resultSet5 = "UPDATE Players SET goldUnicorn = %s WHERE playerName = %s" 
    answer5 = (goldUnicornDamage1, playerName)
    my_cursor.execute(resultSet5, answer5)
    mydb.commit() 

    #didnt pet fairy, pet baby dragon, pet gold unicorn
    if (goldUnicornDamage1 == "pet it"):
        print("")
        print(" You never touch the gold Unicorn.")
        print("")
        print(" You have lost all your health. You have LOST THE GAME.... BETTER LUCK NEXT TIME.")
        print("")
        print(" Total health points left: " + str(playerHealth))
        print("")
        resultSet6 = "UPDATE Players SET endGameHealth = %s  WHERE playerName = %s"
        answer6 = (playerHealth, playerName)
        my_cursor.execute(resultSet6, answer6)
        mydb.commit() 
        game = False
        
                
    # didn't pet fairy, pet baby dragon, didn't pet gold unicorn    
    elif (goldUnicornDamage1 == "do not pet" and playerHealth == 2):
        print("")
        print("Good choice not to pet the Gold Unicorn. You have ended the game with 2 points. ")
        print("")
        print("Well done. You have WON THE GAME")
        print("")
        print(" Total health points left: " + str(playerHealth))
        print("")
        resultSet7 = "UPDATE Players SET endGameHealth = %s  WHERE playerName = %s"
        answer7 = (playerHealth, playerName)
        my_cursor.execute(resultSet7, answer7)
        mydb.commit() 
        game = False
        

    #didn't pet fairy, pet baby dragon, didnt pet gold unicorn    
    elif (goldUnicornDamage1 == "do not pet" and playerHealth == 1):
        print("")
        print(" It's always a good idea to never touch the mystical unicorn. You have ended the game with 1 point.")
        print("")
        print("You could have done better. But either way,  You have WON THE GAME")
        print("")
        print(" Total health points left: " + str(playerHealth))
        print("")
        resultSet8 = "UPDATE Players SET endGameHealth = %s  WHERE playerName = %s"
        answer8 = (playerHealth, playerName)
        my_cursor.execute(resultSet8, answer8)
        mydb.commit() 
        game = False
        
            
            
            
# do not pet baby dragon
def goldUnicorn():
    print("")
    print("Good Choice... Why would anyone pet a baby dragon. The mommy dragon would have eaten you.")
    print("")
    #print(" Your health is now 2. Your health points are getting low. Be careful.")
    print("")
    print("The final creature in your test is a Gold Unicorn. pet it or do not pet")
    print("")
    goldUnicorn1 = input("Type yes Pet it or no Not to Pet: ").lower()
    resultSet9 = "UPDATE Players SET goldUnicorn = %s WHERE playerName = %s" 
    answer9 = (goldUnicorn1, playerName)
    my_cursor.execute(resultSet9, answer9)
    mydb.commit()  

    #didnt pet fairy, pet baby dragon, pet gold unicorn
    if (goldUnicorn1  == "pet it" and playerHealth > 0): 
        print("")
        print(" You never touch the gold Unicorn.")
        print("")
        print(" Total playerHealth points left: " + str(playerHealth))
        print("")
        print(" Great Job. You have WON THE GAME")
        resultSet10 = "UPDATE Players SET endGameHealth = %s  WHERE playerName = %s"
        answer10 = (playerHealth, playerName)
        my_cursor.execute(resultSet10, answer10)
        mydb.commit() 
        game = False
        

        #pet fairy, didn't pet baby dragon, didn't pet gold unicorn    
    elif (goldUnicorn1  == "do not pet" and playerHealth == 3): 
        print("")
        print("Good choice not to pet the Gold Unicorn. You have ended the game with all your health points ")
        print("")
        print("Great Job. You have WON THE GAME")
        print("")
        print(" Total health points left: " + str(playerHealth))
        resultSet11 = "UPDATE Players SET endGameHealth = %s  WHERE playerName = %s"
        answer11 = (playerHealth, playerName)
        my_cursor.execute(resultSet11, answer11)
        mydb.commit() 
        game = False
        #DOESNT END GAME LOOP

    # didn't pet fairy, pet baby dragon, didn't pet gold unicorn    
    elif (goldUnicorn1  == "do not pet" and playerHealth == 2):
        print("")
        print("Good choice not to pet the Gold Unicorn. You have ended the game with 2 points. ")
        print("")
        print("Well done. You have WON THE GAME")
        print("")
        print(" Total health points left: " + str(playerHealth))
        resultSet12= "UPDATE Players SET endGameHealth = %s  WHERE playerName = %s"
        answer12 = (playerHealth, playerName)
        my_cursor.execute(resultSet12, answer12)
        mydb.commit() 
        game = False

    # didn't pet fairy, pet baby dragon, didnt pet gold unicorn    
    elif (goldUnicorn1  == "do not pet" and playerHealth == 1):
        print("")
        print(" It's always a good idea to never touch the mystical unicorn. You have ended the game with 1 point.")
        print("")
        print("You could have done better. But either way,  You have WON THE GAME")
        print("")
        print(" Total health points left: " + str(playerHealth))
        resultSet13 = "UPDATE Players SET endGameHealth = %s  WHERE playerName = %s"
        answer13 = (playerHealth, playerName)
        my_cursor.execute(resultSet13, answer13)
        mydb.commit() 
        game = False
                    
            
# do not pet fairy
def babyDragonDamage():
    print("")
    print(" After not petting the fairy you continuing your journey")
    print("")
    print(" The next create that comes to you in a baby dragon. Do you pet it or do not pet")
    print("")
    babyDragonDamage1 = input("Type Pet it or do not pet: ").lower()
    resultSet4 = "UPDATE Players SET babyDragon = %s WHERE playerName = %s" 
    answer4 = (babyDragonDamage1, playerName)
    my_cursor.execute(resultSet4, answer4)
    mydb.commit()
        
    if babyDragonDamage1 == "pet it":
        print("")
        print(" You are brave but silly")
        set_player_health()
        goldUnicornDamage()
        #print(" Your health is still at 2.... good luck")
    elif babyDragonDamage1 == "do not pet":
        goldUnicorn() 
            
#pets fairy        
def babyDragon():
    print("")
    print(" Good job, you petted a fairy")
    print("")
    print(" You didn't lose any health points. ")
    print("")
    print(" The next create that comes to you in a baby dragon. Do you pet it or do not pet")
    print("")
    babyDragon1 = input("Type Pet it or do not pet: ").lower()
    resultSet3 = "UPDATE Players SET babyDragon = %s WHERE playerName = %s" 
    answer3 = (babyDragon1, playerName)
    my_cursor.execute(resultSet3, answer3)
    mydb.commit()
    
    if babyDragon1 == "pet it":
        print("")
        print(" You are brave but that was a silly choice")
        set_player_health()
        goldUnicornDamage()
        
    elif babyDragon1 == "do not pet":
        #print(" Wise decision not to touch a dragon's baby.")
        goldUnicorn()    
            
            
        
def start():
     
    
        
    # Create Cursor Instance
    my_cursor = mydb.cursor()

    resultSet1 = "INSERT INTO Players (playerName, playerAge, playerHealth) VALUES (%s, %s, %s)"
    answer = (playerName, playerAge, 3)
    my_cursor.execute(resultSet1,answer)
    mydb.commit()

    # Welcome screen to the game
    print(" ")
    print("    ********************************************************")
    print("                                                          ")
    print("                   Welcome To The Game                         ")
    print("                     Pet or Do Not Pet                 ")
    print("                           "  +  playerName + "                       ")
    print("                                                          ")
    print("    ********************************************************")
    print("")

    print(" You have started the game with a health level of 3.")
    print(" ")
    print(" The goal is to get to the end of the game with as many health points as possible.")
    print(" ")
    print(" If your health reaches 0, your game is over.")
    print(" ")
    print(" ")
    print(" As the game starts you find yourself in a dark forest. As you roam this forest you start to notice weird creatures.")
    print("")
    print(" The creatures start to come up to you and seem like they want to be petted.")
    print("")
    print(" Do you pet these creatures or do you shy them away. The choice is yours.")
    print("")
    print(" The first creature is a fairy do you pet it or do not pet")
    print("")
    #fairy1 = input(" Type (yes) Pet it or (no) Not to Pet: ").lower()
    #resultSet2 = "INSERT INTO Players (fairy) VALUES (%s)"
    #answer = (fairy1)  
    #my_cursor.execute(resultSet2, (fairy1, ))
    #mydb.commit()
        
        
                
    fairy1 = input("Type Pet it or do not pet: ").lower()
    resultSet2 = "UPDATE Players SET fairy = %s WHERE playerName = %s"
    answer2 = (fairy1, playerName)
    my_cursor.execute(resultSet2, answer2)
    mydb.commit()
    if fairy1 == "pet it":
        babyDragon()
        
    elif fairy1 == "do not pet":
        print("")
        print(" you should have petted the fairy, it's just a fairy. Don't be chicken. You have lost 1 health")
        set_player_health()
        babyDragonDamage()
        
        
start()

