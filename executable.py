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
    print('What would you like to do?\n1) Search for pokemon\n2) List the pokemon you have caught\n3) Exit Game')
    user_input = int(input('Your selection >>>'))
    if user_input == 1:
        player.search_for_pokemon()
        time.sleep(4)

    elif user_input == 2:
        player.save_pokemon_list_to_player()
        player.load_player_and_pokemon()

    elif user_input == 3:
        print('You leave the Wild Safari and return home.')
        print('Thanks for playing!')
        break