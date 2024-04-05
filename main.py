import re, os
from collections import Counter

def get_output_filename():
    """
    Returns the path to the input file.

    Returns:
    str: The path to the input file.
    """
    return os.path.join('results', 'top_words.txt')


def get_input_filename():
    """
    Повертає шлях до вхідного файлу.
    """
    return os.path.join('assets', 'data.txt')
