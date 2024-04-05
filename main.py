import re, os
from collections import Counter


def clean_text(text: str):
    """
    Cleans the text from punctuation marks except spaces.

    Parameters:
    text (str): The input text to be cleaned.

    Returns:
    str: The cleaned text.
    """
    cleaned_text = re.sub(r'[^\w\s]', ' ', text).lower()
    return cleaned_text


def read_text(filename: str):
    """
    Reads the content of the file with the specified filename.

    Parameters:
    filename (str): The path to the file to be read.

    Returns:
    str: The content of the file as a string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


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
