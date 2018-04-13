import libraries

genres = {
    'comedy': ['black comedy', 'comic fantasy', 'comedy horror', 
                'parody', 'romantic comedy', 'satire', 'zombie comedy'],
    'crime': ['courtroom drama', 'detective', 'gangster', 'hardboiled crime', 'murder mystery'],
    'fantasy': ['contemporary fantasy', 'dark fantasy', 'fairy fale', 'gaslamp fantasy', 'heroic fantasy',
                 'high fantasy', 'magical girl', 'mythic', 'science fantasy', 'urban fantasy'],
    'historical': ['alternate history', 'costume drame', 'historical fiction',],
    'horror': ['ghost', 'monster', 'kaiju', 'occult horror', 'slasher', 'suvival horror'],
    'political': ['dystopian', 'survivalism', 'utopian'],
    'romance': ['paranormal romance', 'romance'],
    'science fiction': ['atompunk', 'biopunk', 'cyberpunk', 'dieselpunk', 'post-apocalyptic',
                         'science fiction', 'space opera', 'space western', 'steampunk', 'tech-noir'],
    'speculative': ['magical realism', 'superhero', 'weird fiction'],
    'thriller': ['crime thriller', 'disaster', 'psychological thriller', 'techno-thriller',],
    'other': ['absurdist', 'action', 'adventure', 'medical drama', 'mystery', 'philosophical', 'propaganda',
              'saga', 'slice of life', 'surreal', 'teen drama', 'urban', 'western']
}


def get_genre(category='all'):
    """
    Return a random genre.
    :param category: string
        Return a genre from this super-category.
    :return: string
        A  random genre.
    """
    if category is 'all':
        genre_list = []
        for cat in genres.keys():
            genre_list.append(get_genre(cat))
        return libraries.get_one(genre_list)

    else:
        return libraries.get_one(genres[category.lower()])


if __name__ == '__main__':
    print get_genre()
