from pokemonNames.pokemonNames import PokemonNames

class Pokemon():
    def __init__(self, name=''):
        self.name = name

    def get_name(self):
        generator = PokemonNames()
        pokemon = generator.get_random_name()
        self.name = pokemon

    def tackle(self):
        print('The pokemon runs towards you')

    def make_noise(self):
        print('The pokemon makes a signature sound')

    def rest_to_refill_health(self):
        print('The pokemon rests to regain its energy')

    def save_pokemon(self):
        ''

    def load_pokemon(self):
        ''
