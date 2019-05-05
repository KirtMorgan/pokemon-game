from pokemonNames.pokemonNames import PokemonNames

class Pokemon:
    def __init__(self):
        self.name = ''

    def get_name(self):
        generator = PokemonNames()
        pokemon = generator.get_random_name()
        self.name = pokemon
        print(self.name)

    def tackle(self):
        ''

    def make_noise(self):
        ''

    def rest_to_refill_health(self):
        ''

    def save_pokemon(self):
        ''

    def load_pokemon(self):
        ''
