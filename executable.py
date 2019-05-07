from player import Player
from pokemon import Pokemon
player = Player()
pokemon = Pokemon()

def new_player():
    input_1 = input('What is your name?')
    input_2 = input(f'What city are you from {input_1}?')
    player.save_player_and_pokemon(f'{input_1}', f'{input_2}', '')
    Player(player.name, player.city)

print('Welcome to the Pokemon Wild Safari!')
print('Before we get started lets find out who you are adventurer!')
new_player()
print('Now we have that sorted you can enter the park')

while True:
    print('What would you like to do?\n1) Search for pokemon\n2) List the pokemon you have caught')
    user_input = int(input('Your selection >>>'))
    if user_input == 1:
        player.search_for_pokemon()

    elif user_input == 2:
        player.load_player_and_pokemon()

    else:
        break