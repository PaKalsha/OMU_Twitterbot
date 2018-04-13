
from random import randint

from prompts.characterGenerator import CharacterGenerator

import libraries

from libraries.concepts.genre import get_genre

from libraries.nouns.animals import get_animal
from libraries.nouns.music import get_instrument


class Mermay(CharacterGenerator):
    """
    Mermaid-themed prompts.

    Mermay started by Tom Bancroft - http://tombancroftstudio.com/
    """

    def __init__(self):
        super(Mermay, self).__init__()
        self.environment = [
            'artificial reef', 'cave', 'cavern', 'coral palace', 'coral reef', 'drowned city', 'flooded city',
            'kelp forest',
            'reef', 'shipwreck', 'sunken pirate ship', 'sunken pirate treasure',
            'underwater castle', 'underwater city', 'whale graveyard',
        ]

        self.scene = [
            'sunbathing {}'.format(self.get_character()),
            'a {} rescuing a shipwrecked sailor'.format(self.get_character()),
            'a {} enticing sailors'.format(self.get_character()),
            'queen of the {} merfolk'.format(get_animal('fish')),
            'king of the {} merfolk'.format(get_animal('fish')),
            'a {} and their pet {}'.format(self.generate_character(), get_animal('fish')),
            'a {} exploring a {}'.format(self.get_character(), self.get_env()),
            'a {} in a {}'.format(self.generate_character(), self.get_env()),
            'a {} playing the {}'.format(self.get_character(), get_instrument()),
            'a {} eating her favourite food'.format(self.get_character()),
            'a {} and her baby'.format(self.get_character()),
            'a family of {} merfolk'.format(get_animal('fish')),
            'a {} surrounded by {}'.format(self.get_character(), get_animal('fish')),
            'a {} rescuing a trapped {}'.format(self.get_character(), get_animal('fish')),
            'a {} fighting a monstrous {}'.format(self.get_character(), get_animal('fish')),
            'a {} tangled in a net'.format(self.get_character()),
            'a {} playing hide and seek'.format(self.get_character()),
            'a {} playing hide and seek in a {}'.format(self.get_character(), self.get_env()),
            'a {} examining human technology'.format(self.get_character()),
            'a mermaid from a {} story'.format(get_genre()),
            'a mermaid who lives in a pool',
            'a tiny mermaid who lives in a fish tank',
            'a mermaid who lives in an aquarium',
            'a beached mermaid',
            'a mermaid rescued by a sailor',
            'a {}\'s first trip to the shore'.format(self.get_character()),

            'a sea witch',
            'a freshwater mermaid',
            'a mermaid from the arctic',
            'a mermaid from the tropics',
            'a mermaid living in a desert oasis',
            'a mermaid from a river',
            'a mermaid from a swamp',
            'a friendly mermaid',
            'a malevolent mermaid',
            'a cruel mermaid',
            'a {} merchant'.format(self.get_character()),
        ]

    @staticmethod
    def get_character():
        """
        Helper function which returns a random mermaid.
        :return: string
            A mermaid based on a random fish.
        """
        merfolk = "mermaid"
        if randint(0,3) == 0:
            merfolk = "merman"
        return '{} {}'.format(get_animal('fish'), merfolk)

    def get_env(self):
        """
        Helper function which returns an environment.
        :return: string
            Returns a random entry from self.environment
        """
        return libraries.get_one(self.environment)

    def get_scene(self):
        """
        Helper function which returns a random scene.
        :return: string
            Returns a random scene.
        """
        return libraries.get_one(self.scene)

    def get_prompt(self):
        """
        Returns a MerMay prompt.
        :return: string
            Returns a mermaid-themed prompt.
        """
        if randint(0,3) == 0:
            return self.get_scene()
        else:
            return self.generate_character()


if __name__ == '__main__':
    c = Mermay()
    print c.generate_character()
    print c.get_prompt()
