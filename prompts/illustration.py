
from random import randint

from nouns.animals import get_animal

illustration = [
    'ninja battle',
    '"whatever you do, keep your eyes on me"',
    'haunted painting studio',
    'abandoned opera house',
    'kaiju attack',
    'campfire tales',
    'saving a sleepwalker from themself',
    'an astonishing slice of cake',
    'a fairytale gatecrashing a birthday party',
    'zombie apocalypse ... on ice!',
    'something wicked this way comes',
    'improve a story you like',
    'fix a story that you don\'t like',
    'your character receives a basket of baby {}s'.format(get_animal('mythical'))
]


def get_prompt():
    """

    :return:
    """
    prompt = illustration[randint(0, (len(illustration) - 1))]
    return prompt