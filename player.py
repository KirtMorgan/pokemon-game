import random
from connection_wrapper import *


class Player:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.pokemon_caught = []

    def search_for_pokemon(self):
        print('Searching for a pokemon!')
        search = random.randint(0,100)
        print(search)
        if search >= 50:
            print('You found a pokemon!')
        elif search <= 50:
            print('You didnt find anything this time')

    def __try_catch_pokemon(self):
        ''

    def save_player_and_pokemon(self, name, city, pokemon_caught):
            try:
                sql_query_no_transaction(
                    f"INSERT INTO pokemon(name, city, pokemon_caught) VALUES('{name}', '{city}', '{pokemon_caught}');")
                docker_pokemon.commit()
                print('The table has been updated, 1 row affected')

            except Exception as errmsg:
                print('There has been a error the record has not been committed, please see below exception message')
                print(errmsg)

    def load_player_and_pokemon(self):
        try:
            player_data = sql_query_no_transaction("SELECT * FROM player")
            for data in player_data :
                print(f"Player name: {data.name}\nPlayer City: {data.city}\nPokemon Caught: {data.pokemon_caught}")
                Player(data.name, data.city)

        except Exception as errmsg:
            print('There has been a error the record(s) have not been read, please see below exception message')
            print(errmsg)
