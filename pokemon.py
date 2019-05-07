from pokemonNames.pokemonNames import PokemonNames
from connection_wrapper import *
# __name__


class Pokemon:
    def __init__(self, name=''):
        self.name = name

    def get_name(self):
        generator = PokemonNames()
        self.name = generator.get_random_name()

    def tackle(self):
        print('The pokemon runs towards you')

    def make_noise(self):
        print('The pokemon makes a signature sound')

    def rest_to_refill_health(self):
        print('The pokemon rests to regain its energy')

    def save_pokemon(self, name):
        try:
            sql_query_no_transaction(
                f"INSERT INTO pokemon(name) VALUES('{name}');")
            docker_pokemon.commit()
            print('The Pokemon has been added to the Pokedex')

        except Exception as errmsg:
            print('There has been a error the record has not been committed, please see below exception message')
            print(errmsg)
