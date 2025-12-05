computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games = sorted(computer_games)

i = 0

while i < 10:
    print(str(i+1), end =' ')
    print(computer_games[i])
    i += 1

