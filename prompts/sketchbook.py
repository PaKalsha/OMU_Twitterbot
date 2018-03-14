import os

from random import randint


def get_prompt():
    """
    Get a sketchbook prompt from weekday.txt
    :return: string
        A random sketchbook prompt
    """
    fn = os.path.join(os.path.dirname(__file__), 'weekday.txt')
    with open(fn, 'r') as f:
        prompt_dict = []
        for line in f:
            if line.startswith('#') or line.startswith('\n'):
                pass
            else:
                prompt_dict.append(line.strip())

        index_limit = len(prompt_dict) - 1

        return prompt_dict[randint(0, index_limit)]
