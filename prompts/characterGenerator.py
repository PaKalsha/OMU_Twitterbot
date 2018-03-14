from random import randint

from concepts.emotions import get_emotion

from nouns.animals import get_animal


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

        self.adjectives = (
            # Emotions
            'lovestruck', 'giddy', 'sleepy', 'angry', 'playful', 'curious', 'silly', 'laughing', 'joyful', 'happy',
            'hopeful', 'confident', 'powerful', 'peaceful', 'surprised', 'eager', 'excited', 'glorious', 'fascinated',
            'compassionate', 'cheerful', 'glamorous', 'determined', 'enthusiastic', 'satisfied', 'courageous',
            'relaxed', 'tired', 'concerned', 'apprehensive', 'flustered', 'rude', 'confused', 'exasperated', 'sad',
            'lonely', 'suspicious', 'grief-stricken', 'morose', 'serious', 'glum', 'aggressive', 'wary', 'nervous',
            'upset', 'envious', 'hungry', 'protective', 'confused', 'smug', 'penitent',

            # Descriptors
            'masked', 'magical', 'cute', 'ancient', 'regal', 'mystical', '{}-like'.format(get_animal('mammal')),
            'interstellar', 'evil', 'corrupt'
        )

    def get_character(self):
        index_limit = len(self.char_type) - 1
        return self.char_type[randint(0, index_limit)]

    def get_prompt(self, character=None):
        # emotion = get_emotion('all')
        if character is None:
            character = self.get_character()

        index_limit = len(self.adjectives) - 1
        desc = self.adjectives[randint(0, index_limit)]

        return '{} {}'.format(desc, character)


if __name__ == '__main__':
    c = CharacterGenerator()
    print c.get_prompt()
    print c.get_prompt('{} mermaid'.format(get_animal('fish')))
