from random import shuffle, randint

animals = {
    'mammal': (
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
    ),

    'bird': (
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
    ),

    # 'fish' includes aquatic mammals to make creating mermaids easier
    'fish': (
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
    ),

    # 'reptiles' includes reptiles and amphibians
    'reptile': (
        'anaconda', 'alligator', 'axolotl', 'boa', 'caiman', 'cobra', 'chameleon', 'crocodile', 'dinosaur',
        'frilled lizard', 'frog', 'gecko', 'iguana', 'newt', 'komodo dragon', 'python', 'rattlesnake', 'salamander',
        'snake', 'stegosaurus', 'toad', 'terrapin', 'tortoise', 'turtle', 'tyrannosaur', 'viper'
    ),

    # 'insects' includes insects and arachnids
    'insect': (
        'ant', 'bee', 'beetle', 'butterfly', 'caterpillar', 'centipede', 'cicada', 'cockroach', 'cricket', 'dragonfly',
        'earthworm', 'earwig', 'flea', 'fly', 'gnat', 'grasshopper', 'hornet', 'locust', 'louse', 'maggot', 'millipede',
        'mosquito', 'moth', 'scarab', 'scorpion', 'slug', 'spider', 'snail', 'stag beetle','tardigrade', 'termite', 'wasp',
        'weevil',
    ),

    'mythical': (
        'basilisk', 'bigfoot', 'bogle', 'bunyip', 'chimera', 'chupacabra', 'cockatrice', 'cyclops', 'dragon', 'gremlin',
        'griffon', 'hydra', 'imp', 'kelpie', 'kraken', 'manticore', 'mermaid', 'Mongolian death worm', 'mothman',
        'nandi bear', 'ogre', 'orc', 'owlman', 'pegasus', 'phoenix', 'roc', 'sasquatch', 'skunk ape', 'tanuki', 'troll',
        'unicorn', 'will-o\'-the-wisp', 'wyvern', 'yale', 'yeti'
    )
}


def get_animal(animal_type):
    """
    Returns a single animal of the required type.
    :param animal_type: List or string
        Which animals to include in the selection.
    :return animal_list: string
        A single animal of the required type.
    """
    try:

        family = animals[animal_type.lower()]

    except KeyError:
        family = [get_menagerie('all', num=1)]

    index_limit = len(family) - 1
    creature = family[randint(0, index_limit)]

    return creature


def get_menagerie(animal_type, num=3):
    """
    Returns a list of animals of the required type.
    :param animal_type: List or string
        Which animals to include in the selection.
    :param num: int
        Number of animals to return.
    :return animal_list: List
        A list of animals of the required type.
    """
    animal_list = []

    if animal_type is 'all':
        animal_type = [
            'mammal',
            'bird',
            'fish',
            'reptile',
            'insect',
        ]

    try:

        animal_list += animals[animal_type]

    except TypeError:
        for family in animal_type:
            animal_list += animals[family]
    except KeyError:
        return get_menagerie('all', num=num)

    shuffle(animal_list)
    if num == 1:
        return animal_list[0]

    try:

        return animal_list[0:num]

    except TypeError:
        return animal_list[0]


if __name__ == '__main__':
    print get_animal('mythical2')
    print get_menagerie('all2', num=3)
