import tweepy

from time import sleep
from datetime import datetime
from random import randint

from credentials import *

from nouns.animals import get_animal


####
# todo: Valentine's theme
# todo: yuletide theme
# todo: proper character design generator
# todo: noun-noun combinaions
# todo: landscapes
# todo: general_opinion
# todo: specific_opinion
# todo: shape
# todo: age
# todo: index_limit / random selector util
####

####
# Setup Tweepy
####
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


####
# Illustration prompts
####

illustration = [
    'ninja battle',
    '"whatever you do, keep your eyes on me"',
    'haunted painting studio',
    'abandoned opera house',
    'kaiju attack',
    'campfire tales',
    'saving a sleepwalker from themself',
    'an astonishing slice of cake',
    'a fairytale gatecrashing a birthday party',
    'zombie apocalypse ... on ice!',
    'something wicked this way comes',
    'improve a story you like',
    'fix a story that you don\'t like',
    'your character receives a basket of baby {}s'.format(get_animal('mythical'))
]

####
# Modifiers
####

object_adjectives = [
    'delicate', 'knotted', 'polished', 'reflective', 'rusted', 'shattered', 'tangled'
]

materials = [
    'metal', 'wooden'
]


def weekday():
    with open('prompts\weekday.txt', 'r') as f:
        prompt_dict = []
        for line in f:
            if line.startswith('#') or line.startswith('\n'):
                pass
            else:
                prompt_dict.append(line.strip())

        index_limit = len(prompt_dict) - 1
        return 'draw {}'.format(prompt_dict[randint(0, index_limit)])


def post_tweet():
    """
    Construct and post tweet based on month and day.
    """
    now = datetime.now()
    day = 6  # now.weekday()
    month = now.month

    hashtags = '#drawingprompt'

    # special months
    # # May is Mermay
    if month == 5:
        from prompts.mermay import get_prompt
        prompt = get_prompt()
        hashtags += ' #mermay'

    # # October is Spooktober
    elif month == 10:
        from prompts.spooktober import get_prompt
        prompt = get_prompt()
        hashtags += ' #spooktober'

    # Saturdays are illustration days
    elif day == 5:
        prompt = illustration[randint(0, (len(illustration)-1))]
        hashtags += ' #illustration'

    # Sundays are character design
    elif day == 6:
        from prompts.characterGenerator import get_prompt
        prompt = get_prompt()
        hashtags += ' #characterdesign'
    else:
        prompt = weekday()

    tweet = '++ DAILY DRAWING PROMPT {:%Y%m%d}: {} ++\n{}'.format(now, prompt.upper(), hashtags)

    try:

        print tweet
        # api.update_status(status=tweet)

    except tweepy.TweepError as e:
        print (e.reason)


if __name__ == '__main__':
    post_tweet()
