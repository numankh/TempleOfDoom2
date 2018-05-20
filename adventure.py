# -*- coding: utf-8 -*-
"""
Text Adventure Game
author: Numan Khan
"""
__version__ = 8

# 2) print_introduction: Print a friendly welcome message for your game
# This function simply prints out a description of the game to the user

def print_introduction():
    print("Welcome to the Temple of Doom and you will be playing as Indiana Jones. ")
    print("After consulting an archaeologist, you have found out that the golden idol")
    print("that you had found in the Temple of Doom was fake. Now you are searching")
    print("a new temple for the real golden idol.")
    print("NOTE: PLEASE TYPE COMMANDS AS YOU SEE THEM")
    print("")
    print("Your mission, if you choose to accept it, is find the real golden idol.")    
    
# 3) get_initial_state: Create the starting player state dictionary
# This function returns the current player state dictionary
    
def get_initial_state():
    
    #outside of the 2 basic player states
    #there are 4 more player items/actions
    playerDict = {"game status" : "playing", 
                  "location" : "Entrance" ,
                  "has snake bite" : False, 
                  "has whip" : False,
                  "has amulet" : False,
                  "has antidote" : False}
    return playerDict
    
# 4) print_current_state: Print some text describing the current game world
# Specifically, this function prints out specific items or actions that the 
# user has encountered in the game.
# This function consumes the player state dictionary and prints the player's
# status in the game.

def print_current_state(playerDict):
    print("Your current location is the: " + playerDict["location"])
    
    #This line prints a header of asteriks for the player state
    if playerDict["has snake bite"] or playerDict["has whip"] == True or playerDict["has amulet"]:
        print("")
        print("******************************************")
        print("Your physical conditions or items you own:")
    
    if playerDict["has snake bite"]:
        print("--->You have been bitten by a snake, you better find an antidote soon!")

    if playerDict["has whip"]:
        print("--->You have obtained a whip, might come in handy in the future.")
        
    if playerDict["has amulet"]:
        print("--->You have found an ancient amulet that has inscriptions similar to the golden idol.")

    if playerDict["has antidote"]:
        print("--->You have obtained an antidote that cures snake bites.")        
    
    #This line prints a footer of asteriks for the player state
    if playerDict["has snake bite"] or playerDict["has whip"] == True or playerDict["has amulet"]:
        print("******************************************")

# 5) get_options: Return a list of commands available to the player right now
# This function provides options that the user can currently take
# In addition, this function consumes the player state dictionary and returns
# a list of possible choices that the user can take.
        
def get_options(playerDict):
    commandList = []
    
    #This chain of IF statements are the possible rooms the user can go to
    #for every room in the temple
    if playerDict["location"] == "Entrance":
        commandList.append("Great Gallery")
        commandList.append("Underground Chamber")
        
    elif playerDict["location"] == "Great Gallery":
        commandList.append("Entrance")
        commandList.append("King's Chamber")
        commandList.append("Queen's Chamber")
        
    elif playerDict["location"] == "King's Chamber":
        commandList.append("Great Gallery")
        
    elif playerDict["location"] == "Queen's Chamber":
        commandList.append("Great Gallery")

    elif playerDict["location"] == "Underground Chamber":
        commandList.append("Entrance")
        commandList.append("Burial Chamber")
        commandList.append("Broken Bridge")
        
    elif playerDict["location"] == "Burial Chamber":
        commandList.append("Underground Chamber")
        
    elif playerDict["location"] == "Broken Bridge":
        commandList.append("Treasure Room")
        
        
    #This returns the list of commands so that they can be printed
    #using the print_options function
    return commandList

# 6) print_options: Print out the list of commands available    
# This function displays the options the user can currently do
# Also, this function consumes the command list and prints the list
    
def print_options(commandList):
    print("The rooms you can explore: ")
    for x in commandList:
        #This prints each command with some formatting (better for UI)
        print("---> "+x)
        
# 7) get_user_input: Repeatedly prompt the user to choose a valid command
# This functioon prompts the user to state which room he or she wants to go to
# and continues to prompt the user if the entered string is not a possible 
# choice or the user quits the game.
# Also, this function consumes a command list and prompts the user 
        
def get_user_input(commandList):
    check = True
    #User will continue to prompted until the command is valid or is "quit"
    while check:
        #The user will be prompted the question below
        destination = input("Which room do you want to explore or you may quit: ")
        #The user may quit if they want to 
        if destination == "quit":
            check = False
            
        #Checks if the command (location the user wants to go to) is valid
        for x in commandList:
            if destination == x:
                check = False
    print("===========================================================================")

    return destination
# 8) process_command: Change the player state dictionary based on the command
# This function takes the user input from the previous function and updates
# the player state table.
# Also, this function consumes a command String and a player state dictionary

