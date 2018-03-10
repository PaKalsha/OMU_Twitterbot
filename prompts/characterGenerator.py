from random import randint

from nouns.animals import get_animal

char_type = (
    # A - E
    'barbarian', 'captain', 'centaur', 'class clown', 'cleric',
    # F - J
    'fairy princess', 'guard',
    # K - O
    'mayor',
    # P - T
    'pair of stowaways', 'plumber-turned-hero', 'priest', '{} shepard'.format(get_animal('mythical')),
    'soldier', 'star-crossed lovers', 'survivalist', 'wizard', 'trader', 'trickster', 'tsundere',
    # U - Z
    'warrior'
)


adjectives = (
    # Emotions
    'lovestruck', 'giddy', 'sleepy', 'angry', 'playful', 'curious', 'silly', 'laughing', 'joyful', 'happy', 'hopeful',
    'confident', 'powerful', 'peaceful', 'surprised', 'eager', 'excited', 'glorious', 'fascinated', 'compassionate',
    'cheerful', 'glamorous', 'determined', 'enthusiastic', 'satisfied', 'courageous', 'relaxed',
    'tired', 'concerned', 'apprehensive', 'flustered', 'rude', 'confused', 'exasperated', 'sad', 'lonely', 'suspicious',
    'grief-stricken', 'morose', 'serious', 'glum', 'aggressive', 'wary', 'nervous', 'upset', 'envious', 'hungry',
    'protective', 'confused', 'smug', 'penitent',

    # Descriptors
    'masked', 'magical', 'cute', 'ancient', 'regal', 'mystical', '{}-like'.format(get_animal('mammal'))
)


def generate_character():
    index_limit = len(char_type) - 1
    return char_type[randint(0, index_limit)]


def get_prompt(character=None):
    if character is None:
        character = generate_character()

    index_limit = len(adjectives) - 1
    desc = adjectives[randint(0, index_limit)]

    return '{} {}'.format(desc, character)


if __name__ == '__main__':
    print get_prompt()
