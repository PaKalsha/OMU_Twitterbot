from random import randint


def get_one(base_list):
    """
    Returns one item from the specified library.
    :param base_list: list
        The list to choose an item from.
    :return: string
        A random library entry.
    """
    index_limit = len(base_list) - 1
    return base_list[randint(0, index_limit)]
