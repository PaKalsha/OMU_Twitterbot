import libraries

shades = ('dark', 'light', 'deep', 'pale', 'pastel', 'neon')

colors = {
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
    return libraries.get_one(shades)


def get_color(hue, shade=False):
    """
    Generates a random colour.
    :param hue: string
        The colour family to choose from.
    :param shade: bool
        Whether or not to tint the colour.
    :return: string
        A randomised colour.
    """
    color = libraries.get_one(colors[hue.lower()])

    if shade is True:
        color = '{} {}'.format(get_shade(), color)
    return color


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

    for color in hues:
        new_color = get_color(color, shade=True)
        if new_color not in palette:
            palette.append(new_color)
        else:
            get_palette([color], palette)
    return palette


if __name__ == '__main__':
    print get_shade()
    print get_color('red', shade=True)
    print get_palette(hues=['grey']*3, palette=['neon slade grey'])
