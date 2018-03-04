import tweepy

from time import sleep
from datetime import datetime
from random import randint

from credentials import *

####
# todo: Valentine's theme
# todo: yuletide theme
# todo: proper character design generator
# todo: noun-noun combinaions
# todo: landscapes
# todo: general_opinion
# todo: specific_opinion
# todo: shape
# todo: age
# todo: prompt database
####

####
# Setup Tweepy
####
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

####
# Tweet prompts
####

weekday_prompts = [
    # people
    'someone siting in an odd pose',
    'family members with things that are important to them',
    'yourself (or someone else) painting toenails',
    'a crowd of people',
    'draw a relative by the light cast from a screen',
    'a portrait of yourself in twenty years',
    'a masked man (or woman) that is not a superhero',
    'the ugliest baby you can imagine',
    'two sports figures - one in a dynamic pose, one in a static pose',
    'two self-portraits with odd expressions',
    'an enormous quantity of hair',
    'someone near you on a bus or in a car',

    # animals
    'an animal eating another animal',
    'your main OC in a fight with an animal',
    'an animal playing a musical instrument',
    'there is an animal living in one of your appliances',
    'a dead bird in a beautiful landscape',
    'draw your pet\'s point of view',
    'an animal taking a bath',
    'an animal taking a human for a walk',
    'combine 3 existing animals to create a completely new creature',
    'a family portrait for a family of insects or animals',
    'an animal playing a game',
    'the most terrifying animal you can imagine',
    'the most adorable animal you can imagine',
    'your ideal pet',

    # food
    'a pile of dishes before they get washed',
    'the best pizza you have ever seen',
    'junk food and the wrapper',
    'your favorite food',
    'draw the ingredients or process of your favorite recipe',
    'salt and pepper shakers',
    'fresh fruit or vegetables',
    'something fresh from the oven',
    'a salad',
    'the oldest thing in your refrigerator',
    'draw a piece of fruit every day until it becomes rotten',
    'everything on a table',

    # objects
    'the image in the rearview mirror of the car',
    'moving water',
    'still water',
    'a floating object',
    'all of your drawing materials',
    'the contents of a trash can',
    'tools that belong to a certain profession',
    'three objects and their environments',
    'an object in motion',
    'the interior of a mechanical object',
    'a mess you made',
    'five objects with different textures',
    'a collection of purses, wallets, or bags',
    'your favorite childhood toy',
    'a well-loved object',
    'a watch, clock or other timepiece',
    'a piece of jewelry',
    'something hideous that you keep for sentimental reasons',
    'something with a mirror image',
    'the contents of your pocket or purse',

    # technical development
    'the contents of your junk drawer',
    'a detailed drawing of a rock',
    'a dark object in a light environment',
    'a light object in a dark environment',
    'a detailed drawing of five square inches of grass',
    'a transparent object',
    'a translucent object',
    'fill a page with studies of eyes, noses, and mouths',
    'an interesting object from three different angles',
    'three eggs and part of the carton with a strong light source',
    'three metallic objects that reflect light',
    'objects partially submerged in water',
    'a drawing using materials with which you are not familiar',
    'a piece of patterned fabric with folds',
    'a bridge and all of its details',
    'the view from a window',

    # something or someone
    'something for which you are thankful',
    'something that can\'t be turned off',
    'something soothing',
    'something you think sounds or smells incredible',
    'something that needs fixing',
    'something you\'ve always wanted',
    'something out of place',
    'something that should have been invented by now',
    'something you keep putting off',
    'something that causes you to procrastinate',
    'something or someone you love',
    'something you\'ve grown out of'

    # creativity
    'yourself as an original superhero',
    'a drawing that looks sticky',
    'a mysterious doorway or staircase',
    'an empty room. Make it interesting',
    'a dangerous flower',
    'an object melting',
    'an imaginary place, adding all kinds of details',
    'a gumball machine that dispenses anything but gumballs',
    'draw yourself in a dangerous situation',
    'draw what\'s under your bed (real or imagined)',
    'an incredible game of hide-and-seek',
    'the car of the future',
    'a drawing that is totally truthful',
    'a drawing that lies all over the place',
    'a drawing that is completely and utterly impossible',
    'ask someone else to tell you what to draw',
    'your greatest fear',
    'a drawing inspired by song lyrics, quotes, or poetry',
    'draw the three most useless objects you can find',
    'an interesting form of transportation',
    'go somewhere new and draw what you see',
    'design your own restaurant. Draw your head chef and today\'s special'
]

