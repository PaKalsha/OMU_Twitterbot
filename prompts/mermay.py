from random import randint

from nouns.animals import get_animal

adjectives = (
    # Emotions
    'lovestruck', 'giddy', 'sleepy', 'angry', 'playful', 'curious', 'silly', 'laughing', 'joyful', 'happy', 'hopeful',
    'confident', 'powerful', 'peaceful', 'surprised', 'eager', 'excited', 'glorious', 'fascinated', 'compassionate',
    'cheerful', 'glamorous', 'determined', 'enthusiastic', 'satisfied', 'courageous', 'relaxed',
    'tired', 'concerned', 'apprehensive', 'flustered', 'rude', 'confused', 'exasperated', 'sad', 'lonely', 'suspicious',
    'grief-stricken', 'morose', 'serious', 'glum', 'aggressive', 'wary', 'nervous', 'upset', 'envious', 'hungry',
    'protective', 'confused', 'smug', 'penitent',

    # Descriptors
    'masked', 'magical', 'cute', 'ancient', 'regal', 'mystical'
)


def get_prompt():
    """
    Mermaid-themed character generator.
    :return: string
        mermaid character prompt
    """

    index_limit = len(adjectives) - 1
    desc = adjectives[randint(0, index_limit)]

    return '{} {} mermaid'.format(desc, get_animal('fish'))


if __name__ == '__main__':
    print get_prompt()
