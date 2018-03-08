from random import shuffle

mammal = [
    # A - E
    'aardvark', 'alpaca', 'anteater', 'antelope', 'ape', 'armadillo', 'baboon', 'badger', 'bat', 'bear', 'beaver',
    'bison', 'boar', 'bongo', 'buffalo', 'bull', 'camel', 'caribou', 'cat', 'cheetah', 'chimpanzee', 'chinchilla',
    'coyote', 'cow', 'deer', 'dog', 'donkey', 'echidna', 'eland', 'elephant', 'elephant seal', 'elk',
    # F - J
    'ferret', 'fish', 'fox', 'frog', 'gazelle', 'gerbil', 'giant panda', 'giraffe', 'gnu', 'goat', 'gorilla',
    'guanaco', 'guinea pig', 'hamster', 'hare', 'hedgehog', 'horse', 'hyena', 'ibex', 'jackal', 'jaguar',
    # K - O
    'kangaroo', 'kinkajou', 'koala', 'kouprey', 'kudu', 'lemur', 'leopard', 'lion', 'llama', 'loris', 'mammoth',
    'mandrill', 'mink', 'mole', 'mongoose', 'monkey', 'moose', 'mouse', 'ocelot', 'okapi', 'opossum', 'otter',
    # P - T
    'panther', 'panda', 'pig', 'polar bear', 'pony', 'porcupine', 'prairie dog', 'rabbit', 'raccoon', 'ram', 'rat',
    'red deer', 'red panda', 'reindeer', 'rhinoceros', 'sheep', 'shrew', 'seal', 'sea lion', 'skunk', 'sloth',
    'squirrel', 'tapir', 'tiger',
    # U - Z
    'uakari', 'vicuna', 'wallaby', 'walrus', 'water buffalo', 'weasel', 'wolf', 'wolverine', 'wombat', 'yak', 'zebra'
]

aves = [
    # A - E
    'albatross', 'cassowary', 'chicken', 'chough', 'cormorant', 'crane', 'crow', 'curlew', 'dotterel', 'dove',
    'duck', 'dunlin', 'eagle', 'emu',
    # F - J
    'falcon', 'finch', 'flamingo', 'goldfinch', 'goosander', 'goose', 'goshawk', 'grouse', 'guinea fowl', 'gull',
    'hawk', 'heron', 'hoopoe', 'hummingbird', 'ibis', 'jay',
    # K - O
    'lapwing', 'lark', 'linnet', 'lyrebird', 'magpie', 'mallard', 'nightingale', 'ostrich', 'owl',
    # P - T
    'parrot', 'partridge', 'peafowl', 'pelican', 'penguin', 'pheasant', 'pigeon', 'quail', 'quelea', 'quetzal',
    'raven', 'red-tailed hawk', 'rook', 'rooster', 'sandpiper',  'starling', 'swan', 'turkey',
    # U - Z
    'umbrellabird', 'wren',
]

# 'fishies' includes aquatic mammals to make creating mermaids easier
fishies = [
    # A - E
    'angelfish', 'anglerfish', 'barracuda', 'basking shark', 'blobfish', 'blue whale', 'catfish', 'cod', 'clownfish',
    'crab', 'dogfish', 'dolphin', 'dragonfish', 'dugong', 'eel', 'electric eel',
    # F - J
    'hagfish', 'herring', 'horseshoe crab', 'humpback whale', 'jellyfish',
    # K - O
    'koi', 'leafy seadragon', 'lionfish', 'lobster', 'mackerel', 'manatee', 'manta-ray', 'megalodon', 'mola mola',
    'moray eel', 'narwhal', 'octopus', 'orca', 'oyster',
    # P - T
    'pike', 'porpoise', 'pufferfish', 'salmon', 'sand dollar', 'sardine', 'sawfish ', 'sea urchin', 'seahorse',
    'sea snake', 'sea turtle', 'shark', 'squid', 'stingray', 'sturgeon', 'swordfish',
    # U - Z
    'unicornfish', 'X-ray tetra', 'whale'
]

# 'scalies' includes reptiles and amphibians
scalies = [
    'anaconda', 'alligator', 'axolotl', 'boa', 'caiman', 'cobra', 'chameleon', 'crocodile', 'dinosaur',
    'frilled lizard', 'frog', 'gecko', 'iguana', 'newt', 'komodo dragon', 'python', 'rattlesnake', 'salamander',
    'snake', 'stegosaurus', 'toad', 'terrapin', 'tortoise', 'turtle', 'tyrannosaur', 'viper'
]

# 'bugs' includes insects and arachnids
bugs = [
    'ant', 'bee', 'beetle', 'butterfly', 'caterpillar', 'centipede', 'cicada', 'cockroach', 'cricket', 'dragonfly',
    'earthworm', 'earwig', 'flea', 'fly', 'gnat', 'grasshopper', 'hornet', 'locust', 'louse', 'maggot', 'millipede',
    'mosquito', 'moth', 'scarab', 'scorpion', 'slug', 'spider', 'snail', 'stag beetle','tardigrade', 'termite', 'wasp',
    'weevil',
]

legendary = ['basilisk', 'bigfoot', 'bogle', 'bunyip', 'chimera', 'chupacabra', 'cockatrice', 'cyclops', 'dragon',
             'gremlin', 'griffon', 'hydra', 'imp', 'kelpie', 'kraken', 'manticore', 'mermaid', 'Mongolian death worm',
             'mothman', 'nandi bear', 'ogre', 'orc', 'owlman', 'pegasus', 'phoenix', 'roc', 'sasquatch', 'skunk ape',
             'tanuki', 'troll', 'unicorn', 'will-o\'-the-wisp', 'wyvern', 'yale', 'yeti']


def get_animals(
        num=1,
        mammals=False,
        birds=False,
        fish=False,
        reptiles=False,
        insects=False,
        mythical=False,
        all=False
):
    """
    Returns a list of animals of the required type
    :param num: int
        Number of animals to return
    :param mammals:Bool
        Include mammals in the returned list
    :param birds: Bool
        Include birds in the returned list
    :param fish: Bool
        Include fish in the returned list
    :param reptiles: Bool
        Include reptiles and amphibians in the returned list
    :param insects: Bool
        Include insects and arachnids in the returned list
    :param mythical: Bool
        Include mythical creatures in the returned list
    :param all: Bool
        Shortcut to include all real animals
    :return animal_list: List
        A list of animals of the required type
    """
    animal_list = []

    if all is True:
        mammals = True
        birds = True
        fish = True
        reptiles = True
        insects = True

    if mammals is True:
        animal_list += mammal
    if birds is True:
        animal_list += aves
    if fish is True:
        animal_list += fishies
    if reptiles is True:
        animal_list += scalies
    if insects is True:
        animal_list += bugs
    if mythical is True:
        animal_list += legendary

    shuffle(animal_list)
    try:
        return animal_list[0:num]
    except TypeError:
        return animal_list[0]


if __name__ == '__main__':
    print get_animals(num=3, reptiles=True)