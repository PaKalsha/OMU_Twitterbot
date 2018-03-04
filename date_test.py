from datetime import datetime
from random import randint

now = datetime.now()

weekly = [
    "view from a window", "dream car", "coins"
]
illustration = [
    "ninja battle", "whatever you do, keep your eyes on me", "haunted painting studio", "abandoned opera house",
    "kaiju attack", "campfire tales", "saving a sleepwalker from themself", "an astonishing slice of cake",
    "a fairytale gatecrashing a birthday party", "zombie apocalypse ... on ice!"
]
object_adjectives = [
    "rusted", "shattered", "tangled", "knotted", "polished", "wooden"
]

general_opinion = []
specific_opinion = []

# #####
# size
# #####

size_l = ["enormous", "colossal", "huge", "massive", "immense", "large", "huge", "immense"]
size_m = ["middling", "moderate", "standard-sized", "normal-sized"]
size_s = ["tiny", "small", "miniature", "pint-sized", "undersized", "stunted", "short"]

shape = []
age = []
# #####
# colours
# #####

variants = ["dark", "light", "deep", "pale"]

pink = ["pink", "hot pink", "coral", "violet-red", "salmon"]
red = ["red", "Indian red", "crimson", "firebrick red", "coral", "tomato red", "salmon"]
orange = ["orange-red", "tomato", "coral", "orange"]
yellow = ["yellow", "lemon yellow", "peach", "gold", "khaki"]
brown = ["maroon", "brown", "sienna", "saddle brown", "chocolate", "sand", "tan", "wheat"]
green = [
    "olive green", "yellow green", "acid green", "lime green", "grass green", "emerald green",
    "spring green", "green", "sea green", "aquamarine", "forest green"
]
cyan = ["aquamarine", "cyan", "turquoise", "sea green", "teal"]
blue = [
    "steel blue", "blue", "powder blue", "sky blue", "royal blue", "dark blue", "navy blue", "azure"
]
purple = ["lavender", "plum", "violet", "fuschia", "magenta", "purple", "indigo", "slate blue"]
white = ["white", "ivory", "cream", "linen", "antique white", "beige"]
grey = ["gray", "silver", "slate gray", "smoke gray"]
black = ["black", "midnight blue", "charcoal", "ebony", "onyx", "jet black"]
fictional_colours = ["octarine", "blurple", "ultra indigo"]

# #######
# Character design
# #######

char_types = [
    "fairy princess", "trickster fox", "class clown", "tsundere", "dragon shepard", "plumber-turned-hero",
    "pair of stowaways", "star-crossed lovers", "survivalist", "wizard", "cleric", "priest", "warrior", "soldier",
    "guard", "barbarian", "mayor", "trader", "captain"
]
char_adjectives = [
    "masked", "magical", "cute", "ancient", "regal", "mystical"
]
emotions = [
    "lovestruck", "giddy", "sleepy", "angry", "playful", "curious", "silly", "laughing", "joyful", "happy", "hopeful",
    "confident", "powerful", "peaceful", "surprised", "eager", "excited", "glorious", "fascinated", "compassionate",
    "cheerful", "glamorous", "determined", "enthusiastic", "satisfied", "courageous", "relaxed",
    "tired", "concerned", "apprehensive", "flustered", "rude", "confused", "exasperated", "sad", "lonely", "suspicious",
    "grief-stricken", "morose", "serious", "glum", "aggressive", "wary", "nervous", "upset", "envious", "hungry",
    "protective", "confused", "smug", "penitent"
]
animal = [
    "cat", "dog", "pig", "owl", "ape", "fox"
]

# #######
# Valentine
# #######

# #######
# Mermay
# #######

mermay_adj = [
    "koi", "lionfish", "shark", "manta-ray", "jellyfish", "mackerel", "catfish", "pufferfish", "clownfish",
    "squid", "orca", "whale", "seahorse", "pike", "lobster", "crab", "anglerfish", "manatee"
]

# #######
# Halloween
# #######