####
# Illustration prompts
####

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
]

####
# Modifiers
####

object_adjectives = [
    'rusted', 'shattered', 'tangled', 'knotted', 'polished', 'wooden'
]

# sizes
size_l = ['enormous', 'colossal', 'huge', 'massive', 'immense', 'large', 'huge', 'immense']
size_m = ['middling', 'moderate', 'standard-sized', 'normal-sized']
size_s = ['tiny', 'small', 'miniature', 'pint-sized', 'undersized', 'stunted', 'short']

# colours
variants = ['dark', 'light', 'deep', 'pale']

pink = ['pink', 'hot pink', 'coral', 'violet-red', 'salmon']
red = ['red', 'Indian red', 'crimson', 'firebrick red', 'coral', 'tomato red', 'salmon']
orange = ['orange-red', 'tomato', 'coral', 'orange']
yellow = ['yellow', 'lemon yellow', 'peach', 'gold', 'khaki']
brown = ['maroon', 'brown', 'sienna', 'saddle brown', 'chocolate', 'sand', 'tan', 'wheat']
green = [
    'olive green', 'yellow-green', 'acid green', 'lime green', 'grass green', 'emerald green',
    'spring green', 'green', 'sea green', 'aquamarine', 'forest green'
]
cyan = ['aquamarine', 'cyan', 'turquoise', 'sea green', 'teal']
blue = [
    'steel blue', 'blue', 'powder blue', 'sky blue', 'royal blue', 'dark blue', 'navy blue', 'azure'
]
purple = ['lavender', 'plum', 'violet', 'fuschia', 'magenta', 'purple', 'indigo', 'slate blue']
white = ['white', 'ivory', 'cream', 'linen', 'antique white', 'beige']
grey = ['gray', 'silver', 'slate gray', 'smoke gray']
black = ['black', 'midnight blue', 'charcoal', 'ebony', 'onyx', 'jet black']
fictional_colours = [
    'octarine', 'blurple', 'ultra indigo', 'actinic', 'infra-white', 'kalish', 'amarklor', 'zurple',
    'jale', 'ulfire'
]

# #######
# Character design
# #######

char_types = [
    'fairy princess', 'trickster fox', 'class clown', 'tsundere', 'dragon shepard', 'plumber-turned-hero',
    'pair of stowaways', 'star-crossed lovers', 'survivalist', 'wizard', 'cleric', 'priest', 'warrior', 'soldier',
    'guard', 'barbarian', 'mayor', 'trader', 'captain'
]
char_adjectives = [
    'masked', 'magical', 'cute', 'ancient', 'regal', 'mystical'
]
emotions = [
    'lovestruck', 'giddy', 'sleepy', 'angry', 'playful', 'curious', 'silly', 'laughing', 'joyful', 'happy', 'hopeful',
    'confident', 'powerful', 'peaceful', 'surprised', 'eager', 'excited', 'glorious', 'fascinated', 'compassionate',
    'cheerful', 'glamorous', 'determined', 'enthusiastic', 'satisfied', 'courageous', 'relaxed',
    'tired', 'concerned', 'apprehensive', 'flustered', 'rude', 'confused', 'exasperated', 'sad', 'lonely', 'suspicious',
    'grief-stricken', 'morose', 'serious', 'glum', 'aggressive', 'wary', 'nervous', 'upset', 'envious', 'hungry',
    'protective', 'confused', 'smug', 'penitent'
]
animal = [
    'cat', 'dog', 'pig', 'owl', 'ape', 'fox', 'lion', 'bear'
]

fish = [
    'koi', 'lionfish', 'shark', 'manta-ray', 'jellyfish', 'mackerel', 'catfish', 'pufferfish', 'clownfish',
    'squid', 'orca', 'whale', 'seahorse', 'pike', 'lobster', 'crab', 'anglerfish', 'manatee', 'mola mola'
]

