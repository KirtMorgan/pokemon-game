import random
from connection_wrapper import *
from pokemon import Pokemon
import time
# __name__
poke = Pokemon()


class Player:
    def __init__(self, name='', city=''):
        self.name = name
        self.city = city
        self.pokemon_caught = []

    def __try_catch_pokemon(self):
        poke.get_name()
        print(f'A wild {poke.name} appeared!')
        time.sleep(3)
        print('Throwing Pokeball!')
        time.sleep(2)
        catch = random.randint(0, 100)
        if catch >= 50:
            print(f'Well done, you caught {poke.name}')
            new_pokemon = poke.name
            self.pokemon_caught.append(new_pokemon)
            poke.save_pokemon(f'{poke.name}')

        elif catch <= 50:
            print(f'The {poke.name} got away, better luck next time')

    def search_for_pokemon(self):
        print('Searching for a pokemon!')
        time.sleep(2)
        self.__try_catch_pokemon()

    def save_player(self):
            try:
                sql_query_no_transaction(f"INSERT INTO player(name, city) VALUES('{self.name}', '{self.city}');")
                docker_pokemon.commit()
                print('Thank you, i have updated the Safari records!')

            except Exception as errmsg:
                print('There has been a error the record has not been committed, please see below exception message')
                print(errmsg)

    def save_pokemon_list_to_player(self, pokemon_name=''):
        try:
            format = ', '
            pokemon_list = format.join(self.pokemon_caught)
            sql_query_no_transaction(f"UPDATE player SET pokemon_caught = '{pokemon_list}' WHERE name = '{self.name}';")
            docker_pokemon.commit()

        except Exception as errmsg:
            print('There has been a error the record has not been committed, please see below exception message')
            print(errmsg)

    def load_player_and_pokemon(self):
        try:
            player_data = sql_query_no_transaction(f"SELECT pokemon_caught FROM player WHERE name = '{self.name}'")
            for data in player_data :
                print(f"\nPokemon Caught: {data.pokemon_caught}")

        except Exception as errmsg:
            print('There has been a error the record(s) have not been read, please see below exception message')
            print(errmsg)
