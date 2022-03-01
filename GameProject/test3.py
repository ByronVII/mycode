player= {"stats":{"name":"Bryan", "life":25, "attack": 4},"equipment":{"weapon":"sword"},"inventory":{}}
print(f"You have {player['equipment']['weapon'][k]} equipped.")
player['equipment']['weapon']= input("What weapon would you like to use?")
print(f"You have {player['equipment']['weapon']} equipped.")
