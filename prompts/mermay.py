
from prompts.characterGenerator import CharacterGenerator

from libraries.nouns.animals import get_animal


class Mermay(CharacterGenerator):

    def get_character(self):
        """
        Mermaid-themed character generator.
        :return: string
            mermaid character prompt
        """

        return '{} mermaid'.format(get_animal('fish'))


if __name__ == '__main__':
    c = Mermay()
    print c.get_prompt()
