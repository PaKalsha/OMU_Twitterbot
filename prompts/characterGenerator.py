import libraries

from libraries.nouns.animals import get_animal
from libraries.concepts.emotions import get_emotion

from random import randint


class CharacterGenerator(object):
    def __init__(self):
        self.char_type = (
            # A - E
            'adventurer', 'alchemist', 'animal sidekick', 'animal trainer', 'archaeologist', 'archer', 'armouror',
            'art critic', 'artist', 'assassin',
            'baker', 'bartender', 'barbarian', 'bard', 'battle mage', 'berserker', 'black mage', 'blacksmith',
            'blue mage', 'botanist', 'bouncer', 'bounty hunter', 'boxer', 'builder', 'bully', 'bureaucrat',
            'captain', 'carpenter', 'centaur', 'cheerleader', 'chef', 'chemist', 'child', 'class clown', 'cleric',
            'collector', 'con-artist', 'cook', 'cowboy', 'curmudgeon',
            'dancer', 'demon hunter', 'detective', 'DJ', 'doctor', 'dragoon', 'druid',
            'elder', 'elementalist', 'emperor', 'empress', 'explorer', 'extrovert',
            # F - J
            'fairy princess', 'farmer', 'fencer', 'fisherman', 'fool', 'fusilier',
            'gambler', 'gardener', 'geek', 'geologist', 'geomancer', 'gossip', 'goth', 'gladiator', 'guard',
            'guerrilla fighter', 'guide', 'gunner',
            'hacker', 'healer', 'herald', 'hermit', 'hero', 'homemaker', 'hunter',
            'illusionist', 'introvert', 'inventor',
            'jailbird', 'jester', 'jeweller', 'judge', 'juggler',
            # K - O
            'king', 'knight',
            'librarian',
            'machinist', 'mage', 'martial artist', 'mascot', 'mathematician', 'mayor', 'mechanic', 'medic', 'merchant',
            'mime', 'miner', 'monk', 'musician', 'mystic',
            'necromancer', 'nerd', 'ninja', 'nun', 'nurse',
            'onion knight', 'oracle', 'orator', 'outlaw',
            # P - T
            'painter', 'pair of stowaways', 'paladin', 'performer', 'pilot', 'pirate', 'plumber-turned-hero', 'poet',
            'police officer', 'pop star', 'poacher', 'priest', 'prince', 'princess', 'programmer', 'psychic',
            'pugilist', 'puppeteer',
            'queen',
            'ranger', 'rebel', 'revolutionary', 'rock star', 'romantic',
            'saboteur', 'sage', 'samurai', 'sculptor', 'seer', 'sentinel', 'singer', 'scholar', 'scientist', 'shaman',
            '{} shepard'.format(get_animal('mythical')), 'sky pirate', 'soldier', 'soothsayer', 'sorcerer',
            'special agent', 'spy', 'stagecoach driver', 'star-crossed lovers', 'smuggler', 'summoner', 'survivalist',
            'teacher', 'templar', 'thief', 'tinker', 'time mage', 'tracker', 'trader', 'trainer', 'trickster',
            'tsundere', 'tyrant',
            # U - Z
            'vampire', 'viking', 'villain', 'village elder',
            'waif', 'waiter', 'waitress', 'warrior', 'weaver', 'white mage', 'witch', 'wizard'
        )

        self.adjectives = [
            'masked', 'magical', 'cute', 'ancient', 'regal', 'mystical', '{}-like'.format(get_animal('mammal')),
            'interstellar', 'evil', 'corrupt', 'corrupted', 'glamorous', 'concerned', 'flustered', 'rude', 'serious',
            'protective', 'guilty', 'humiliated', 'reproachful', 'humble', 'overwhelmed', 'content', 'comfortable',
            'victorious', 'calm', 'confident', 'courageous', 'determined', 'powerful', 'peaceful', 'smug', 'triumphant',
            'relaxed', 'glorious', 'laughing', 'hopeful', 'robot'
        ]

        self.description = ['who is out of their depth',
                            'who got more than they bargained for',
                            'from beyond the stars',
                            'from the future']

        self.nope_combo ={
            'romantic': 'romantic'
        }

    def get_character(self):
        """
        Get a character type from self.char_type.
        :return: string
            Returns a single character type.
        """
        return libraries.get_one(self.char_type)

    def get_adjective(self):
        """
        Get a adjective from self.adjectives.
        :return: string
            Returns a single adjective.
        """
        adjective = self.adjectives + [get_emotion()]*len(self.adjectives)
        return libraries.get_one(adjective)

    def get_description(self):
        """
        Get a description from self.description.
        :return: string
            Returns a single description.
        """
        return libraries.get_one(self.description)

    def get_prompt(self, character=None):
        """
        Combines a random character and an emotion or adjective.
        :param character: string
            Specify a character type
        :return: string
            Returns a character design prompt.
        """#
        if character is None:
            character = self.get_character()

        num_descriptions = len(self.adjectives) + len(self.description)
        die = randint(1, num_descriptions)

        if (die - 1) <= len(self.adjectives):
            prompt = '{} {}'.format(self.get_adjective(), character)
            if character in self.nope_combo.keys() and self.adjectives[die] in self.nope_combo[character]:
                prompt = self.get_prompt()
        else:
            prompt = '{} {}'.format(character, self.get_description())
            if character in self.nope_combo.keys() and self.description[0] in self.nope_combo[character]:
                prompt = self.get_prompt()

        return prompt


if __name__ == '__main__':
    c = CharacterGenerator()
    print c.get_prompt()
    print c.get_prompt(get_animal('mammal'))
