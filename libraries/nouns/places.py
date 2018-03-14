import libraries

places = [
    # A - E
    'abby', 'airport', 'aquarium', 'bank', 'bakery', 'basilica', 'bridge', 'bus station', 'cafe', 'campsite', 'casino',
    'castle', 'cathedral', 'church', 'cinema', 'city wall', 'dentist',
    # F - J
    'fort', 'gallery', 'garden', 'gym', 'hospital', 'hotel', 'house', 'hot spring', 'jail',
    # K - O
    'karaoke bar', 'laundromat', 'library', 'lighthouse', 'market', 'mosque', 'museum', 'observatory', 'opera house',
    # P - T
    'painting studio', 'palace', 'prison', 'restaurant', 'school', 'ship', 'shop', 'shrine', 'stadium', 'synagogue',
    'temple', 'tower', 'train station',
    # U - Z
    'warehouse', 'windmill', 'zoo'
]


def get_place():
    """
    Get a random location.
    :return: string
        A random location from the places list.
    """
    return libraries.get_one(places)


if __name__ == '__main__':
    print get_place()