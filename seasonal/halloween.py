# Halloween drawing prompt generator

from random import shuffle, randint

from nouns.animals import get_animals

noun = [
    # A - E
    'black cat', 'black dog', 'black-eyed children', 'bloody butcher', 'boogeyman', 'brain in a jar', 'clown',
    'costume', 'creature', 'demon', 'devil', 'doll', 'doppelganger',
    # F - J
    'faceless man', 'familiar', 'ghost', 'ghoul', 'goatman', 'goblin', 'hellhound', 'homunculus', 'horseman',
    # K - O
    'kaiju', 'lake monster', 'mad scientist', 'mermaid', 'mummy', 'mothman', 'ninja', 'owl',
    # P - T
    'puppet', 'raven', 'reflection', 'shadow', 'skeleton', 'skull', 'slenderman', 'something', 'stranger',
    # U - Z
    'vampire', 'warlock', 'were-beast', 'werewolf', 'witch', 'zombie'

]

adjectives = [
    # A - E
    'alien', 'angry', 'bizarre', 'bloody', 'body-snatching', 'burning', 'clockwork', 'cobwebbed', 'creeping', 'creepy',
    'cursed', 'eerie', 'envious', 'evil',
    # F - J
    'faceless', 'fanged', 'frost-bitten', 'gaunt', 'gloomy', 'glowing', 'grim', 'grotesque', 'haunted', 'headless',
    'hungry', 'infected',
    # K - O
    'looming', 'luminescent', 'lurking', 'macabre', 'malevolent', 'many-faced', 'many-limbed', 'mouldy', 'mournful',
    'ominous', 'patchwork', 'poisonous', 'otherworldly',
    # P - T
    'parasitic', 'radioactive', 'rotten', 'scaly', 'screaming', 'sinister', 'skeletal', 'slimy', 'spectral', 'spidery',
    'spiky', 'tentacled', 'twisted',
    # U - Z
    'uncanny', 'vengeful', 'watchful'
]

description = [
    'made of bones',
    'from a nightmare',
    'in disguise',
    'with the head of a {}'.format(get_animals(all=True))
]

nope_combo = {
    'bloody butcher': 'bloody',
    'ghost': 'spectral',
    'skeleton': ('skeletal', 'made of bones'),
    'skull': ('skeletal', 'made of bones'),
    'owl': 'with the head of an owl',
    'black cat': 'with the head of a cat',
    'black dog': 'with the head of a dog',
    'hellhound': 'with the head of a dog',
    'slenderman': ('many-limbed', 'faceless'),
    'faceless man': 'faceless'
}


def get_prompt():
    """
    Hallowe'en-themed character generator.

    :return: string
         Description + character.
    """
    shuffle(noun)
    shuffle(adjectives)
    shuffle(description)

    subject = noun[0]

    options = len(adjectives) + len(description)
    die = randint(1, options)

    if (die - 1) <= len(adjectives):
        prompt = '{} {}'.format(adjectives[0], subject)
        if subject in nope_combo.keys() and adjectives[0] in nope_combo[subject]:
            prompt = get_prompt()
    else:
        prompt = '{} {}'.format(subject, description[0])
        if subject in nope_combo.keys() and description[0] in nope_combo[subject]:
            prompt = get_prompt()

    return prompt


if __name__ == '__main__':
    print get_prompt()
