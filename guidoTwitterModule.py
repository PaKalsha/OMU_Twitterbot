import tweepy

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
# Modifiers
####

object_adjectives = [
    'delicate', 'knotted', 'polished', 'reflective', 'rusted', 'shattered', 'tangled', 'embroidered', 'folded'
]

materials = [
    'metal', 'wooden'
]


def generate_tweet():
    """
    Construct and post tweet based on month and day.
    """
    now = datetime.now()
    day = now.weekday()
    month = now.month

    hashtags = '#drawingprompt'

    # special months
    # # May is Mermay
    if month == 5:
        from prompts.mermay import Mermay
        module = Mermay()
        prompt = module.get_prompt()
        hashtags += ' #mermay'

    # # October is Spooktober
    elif month == 10:
        from prompts.spooktober import Spooktober
        module = Spooktober()
        prompt = module.get_prompt()
        hashtags += ' #spooktober'

    # Saturdays are illustration days
    elif day == 5:
        from prompts.illustration import get_prompt
        prompt = get_prompt()
        hashtags += ' #illustration'

    # Sundays are character design
    elif day == 6:
        from prompts.characterGenerator import CharacterGenerator
        module = CharacterGenerator()
        prompt = module.get_prompt()
        hashtags += ' #characterdesign'
    else:
        from prompts.sketchbook import get_prompt
        prompt = get_prompt()

    tweet = '++ DAILY DRAWING PROMPT {:%Y%m%d}: {} ++\n{}'.format(now, prompt.upper(), hashtags)
    return tweet


def post_tweet(tweet):
    try:

        api.update_status(status=tweet)

    except tweepy.TweepError as e:
        print (e.reason)


if __name__ == '__main__':
    tweet = generate_tweet()
    print tweet
    post_tweet(tweet)
