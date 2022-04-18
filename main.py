import mysql.connector
import logging



name = ""
fairy = ""
babyDragon = ""
babyDragonDamage = ""
goldUnicorn = ""
goldUnicornDamage = ""
takeDamage = ""
playerName = ""
playerAge = ""
endGameHealth = 0
playerHealth = 3
valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
game = True

#log = need to add logging feature

    #Game loop
    
    #while (game){
try:
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "##########################",
    database = "python_game_with_mysql",
    )
    #print(mydb)
    
    
    #Create A Database
    #my_cursor.execute("CREATE DATABASE python_game_with_mysql") 

    # Show Database
    #my_cursor.execute("SHOW DATABASES")
    #for db in my_cursor:
    #    print(db)

    #Create Table
    #my_cursor.execute("CREATE TABLE Players ( user_id INT AUTO_INCREMENT PRIMARY KEY, playerName VARCHAR(255) NOT NULL, playerAge INT NOT NULL, playerHealth INT, fairy VARCHAR(255), babyDragon VARCHAR(255), goldUnicorn VARCHAR(255), endGameHealth INT)")
    
    
    playerName = input("What is your name: ").upper()
    playerAge = int(input("What is your age: ")) 
        
    # Create Cursor Instance
    my_cursor = mydb.cursor()

    resultSet1 = "INSERT INTO Players (playerName, playerAge, playerHealth) VALUES (%s, %s, %s)"
    answer = (playerName, playerAge, 3)
    my_cursor.execute(resultSet1,answer)
    mydb.commit()
    
    


    # Welcome screen to the game
    def main():
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
        fairy1 = input("Type yes Pet it or no Not to Pet: ").lower()
        resultSet2 = "UPDATE Players SET fairy = %s WHERE playerName = %s"
        answer2 = (fairy1, playerName)
        my_cursor.execute(resultSet2, answer2)
        mydb.commit()
        
            
                
        if fairy1 == "yes":
            babyDragon()
            
        elif fairy1 == "no":
            print("")
            print(" you should have petted the fairy, it's just a fairy. Don't be chicken. You have lost 1 health")
            takeDamage()
            babyDragonDamage()
                    
        
            # taking damage method    
            def takeDamage():
                print("")
                print( playerName + " has taken damage!!!")
                playerHealth -= 1
                print("")
                print(playerName + " your health level is " + playerHealth)
                print("")
                        
            #pets fairy
            def babyDragon():
                print("")
                print(" Good job, you petted a fairy")
                print("")
                print(" You didn't lose any health points. ")
                print("")
                print(" The next create that comes to you in a baby dragon. Do you pet it or do not pet")
                print("")
                babyDragon = input(" Type (yes) Pet it or (no) Not to Pet: ").lower()
                resultSet3 = "INSERT INTO Players (babyDragon) VALUES (%s)"
                answer = (babyDragon)

                my_cursor.execute(resultSet3,answer)
                mydb.commit()
                
                if babyDragon == "pet it":
                    print(" You are brave but that was a silly choice")
                    takeDamage()
                    goldUnicornDamage()
                    
                elif babyDragon == "do not pet":
                    #print(" Wise decision not to touch a dragon's baby.")
                    goldUnicorn()

                    
                    
            # do not pet fairy
            def babyDragonDamage():
                print("")
                print(" After not petting the fairy you continuing your journey")
                print("")
                print(" The next create that comes to you in a baby dragon. Do you pet it or do not pet")
                print("")
                babyDragonDamage =  input(" Type (yes) Pet it or (no) Not to Pet: ").lower()
                resultSet3_3 = "INSERT INTO Players (babyDragon) VALUES (%s)"
                answer = (babyDragonDamage)
                my_cursor.execute(resultSet3_3,answer)
                mydb.commit()
                    
                if babyDragonDamage == "yes":
                    print(" You are brave but silly")
                    takeDamage()
                    goldUnicornDamage()
                    #print(" Your health is still at 2.... good luck")
                elif babyDragonDamage == "no":
                    goldUnicorn()                

                            
                        
            # do not pet baby dragon
            def goldUnicorn():
                print("")
                print("Good Choice... Why would anyone pet a baby dragon. The mommy dragon would have eaten you.")
                print("")
                #print(" Your health is now 2. Your health points are getting low. Be careful.")
                print("")
                print("The final creature in your test is a Gold Unicorn. pet it or do not pet")
                goldUnicorn = input(" Type (yes) Pet it or (No) Not to Pet: ").lower()
                resultSet4 = "INSERT INTO Players (goldUnicorn) Values (%s)"
                answer = (goldUnicorn)
                my_cursor.execute(resultSet4,answer)
                mydb.commit()  

                #didnt pet fairy, pet baby dragon, pet gold unicorn
                if (goldUnicorn  == "pet it" and playerHealth > 0): 
                    print("")
                    print(" You never touch the gold Unicorn.")
                    print("")
                    takeDamage()
                    print(" Total playerHealth points left: " + playerHealth )
                    print("")
                    print(" Great Job. You have WON THE GAME")
                    resultSet5 = "UPDATE Players SET endGameplayerHealth = ('"+playerHealth+"') WHERE playerName = ('"+playerName+"')"
                    my_cursor.execute(resultSet5)
                    mydb.commit() 
                    game = False

                    #pet fairy, didn't pet baby dragon, didn't pet gold unicorn    
                elif (goldUnicorn  == "do not pet" and playerHealth == 3): 
                    print("")
                    print("Good choice not to pet the Gold Unicorn. You have ended the game with all your health points ")
                    print("")
                    print("Great Job. You have WON THE GAME")
                    print("")
                    print(" Total health points left: " + playerHealth )
                    resultSet6 = "UPDATE Players SET endGameplayerHealth = ('"+playerHealth+"') WHERE playerName = ('"+playerName+"')"
                    my_cursor.execute(resultSet6)
                    mydb.commit() 
                    game = False
                    #DOESNT END GAME LOOP

                # didn't pet fairy, pet baby dragon, didn't pet gold unicorn    
                elif (goldUnicorn  == "do not pet" and playerHealth == 2):
                    print("")
                    print("Good choice not to pet the Gold Unicorn. You have ended the game with 2 points. ")
                    print("")
                    print("Well done. You have WON THE GAME")
                    print("")
                    print(" Total health points left: " + playerHealth )
                    resultSet7 = "UPDATE Players SET endGameplayerHealth = ('"+playerHealth+"') WHERE playerName = ('"+playerName+"')"
                    my_cursor.execute(resultSet7)
                    mydb.commit() 
                    game = False

                # didn't pet fairy, pet baby dragon, didnt pet gold unicorn    
                elif (goldUnicorn  == "do not pet" and playerHealth == 1):
                    print("")
                    print(" It's always a good idea to never touch the mystical unicorn. You have ended the game with 1 point.")
                    print("")
                    print("You could have done better. But either way,  You have WON THE GAME")
                    print("")
                    print(" Total health points left: " + playerHealth )
                    resultSet8 = "UPDATE Players SET endGameplayerHealth = ('"+playerHealth+"') WHERE playerName = ('"+playerName+"')"
                    my_cursor.execute(resultSet8)
                    mydb.commit() 
                    game = False
                            
                        

            #pet baby dragon
            def goldUnicornDamage():
                print("")
                print("Why would anyone pet a baby dragon. The mommy dragon could have eaten you")
                print("")
                print("The final creature in your test is a Gold Unicorn. pet it or do not pet")
                goldUnicornDamage  = input(" Type (yes) Pet it or (No) Not to Pet: ").lower()
                resultSet9 = "INSERT INTO Players (goldUnicornDamage) Values (%s)"
                answer = (goldUnicornDamage)
                my_cursor.execute(resultSet9,answer)
                mydb.commit() 

                #didnt pet fairy, pet baby dragon, pet gold unicorn
                if (goldUnicornDamage == "pet it"):
                    print("")
                    print(" You never touch the gold Unicorn.")
                    print("")
                    takeDamage()
                    print(" You have lost all your health. You have LOST THE GAME.... BETTER LUCK NEXT TIME.")
                    print("")
                    print(" Total health points left: " + playerHealth )
                    print("")
                    resultSet10 = "UPDATE Players SET endGameplayerHealth = ('"+playerHealth+"') WHERE playerName = ('"+playerName+"')"
                    my_cursor.execute(resultSet10)
                    mydb.commit() 
                    game = False
                    
                            
                # didn't pet fairy, pet baby dragon, didn't pet gold unicorn    
                elif (goldUnicornDamage == "do not pet" and playerHealth == 2):
                    print("")
                    print("Good choice not to pet the Gold Unicorn. You have ended the game with 2 points. ")
                    print("")
                    print("Well done. You have WON THE GAME")
                    print("")
                    print(" Total health points left: " + playerHealth )
                    print("")
                    resultSet11 = "UPDATE Players SET endGameplayerHealth = ('"+playerHealth+"') WHERE playerName = ('"+playerName+"')"
                    my_cursor.execute(resultSet11)
                    mydb.commit() 
                    game = False

                #didn't pet fairy, pet baby dragon, didnt pet gold unicorn    
                elif (goldUnicornDamage == "do not pet" and playerHealth == 1):
                    print("")
                    print(" It's always a good idea to never touch the mystical unicorn. You have ended the game with 1 point.")
                    print("")
                    print("You could have done better. But either way,  You have WON THE GAME")
                    print("")
                    print(" Total health points left: " + playerHealth )
                    print("")
                    resultSet12 = "UPDATE Players SET endGameplayerHealth = ('"+playerHealth+"') WHERE playerName = ('"+playerName+"')"
                    my_cursor.execute(resultSet12)
                    mydb.commit() 
                    game = False        
               

except ValueError:
    print("Invalid value, Try again")
    
if __name__ == "__main__":
    main()