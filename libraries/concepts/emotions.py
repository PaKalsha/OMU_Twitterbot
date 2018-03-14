import libraries

emotions = {
    'love': ('adoring', 'affectionate', 'broody', 'caring', 'compassionate', 'infatuated', 'longing', 'lovestruck',
             'lustful', 'passionate', 'sentimental', 'sensuous'),
    'joy': ('carefree', 'cheerful', 'delighted', 'ecstatic', 'eager', 'enthusiastic', 'euphoric', 'excited', 'giddy',
            'gleeful', 'grateful', 'happy', 'playful', 'proud', 'joyful', 'radiant', 'relieved', 'satisfied', 'silly'),
    'anger': ('aggressive', 'angry', 'cheesed off', 'disgruntled', 'envious', 'exasperated', 'frustrated', 'furious',
              'huffy', 'indignant', 'insulted', 'irritated', 'jealous', 'miffed', 'piqued', 'vengeful'),
    'sad': ('apathetic', 'despairing', 'disappointed', 'glum', 'grief-stricken', 'grieving', 'lonely', 'melancholy',
            'nostalgic', 'morose', 'penitent', 'remorseful', 'sad', 'upset'),
    'fear': ('apprehensive', 'anxious', 'awed', 'fearful', 'nervous', 'panicky', 'paranoid', 'suspicious', 'wary',
             'worried'),
    'disgust': ('ashamed', 'contemptuous', 'disgusted', 'nauseous', 'revolted'),
    'surprise': ('astonished', 'baffled', 'befuddled', 'bewildered', 'confused', 'shocked', 'embarrassed', 'shocked',
                 'surprised'),
    'curious': ('curious', 'enchanted', 'fascinated', 'quizzical', 'wondering'),
}

feelings_of = ('anticipation', 'boredom', 'claustrophobia', 'dismay', 'dread', 'gratitude', 'hatred', 'homesickness',
               'hope', 'humility', 'hunger', 'impatience', 'nostalgia', 'pity', 'regret', 'reluctance',  'resentment',
               'self-pity', 'sleepiness', 'terror', 'tiredness', 'vulnerability', 'wanderlust', 'wonder')


def get_feeling():
    """

    :return:
    """
    return libraries.get_one(feelings_of)


def get_emotion(emotion_type='all'):
    """
    Get random emotion.
    :return: string
        A  random emotion.
    """
    emotion_list = []
    if emotion_type == 'all':
        emotion_type = [
            'love',
            'joy',
            'anger',
            'sad',
            'fear',
            'disgust',
            'surprise',
            'curious',
        ]

    try:
        emotion_list += emotions[emotion_type]

    except TypeError:
        for family in emotion_type:
            emotion_list += emotions[family]
    except KeyError:
        return get_emotion('all')

    return libraries.get_one(emotion_list)


if __name__ == '__main__':
    print 'feeling {}'.format(get_emotion())
    print get_feeling()