def process_command(command, playerDict):
    
    #this chain of IF statements are how the player state dictionary will
    #be altered for every possible valid command
    if command == "quit":
        playerDict["game status"] = "quit"
    
    elif command == "Entrance":
        playerDict["location"] = "Entrance"
        
    elif command == "Great Gallery":
        playerDict["location"] = "Great Gallery"
        
        #At the king's chamber, user will be bit by snakes
    elif command == "King's Chamber":
        playerDict["location"] = "King's Chamber"
        playerDict["has snake bite"] = True
        
        #At the queen's chamber, user will obtain an amulet
    elif command == "Queen's Chamber":
        playerDict["location"] = "Queen's Chamber"
        
        playerDict["has amulet"] = True


    elif command == "Underground Chamber":
        playerDict["location"] = "Underground Chamber"
        
        #At the burial chamber, user will cure themselve of the snake
        #bite and obtains a whip to cross the broken bridge
    elif command == "Burial Chamber":
        playerDict["location"] = "Burial Chamber"
        
        playerDict["has antidote"] = True            
        playerDict["has snake bite"] = False
        playerDict["has whip"] = True

        
        #if the user has a snake bite, they will die
        #else they will continue to go to the Broken Bridge
    elif command == "Broken Bridge":
        if playerDict["has snake bite"] == True:
            playerDict["game status"] = "lose"
        else:
            playerDict["location"] = "Broken Bridge"
            print("CURRENT EVENT: ")
            print("Because you don't have a snake bite, you were aware")
            print("enough to evade a switch that would've activated a trap")
            
        
        #if the user doesn't have a whip, they will fail to travel
        #across the broken bridge and die
        #else the user will reach the treasure room
        #if they dont have the amulet, the golden idol will be destroyed
        #else they will win
    elif command == "Treasure Room":
        if playerDict["has whip"] == False:
            playerDict["game status"] = "lose"
        else:
            playerDict["location"] = "Treasure Room"
            print("CURRENT EVENT: ")
            print("A trap had activated which cut the bridge while you were ")
            print("crossing it. But you had a whip that helped you survive")

            if playerDict["has amulet"] == True:
                playerDict["game status"] = "win"
            else:
                playerDict["game status"] = "lose"
            

# 9) print_game_ending: Print a victory, lose, or quit message at the end  
# This function prints a description for when the user is still playing, has
# won, has lost, or has quit the game.
# Also, this function consumes a player state dictionary and prints a 
# a description based on the user's current game status
def print_game_ending(playerDict):
    
    if playerDict["game status"] == "playing":
        print("You are still alive, continue exploring the temple!")
        
    if playerDict["game status"] == "win":
        print("")
        print('''
              You have arrived at the Treasure Room but the real golden idol
              is locked in a cage that will crush itself if you don't open it
              as soon as possible. The only way to open is to manipulating the
              glyphs on a totem. 
              
              It seems like the glyphs on totem are similar to the 
              inscription on the amulet you have. Using the amulet, you move 
              different layers of the totem and obtain the real golden idol. 
              
              You have won!''')

    elif playerDict["game status"] == "lose":
        if playerDict["has snake bite"] == True:
            print("")
            print('''
                  While trying to travel to the Broken Bridge, you started
                  feeling weak from the snake bite and stepped on a switch. The
                  switch activates a spear trap from the sides of the walls 
                  which kills you.
                  
                  You have been impaled to death.
              
                  GAME OVER''')
            
        if playerDict["has snake bite"] == False and playerDict["has whip"] == False:
            print("")
            print('''
                  While trying to get pass the Broken Bridge, a trap
                  activates and the bridge collapses. You have no item that 
                  allows you to survive this encounter.
                  
                  You have fallen to your death.
              
                  GAME OVER''')
            
        if playerDict["has snake bite"] == False and playerDict["has whip"] == True and playerDict["has amulet"] == False:
            print("")
            print('''
                  You have arrived at the Treasure Room but the real golden 
                  idol is locked in a cage that will destroy the golden idol 
                  if you don't open it as soon as possible. The only way to 
                  open is by manipulating the glyphs on a totem next to it. 
              
                  You tried different combinations of glyphs on the totem but
                  end up running out of time. In the end, the cage
                  destroys the real golden idol. 
                  
                  You have failed your mission.
              
                  GAME OVER''')

    elif playerDict["game status"] == "quit":
        print("")
        print('''
              You have tried your best and are willing to give up and find the
              golden idol another day.
              
              You have quit your mission. 
              
              GAME OVER''')
     
# Command Paths to give to the unit tester

# These are the game specific paths to either lose or win
# In this game, losing means dying or not getting the real golden idol
# and winning means obtaining the real golden idol
        
WIN_PATH = ["Great Gallery","Queen's Chamber","Great Gallery","Entrance",
            "Underground Chamber","Burial Chamber","Underground Chamber", 
            "Broken Bridge", "Treasure Room"]

LOSE_PATH = ["Underground Chamber", "Broken Bridge","Treasure Room"]

# 1) Main function that runs your game, read it over and understand
# how the player state flows between functions.
def main():
    # Print an introduction to the game
    print_introduction()
    # Make initial state
    the_player = get_initial_state()
    # Check victory or defeat
    while the_player['game status'] == 'playing':
        # Give current state
        print_current_state(the_player)
        # Get options
        available_options = get_options(the_player)
        # Give next options
        print_options(available_options)
        # Get Valid User Input
        chosen_command = get_user_input(available_options)
        # Process Commands and change state
        process_command(chosen_command, the_player)
    # Give user message
    print_game_ending(the_player)

# Executes the main function
if __name__ == "__main__":
    main()
