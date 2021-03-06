import libraries

instruments = [
    # A - E
    'accordion', 'acoustic guitar', 'aeolian harp', 'alphorn', 'balalaika', 'bagpipes', 'banjo', 'bamboo flute',
    'barrel drum', 'basset horn', 'bass drum', 'bass guitar', 'bassoon', 'bell', 'bugle', 'bullroarer', 'Burmese harp',
    'bongos', 'calliope', 'castanets', 'cello', 'chimes', 'ching', 'Chinese lute', 'Chinese zither', 'cigar box guitar',
    'clarinet', 'clavichord', 'concertina', 'congas', 'cornet', 'cowbell', 'crumhorn', 'cymbals', 'didgeridoo',
    'double bass', 'double contrabass flute', 'electric guitar', 'electric organ', 'euphonium',
    # F - J
    'fiddle', 'finger cymbals', 'flute', 'flugelhorn', 'folgerphone', 'frame drum', 'French horn', 'fretted dulcimer',
    'glass harp', 'goblet drum', 'gong', 'guitar', 'hand drum', 'hanging drum', 'hammered dulcimer', 'handbells',
    'harmonica', 'harp', 'harp guitar','harpsichord', 'horn', 'horsehead fiddle', 'hurdy gurdy', 'jingle bell', 'jug',
    # K - O
    'koto', 'lithophone', 'lute', 'lyre', 'mandolin', 'maracas', 'marimba', 'melodica', 'metallophone', 'mouth harp',
    'musical bow', 'musical saw', 'musical spoons', 'nose flute', 'nyckelharpa', 'oboe', 'ocarina',
    # P - T
    'pan pipes', 'piano', 'piccolo', 'pipe organ', 'ratchet', 'recorder', 'saxophone', 'serpent' 'shamisen', 'shekere',
    'shell trumpet', 'sheng', 'shofar', 'singing bowl', 'sitar', 'skiffle bass', 'slide whistle', 'slit drum',
    'snare drum', 'sousaphone', 'spike fiddle', 'steel drum', 'steel guitar', 'Stylophone', 'synthesizer', 'taiko drum',
    'talking drum', 'tambourine', 'tanbur', 'theorbo', 'theremin', 'thumb piano', 'timpani', 'tom-tom', 'triangle',
    'trombone', 'tromboon', 'trumpet', 'tuba',
    # U - Z
    'udu', 'ukulele', 'valiha', 'veena', 'vibraphone', 'viola', 'violin', 'vuvusela', 'washboard', 'washtub bass',
    'whirly tube', 'whistle', 'wooden flute', 'xylophone', 'zither'
]


def get_instrument():
    """
    Returns a list of musical instruments.
    :param num: int
        Number of instruments to return.
    :return instruments: List
        A list of musical instruments.
    """
    return libraries.get_one(instruments)


def get_ensemble(num=3):
    """
    Returns multiple musical instruments.
    :param num: int
        The number of instruments to return.
    :return: set
        A set of musical instruments.
    """
    ensemble = set()
    while len(ensemble) < num:
        ensemble.add(get_instrument())


if __name__ == '__main__':
    print get_instrument()