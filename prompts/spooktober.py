# Halloween drawing prompt generator

from random import randint


from prompts.characterGenerator import CharacterGenerator

from nouns.animals import get_animal


class Spooktober(CharacterGenerator):
    def __init__(self):
        self.char_type = [
            # A - E
            'black cat', 'black dog', 'black-eyed children', 'bloody butcher', 'boogeyman', 'brain in a jar', 'clown',
            'costume', 'creature', 'demon', 'devil', 'doll', 'doppelganger',
            # F - J
            'faceless man', 'familiar', 'ghost', 'ghoul', 'goatman', 'goblin', 'hellhound', 'homunculus', 'horseman',
            # K - O
            'kaiju', 'lake monster', 'mad scientist', 'mummy', 'mothman', 'owl',
            # P - T
            'puppet', 'raven', 'reflection', 'shadow', 'skeleton', 'skull', 'slenderman', 'something', 'stranger',
            # U - Z
            'vampire', 'warlock', 'were-beast', 'werewolf', 'witch', 'zombie'

        ]

        self.adjectives = [
            # A - E
            'alien', 'angry', 'bizarre', 'bloody', 'body-snatching', 'burning', 'clockwork', 'cobwebbed', 'creeping',
            'creepy', 'cursed', 'eerie', 'envious', 'evil',
            # F - J
            'faceless', 'fanged', 'frost-bitten', 'gaunt', 'gloomy', 'glowing', 'grim', 'grotesque', 'haunted',
            'headless', 'hungry', 'infected',
            # K - O
            'looming', 'lurking', 'macabre', 'malevolent', 'many-faced', 'many-limbed', 'mouldy', 'mournful', 'ominous',
            'patchwork', 'poisonous', 'otherworldly',
            # P - T
            'parasitic', 'radioactive', 'rotten', 'scaly', 'screaming', 'sinister', 'skeletal', 'slimy', 'spectral',
            'spidery', 'spiky', 'tentacled', 'twisted',
            # U - Z
            'uncanny', 'vengeful', 'watchful'
        ]

        self.description = [
            'made of bones',
            'from a nightmare',
            'in disguise',
            'with the head of a {}'.format(get_animal('all'))
        ]

        self.nope_combo = {
            'bloody butcher': 'bloody',
            'ghost': 'spectral',
            'skeleton': ('skeletal', 'made of bones'),
            'skull': ('skeletal', 'made of bones'),
            'owl': 'with the head of an owl',
            'black cat': 'with the head of a cat',
            'black dog': 'with the head of a dog',
            'hellhound': 'with the head of a dog',
            'slenderman': ('many-limbed', 'faceless'),
            'faceless man': 'faceless',
            'costume': 'frost-bitten'
        }


if __name__ == '__main__':
    c = Spooktober()
    print c.get_prompt()