# Halloween
halloween_noun = [
    'mummy', 'werewolf', 'vampire', 'ghost', 'goblin', 'witch', 'horseman', 'mothman', 'kaiju', 'faceless man',
    'mermaid', 'goatman', 'mothman', 'ninja', 'shadow', 'black cat', 'black dog', 'creature', 'hellhound', 'doll',
    'reflection', 'demon', 'devil', 'something', 'puppet', 'clown', 'zombie', 'brain in a jar', 'mad scientist',
    'costume', 'skeleton', 'lake monster', 'homunculus', 'skull', 'raven', 'stranger', 'owl', 'ghoul', 'warlock',
    'boogeyman', 'familiar', 'were-beast'
]
halloween_adj = [
    'slimy', 'bloody', 'headless', 'ominous', 'haunted', 'creeping', 'creepy', 'watchful', 'vengeful',
    'malevolent', 'radioactive', 'alien', 'evil', 'cursed', 'sinister', 'bizarre', 'spidery', 'tentacled',
    'many-limbed', 'grotesque', 'lurking', 'burning', 'skeletal', 'mouldy', 'rotten', 'frost-bitten', 'infected',
    'patchwork', 'poisonous', 'spiked', 'fanged', 'spectral', 'eerie', 'macabre', 'otherworldly', 'screaming',
    'cobwebbed', 'parasitic', 'uncanny', 'grim', 'body-snatching', 'many faced', 'uncanny', 'gloomy', 'scaly',
    'luminescent', 'glowing', 'reflective', 'delicate', 'twisted', 'clockwork'
]
halloween_desc = [
    'made of bones', 'from a nightmare', 'in disguise', 'made of clay',
    'with the head of a {}'.format(animal[randint(0, len(animal)-1)])
]

nope_combo = {
    'ghost': 'spectral',
    'skeleton': 'skeletal',
    'skull': 'skeletal',
    'owl': 'with the head of an owl',
    'black cat': 'with the head of a cat',
    'black dog': 'with the head of a dog',
    'hellhound': 'with the head of a dog'
}


def character_design(character):
    """
    Creates a character from the database.

    :param character: string
        Type of character.
    :return: string
        Description + character.
    """
    desc = emotions + char_adjectives
    subject = desc[randint(0, len(desc)-1)] + ' ' + character
    return subject


def halloween_prompt():
    """
    Hallowe'en-themed character generator.

    :return: string
         Description + character.
    """
    noun = halloween_noun[randint(0, len(halloween_noun)-1)]
    adjs = emotions + char_adjectives + halloween_adj
    rand = randint(0, (len(adjs) + len(halloween_desc)-1))

    if rand <= (len(adjs)-1):
        subject = adjs[rand] + ' ' + noun
    else:
        rand %= (len(halloween_desc) - 1)
        subject = noun + ' ' + halloween_desc[rand]
    if subject in nope_combo.keys():
        if (adjs[rand] in nope_combo[subject]) or (halloween_desc[rand] in nope_combo[subject]):
            halloween_prompt()
    return subject


def post_tweet():
    """
    Construct and post tweet.
    """
    now = datetime.now()
    day = now.weekday()
    month = now.month

    hashtags = '#drawingprompt'

    # special months
    # # May is Mermay
    if month == 5:
        prompt = character_design(character=fish[randint(0, len(fish)-1)] + ' mermaid')
        hashtags += ' #mermay'

    # # October is Spooktober
    elif month == 10:
        prompt = halloween_prompt()
        hashtags += ' #spooktober'

    # Saturdays are illustration days
    elif day == 5:
        prompt = illustration[randint(0, (len(illustration)-1))]
        hashtags += ' #illustration'

    # Sundays are character design
    elif day == 6:
        prompt = character_design(character=char_types[randint(0, len(char_types)-1)])
        hashtags += ' #characterdesign'

    else:
        prompt = weekday_prompts[randint(0, (len(weekday_prompts)-1))]

    tweet = '++ DAILY DRAWING PROMPT {:%Y%m%d}: {} ++\n{}'.format(now, prompt.upper(), hashtags)

    try:

        print tweet
        print len(tweet)
        # api.update_status(status=tweet)
        sleep(5)

    except tweepy.TweepError as e:
        print (e.reason)


if __name__ == '__main__':
    post_tweet()
