import os
import libraries

from libraries.concepts.colours import get_colors

sketchbook_prompts = [
    'still life in {0} and {1}'.format(*get_colors(2))
]


def get_prompt():
    """
    Get a sketchbook prompt from weekday.txt
    :return: string
        A random sketchbook prompt
    """
    fn = os.path.join(os.path.dirname(__file__), 'weekday.txt')
    with open(fn, 'r') as f:
        for line in f:
            if line.startswith('#') or line.startswith('\n'):
                pass
            else:
                sketchbook_prompts.append(line.strip())

        return libraries.get_one(sketchbook_prompts)


if __name__ == '__main__':
    print get_prompt()