from random import randint

instruments = [
    # A - E
    'accordion', 'acoustic guitar', 'aeolian harp', 'alphorn', 'balalaika', 'bagpipes', 'banjo', 'bamboo flute', 'barrel drum', 'basset horn', 'bass drum', 'bass guitar', 'bassoon', 'bell', 'bugle', 'bullroarer', 'Burmese harp', 'bongos', 'calliope', 'castanets', 'cello', 'chimes', 'ching', 'Chinese lute', 'Chinese zither', 'cigar box guitar', 'clarinet', 'clavichord', 'concertina', 'congas', 'cornet', 'cowbell', 'crumhorn', 'cymbals', 'didgeridoo', 'double bass', 'double contrabass flute', 'electric guitar', 'electric organ', 'euphonium',
    # F - J
    'fiddle', 'finger cymbals', 'flute', 'flugelhorn', 'folgerphone', 'frame drum', 'French horn', 'fretted dulcimer', 'glass harp', 'goblet drum', 'gong', 'guitar', 'hand drum', 'hanging drum', 'hammered dulcimer', 'handbells', 'harmonica', 'harp', 'harp guitar','harpsichord', 'horn', 'horsehead fiddle', 'hurdy gurdy', 'jingle bell', 'jug',
    # K - O
    'koto', 'lithophone', 'lute', 'lyre', 'mandolin', 'maracas', 'marimba', 'melodica', 'metallophone', 'mouth harp', 'musical bow', 'musical saw', 'musical spoons', 'nose flute', 'nyckelharpa', 'oboe', 'ocarina',
    # P - T
    'pan pipes', 'piano', 'piccolo', 'pipe organ', 'ratchet', 'recorder', 'saxophone', 'serpent' 'shamisen', 'shekere', 'shell trumpet', 'sheng', 'shofar', 'singing bowl', 'sitar', 'skiffle bass', 'slide whistle', 'slit drum', 'snare drum', 'sousaphone', 'spike fiddle', 'steel drum', 'steel guitar', 'Stylophone', 'synthesizer', 'taiko drum', 'talking drum', 'tambourine', 'tanbur', 'theorbo', 'theremin', 'thumb piano', 'timpani', 'tom-tom', 'triangle', 'trombone', 'tromboon', 'trumpet', 'tuba',
    # U - Z
    'udu', 'ukulele', 'valiha', 'veena', 'vibraphone', 'viola', 'violin', 'vuvusela', 'washboard', 'washtub bass', 'whirly tube', 'whistle', 'wooden flute', 'xylophone', 'zither'
]


def get_instrument():
    return instruments[randint(0, len(instruments)-1)]