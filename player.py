import random


class Player:
    def __init__(self):
        self.name = ''
        self.city = ''
        self.pokemon_caught_list = []

    def search_for_pokemon(self):
        while True:
            user_input = input('Search for a pokemon? y/n')
            if user_input == 'y':
                print('Searching for a pokemon!')
                search = random.randint(0,100)
                print(search)
                if search >= 50:
                    print('You found a pokemon!')
                elif search <= 50:
                    print('You didnt find anything this time')

    def __try_catch_pokemon(self):
        ''

    def save_player_and_pokemon(self):
        ''

    def load_player_and_pokemon(self):
        ''
