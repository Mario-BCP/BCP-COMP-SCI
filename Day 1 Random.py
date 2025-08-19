import random

def choose_player(players):
    if not players: 
        return now    # in case the array is empty
    return random.choice(players)

# Example usage: 
players = [ "lebron", "curry", "Jordan", "Kobe", "KD", "Poole", "Tatum", "SGA"]
chosen = choose_player(players)
print("chosen player:", chosen)
