from random import randint

sizes = {
    'large': ('colossal', 'elephantine', 'enlarged', 'enormous', 'epic', 'full-sized', 'gargantuan', 'giant', 'grand',
              'great', 'heroic', 'huge', 'hulking', 'humongous', 'immense', 'large', 'larger-than-life', 'mammoth',
              'massive', 'monolithic', 'monstrous', 'monumental', 'mountainous', 'oversized', 'stupendous', 'titanic',
              'tremendous', 'whacking great', 'whopping great'
    ),
    'medium': ('average', 'fair-sized', 'mediocre', 'medium', 'middling', 'moderate', 'normal-sized', 'ordinary',
               'standard', 'unexceptional', 'unremarkable'
    ),
    'small': ('diminutive', 'dinky', 'lilliputian', 'little', 'micro', 'microscopic', 'miniature', 'miniscule',
              'minute', 'petite', 'pint-sized', 'pocket-sized', 'puny', 'runty', 'short', 'slender', 'small', 'stunted',
              'teeny-weeny', 'tiny', 'undersized', 'weeny'
    )
}


def get_size(size):
    """
    Generate a synonym for a given size.
    :param size: string
        Size required: small, medium or large.
    :return: string
        A  random synonym for the size given.
    """
    try:
        index_limit = len(sizes[size.lower()]) - 1
        return sizes[size][randint(0, index_limit)]
    except KeyError:
        raise


if __name__ == '__main__':
    print get_size('small')
