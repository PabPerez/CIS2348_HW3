#Pablo Perez
#PSID: 1770045
def output_roster():
    keys = list(player_info.keys())
    keys.sort()
    for key in keys:
        print("Jersey number: %d, Rating: %d" %(key, player_info[key]))

def add_player():
    print("Enter new player's jersey number:")
    player = int(input())
    print("Enter the player's rating:")
    rating = int(input())
    player_info[player] = rating


player_info = {}
for i in range(5):
    player = int(input("Enter player %d's jersey number:\n" %(i+1)))
    player_info[player] = int(input("Enter player %d's rating:\n" %(i + 1)))
    print()
keys = list(player_info.keys())
keys.sort()

print("ROSTER")
for key in keys:
    print("Jersey number: %d, Rating: %d" %(key, player_info[key]))
print()

while True:
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()

    #output_roster()
    print("Choose an option:")
    user_option = input()
    if user_option == 'q':
        break
    if user_option == 'o':
        output_roster()

    if user_option == 'a':
        add_player()

    #if user_option == 'r':