halloween_noun = [
    "mummy", "werewolf", "vampire", "ghost", "goblin", "witch", "horseman", "mothman", "kaiju", "faceless man",
    "pig-faced woman", "mermaid", "goatman", "mothman", "ninja", "shadow", "black cat", "black dog", "creature",
    "reflection", "demon", "devil", "something", "doll", "puppet", "clown", "zombie", "brain in a jar", "mad scientist",
    "costume", "skeleton", "lake monster", "homunculus", "skull", "raven", "stranger", "owl", "ghoul", "warlock",
    "boogeyman", "familiar", "were-beast", "hellhound", "kaiju"
]
halloween_adj = [
    "slimy", "bloody", "headless", "ominous", "haunted", "creeping", "creepy", "watchful", "vengeful",
    "malevolent", "radioactive", "alien", "evil", "cursed", "sinister", "bizarre", "spidery", "tentacled",
    "many-limbed", "grotesque", "lurking", "burning", "skeletal", "mouldy", "rotten", "frost-bitten", "infected",
    "patchwork", "poisonous", "spiked", "fanged", "spectral", "eerie", "macabre", "otherworldly", "screaming",
    "cobwebbed", "parasitic", "uncanny", "grim", "body-snatching", "many faced", "uncanny", "gloomy", "scaly",
    "luminescent", "glowing", "reflective", "delicate", "twisted", "clockwork"
]
halloween_desc = [
    "made of bones", "from a nightmare", "in disguise", "made of clay",
    "with the head of a {}".format(animal[randint(0, len(animal)-1)])
]

nope_combo = {
    "ghost": "spectral",
    "pig-faced woman": [
        "with the head of a cat",
        "with the head of a dog",
        "with the head of a pig",
        "with the head of a fox",
        "with the head of a owl"
    ],
    "skeleton": "skeletal",
    "skull": "skeletal",
    "owl": "with the head of an owl",
    "black cat": "with the head of a cat",
    "black dog": "with the head of a dog",
    "hellhound": "with the head of a dog"
}


def character_design(character):
    desc = emotions + char_adjectives
    subject = desc[randint(0, len(desc)-1)] + " " + character
    return subject


def halloween_prompt():
    noun = halloween_noun[randint(0, len(halloween_noun)-1)]
    adjs = emotions + char_adjectives + halloween_adj
    rand = randint(0, (len(adjs) + len(halloween_desc)-1))

    if rand <= (len(adjs)-1):
        subject = adjs[rand] + " " + noun
    else:
        rand %= (len(halloween_desc) - 1)
        subject = noun + " " + halloween_desc[rand]
    if subject in nope_combo.keys():
        if (adjs[rand] in nope_combo[subject]) or (halloween_desc[rand] in nope_combo[subject]):
            halloween_prompt()
    return subject


# #######
# Yuletide
# #######

# todo: Month of Love theme
# todo: yuletide theme
# todo: proper character design generator
# todo: noun-noun combinaions
# todo: landscapes

hashtags = "#drawingprompt"

if now.month == 2:
    prompt = halloween_prompt()
    hashtags += " #monthoflove"

if now.month == 5:
    prompt = character_design(character=mermay_adj[randint(0, len(adjectives)-1)] + " mermaid")
    hashtags += " #mermay"

elif now.month == 10:
    prompt = halloween_prompt()
    hashtags += " #inktober"

elif now.month == 11:
    prompt = halloween_prompt()
    hashtags += " #monthoffear"

elif now.weekday() == 5:
    prompt = illustration[randint(0, (len(illustration)-1))]
    hashtags += " #illustration"

elif now.weekday() == 6:
    prompt = character_design(character=char_types[randint(0, len(char_types)-1)])
    hashtags += " #characterdesign"
else:
    prompt = weekly[randint(0, (len(weekly)-1))]


tweet = "++ DAILY DRAWING PROMPT {:%Y%m%d}: {} ++\n{}".format(now, prompt.upper(), hashtags)
print tweet
print len(tweet)
