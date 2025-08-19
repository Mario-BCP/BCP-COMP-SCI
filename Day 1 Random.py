import random
# lets us use like the random function options
def choose_player(players): 
    #Define a function that takes a list of players
    if not players:
         #check if the list is empty
        return None    
    # if its empty, return None (no player to choose)
    return random.choice(players) 
# pick and return one random player from the list

# Example usage: 
players = [ "lebron", "curry", "Jordan", "Kobe", "KD", "Poole", "Tatum", "SGA"] 
 #creates like the list
chosen = choose_player(players)  
#CHooses one player
print("chosen player:", chosen) 
#shows the chosen player
