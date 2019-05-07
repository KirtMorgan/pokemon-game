from player import Player
from pokemon import Pokemon
import time
player = Player()
pokemon = Pokemon()

def set_player_name_save():
    input_1 = input('What is your name?')
    input_2 = input(f'What city are you from {input_1}?')
    player.name = input_1
    player.city = input_2
    player.save_player()

print('Welcome to the Pokemon Wild Safari!')
print('Before we get started lets find out who you are adventurer!')
set_player_name_save()
print('Now we have that sorted you can enter the park')
time.sleep(2)

while True:
    print('What would you like to do?\n1) Search for pokemon\n2) List the pokemon you have caught')
    user_input = int(input('Your selection >>>'))
    if user_input == 1:
        player.search_for_pokemon()

    elif user_input == 2:
        player.load_player_and_pokemon()

    else:
        #save player and pokemons
        break