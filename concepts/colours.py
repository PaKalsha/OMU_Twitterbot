from random import randint

shades = ('dark', 'light', 'deep', 'pale', 'pastel', 'neon')

colours = {
    'pink': ('pink', 'hot pink', 'coral', 'violet-red', 'salmon'),

    'red': ('red', 'Indian red', 'crimson', 'firebrick red', 'coral', 'tomato red', 'salmon'),

    'orange': ('orange-red', 'tomato', 'coral', 'orange'),

    'yellow': ('yellow', 'lemon yellow', 'peach', 'gold', 'khaki'),

    'brown': ('brown', 'maroon', 'brown', 'sienna', 'saddle brown', 'chocolate', 'sand', 'tan', 'wheat'),

    'green': (
        'olive green', 'yellow-green', 'acid green', 'lime green', 'grass green', 'emerald green', 'spring green',
        'green', 'sea green', 'aquamarine', 'forest green'
    ),

    'cyan': ('aquamarine', 'cyan', 'turquoise', 'sea green', 'teal'),

    'blue': ('steel blue', 'blue', 'powder blue', 'sky blue', 'royal blue', 'dark blue', 'navy blue', 'azure'),

    'purple': ('lavender', 'plum', 'violet', 'fuschia', 'magenta', 'purple', 'indigo', 'slate blue'),

    'white': ('white', 'ivory', 'cream', 'linen', 'antique white', 'beige'),

    'grey': ('gray', 'silver', 'slate gray', 'smoke gray'),

    'black': ('black', 'midnight blue', 'charcoal', 'ebony', 'onyx', 'jet black'),

    'fictional': (
        'octarine', 'blurple', 'ultra indigo', 'actinic', 'infra-white', 'kalish', 'amarklor', 'zurple',
        'jale', 'ulfire'
    )
}


def get_shade():
    """
    Picks a random shade modifier.
    :return: string
        Random shade modifier.
    """
    index_limit = len(shades) - 1
    return shades[randint(0, index_limit)]


def get_colour(hue, shade=False):
    """
    Generates a random colour.
    :param hue: string
        The colour family to choose from.
    :param shade: bool
        Whether or not to tint the colour.
    :return: string
        A randomised colour.
    """
    colour_range = colours[hue.lower()]
    index_limit = len(colour_range) - 1

    colour = colour_range[randint(0, index_limit)]
    if shade is True:
        colour = '{} {}'.format(get_shade(), colour)
    return colour


def get_palette(hues, palette=None):
    """
    Creates a palette of colours.
    :param hues: list
        List of colours to include in the palette.
    :param palette: list
        Colours already included in palette.
    :return: list
        Returns list of colours.
    """
    if isinstance(palette, list):
        palette = palette
    else:
        palette = []

    for colour in hues:
        new_colour = get_colour(colour, shade=True)
        if new_colour not in palette:
            palette.append(new_colour)
        else:
            get_palette([colour], palette)
    return palette


if __name__ == '__main__':
    print get_colour(hue='red')
    print get_palette(hues=['grey']*3, palette=['neon slade grey'])
