
import libraries

from libraries.nouns.animals import get_animal
from libraries.nouns.places import get_place
from libraries.concepts.colours import get_color
from libraries.concepts.sizes import get_size

from characterGenerator import CharacterGenerator

chara = CharacterGenerator()

illustration = [
    'ninja battle',
    '"whatever you do, keep your eyes on me"',
    'kaiju attack',
    'campfire tales',
    'saving a sleepwalker from themself',
    'an astonishing slice of cake',
    'a fairytale gatecrashing a birthday party',
    'zombie apocalypse ... on ice!',
    'something wicked this way comes',
    'improve a story you like',
    'fix a story that you don\'t like',
    'your character receives a basket of baby {}s'.format(get_animal('mythical')),
    'the voyage home',
    'there and back again',
    'space {}s'.format(get_animal('insect')),
    'king under the mountain',
    'king of the world',
    'queen of the air',
    'queen of the deep blue sea',
    'sunken kingdom',
    'steal the thunder',
    'ride the lightning',
    'lightning in a bottle',
    'things with wings',
    'praise the sun',
    'time travelling pizza delivery',
    'late night at the alien noodle bar',
    'self-portrait',
    'vintage superhero',
    'shiny and chrome',
    'dragon teeth',
    'robot {}'.format(get_animal('all')),
    '{} dentist'.format(get_animal('mythical')),
    'ancient {}'.format(get_animal('mythical')),
    'baby {}'.format(get_animal('mythical')),
    '{} centaur'.format(get_animal('mammal')),
    'urban {}'.format(get_animal('mythical')),
    'high noon'
    'battle between {} and {}'.format(chara.get_character(), get_animal('mythical')),
    'an unlikely {}'.format(chara.get_character()),
    'a case of mistaken identity',
    'mother of {}s'.format(get_animal('mythical')),
    'caveman family',
    'father time',
    'early draft of a famous monument',
    'one of these things is not like the others',
    'in hindsight, it probably wasn\'t a puppy',
    'teenage mutant ninja {}s'.format(get_animal('all')),
    'the king in yellow',
    'birthday party for a tree',
    'an unlikely pet for a {}'.format(chara.get_character()),
    'magical girl duel',
    '{} summoner'.format(get_animal('all')),
    'wrapped up warm',
    'the librarians led the rebellion',
    'old friends',
    'a chance encounter',
    'meet-cute',
    'happy reunion',
    'illuminated by stars',
    'in the limelight',
    'five minutes of fame',
    'island fortress',
    'peace, at last',
    'strange things',
    'dinner for one',
    'dinner for two; better make that three',
    'beowulf vs. the grendel\'s mother',
    'forest spirit',
    'animal sidekick',
    'gentle giant',
    'lost and found',
    'a scene from page 33 of the last story you read',
    'what\'s in the box?',
    'the fifth horseman of the apocalypse',
    'a case of mistaken identity',
    'the spirit of the {}'.format(get_place()),
    'the fairy knight',
    'want and ignorance',
    'illusion and greed',
    'the end boss for a horror game',
    'mystic artifact found in a charity shop',
    '{} {}'.format(get_size('small'),get_animal('mammal')),
    'a mysterious stranger brings a message',
    'a map, and a trap',
    'trouble with the law',
    'help from an unlikely source',
    'the hidden meaning of the message revealed',
    'haunted necklace',
    'a light in the darkness',
    'the longest night',
    'last-ditch effort to make the \'nice\' list',
    'oh, the weather outside is frightful. frightening. actually terrifying',
    'things that should not be made of patchwork',
    'it came upon the midnight clear',
    'magical transformation',
    'snow queen',
    'howl at the moon',
    'creepy child\'s toy',
    'Immelmann turn',
    'battle-scarred pacifist',
    'summer holiday',
    'she who commands the lightning',
    'the old jefferson place',
    'draw a bird in a paper hat',
    'a cute {}'.format(get_animal('all')),
    'an unlikely superhero',
    'in memoriam',
    'in the hall of the mountain king',
    'puppet show',
    'a confrontation',
    'high plains drifter',
    'kitsune',
    'ghost dog',
    'underlord of the mole-people',
    'underwater mage',
    'bittersweet homecoming',
    'a great escape',
    'first contact',
    '{}-dragon'.format(get_animal('mammal')),
    'space pirates',
    'princess of the internet',
    'queen of the night',
    'a ninja fighting a dragon',
    'when she woke up, her first question was "what am I?"',
    'meet me at city hall with 8 forks, a ball of string and a small {} clock'.format(get_color()),

    # quotes
    '"Many\'s the long night I\'ve dreamed of cheese - toasted, mostly"',
    '"This world is made of love and peace"',
    '"we meet at last!"',
    "alternative forms of payment include: sacks of crows",
    '"it\'s adorable, but what is it?"',
    '"(she\'s buying a) stairway to heaven"',
    '"it\'s not a ___, it\'s a time machine!"',
    '"we\'re going on a bear hunt',
    '"I mean, have you ever actually seen your brain?"',
    '"They\'re still not sure it is a baby!"',
    '"This is the receipt for your husband"',
    '"Is this how it starts?"',
    '"What\'s that screaming? A good many dramatic situations begin with screaming..."',
    '"We have done the impossible, and that makes us mighty"',
    '"You\'re telling me gnomes did this?"',
    '"but it\'s my *lucky* ___"',
    '"I don\'t think you\'re the one who deserves a happily ever after"',
    '"I have conquered the wall of death and returned with the spoils of victory"',
    '"my enemies also carry shields"',
    '"let\'s split up and cover more ground"',
    '"the ships hung in the sky in much the same way that bricks don\'t"',
    '"hang on a minute lads, I\'ve got a great idea"',

    # landscapes
    'haunted {}'.format(get_place()),
    'abandoned {}'.format(get_place()),
    'poppy field',
    'wheat field',
    'grassy meadow',
    'lake',
    'fields',
    'forest',
    'a city of ghosts',

    # one-word prompts
    'mask',
    'found',
    'climb',
    'stealthy',
    'hope',
    'paranoia',
    'nostalgia',
    'obsession',
    'firebreak',
    '{}'.format(chara.get_adjective()),
    'renewal',
    'open',
    '{}'.format(get_color()),
    'family',
    'bouquet',
    'brotherhood',
    'camping'
]


def get_prompt():
    """
    Get a random prompt from the illustration list.
    :return: string
        An illustration prompt.
    """
    return libraries.get_one(illustration)


if __name__ == '__main__':
    print get_prompt()
