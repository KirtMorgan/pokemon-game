import random
from connection_wrapper import *
from pokemon import Pokemon
# __name__

class Player:
    def __init__(self, name='', city=''):
        self.name = name
        self.city = city
        self.pokemon_caught = []

    def __try_catch_pokemon(self):
        print('Thowing Pokeball!')
        catch = random.randint(0, 100)
        if catch >= 50:
            poke = Pokemon(self.name)
            poke.get_name()
            new_pokemon = print('You caught a..', poke.name)
            self.pokemon_caught.append(new_pokemon)
            self.save_player_and_pokemon('' , '' , f'{poke.name}')
            poke.save_pokemon(f'{poke.name}')

        elif catch <= 50:
            print('The pokemon got away, better luck next time')

    def search_for_pokemon(self):
        print('Searching for a pokemon!')
        self.__try_catch_pokemon()

    def save_player_and_pokemon(self, name='', city='', pokemon_caught=''):
            try:
                sql_query_no_transaction(
                    f"INSERT INTO player(name, city, pokemon_caught) VALUES('{name}', '{city}', '{pokemon_caught}');")
                docker_pokemon.commit()
                print('Thank you, i have updated the Safari records!')

            except Exception as errmsg:
                print('There has been a error the record has not been committed, please see below exception message')
                print(errmsg)

    def load_player_and_pokemon(self):
        try:
            player_data = sql_query_no_transaction("SELECT pokemon_caught FROM player")
            for data in player_data :
                print(f"\nPokemon Caught: {data.pokemon_caught}")

        except Exception as errmsg:
            print('There has been a error the record(s) have not been read, please see below exception message')
            print(errmsg)
