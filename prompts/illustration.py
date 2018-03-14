
import libraries

from libraries.nouns.animals import get_animal
from libraries.nouns.places import get_place


illustration = [
    'ninja battle',
    '"whatever you do, keep your eyes on me"',
    'haunted {}'.format(get_place()),
    'abandoned {}'.format(get_place()),
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
    Get a random prompt from the illustration list.
    :return: string
        An illustration prompt.
    """
    return libraries.get_one(illustration)