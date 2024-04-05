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


def find_top_words(text: str, n=10):
    """
    Finds the top N most common words in the text.

    Parameters:
    text (str): The input text to analyze.
    n (int): The number of top words to find. Default is 10.

    Returns:
    list: A list of tuples containing the top words and their frequencies.
    """
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    word_counts = Counter(words)
    top_words = word_counts.most_common(n)
    return top_words


def write_to_file(top_words: str, output_filename: str):
    """
    Writes the top words and their frequencies to a file.

    Parameters:
    top_words (list): A list of tuples containing the top words and their frequencies.
    output_filename (str): The path to the output file.

    Returns:
    None
    """
    with open(output_filename, 'w', encoding='utf-8') as file:
        for word, count in top_words:
            file.write(f"{word}-{count}\n")


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


def main():
    """
    Reads the input file, finds the top words, writes the result to the output file, and prints a message.

    Returns:
    None
    """
    input_filename = get_input_filename()
    output_filename = get_output_filename()
    
    text = read_text(input_filename)
    top_words = find_top_words(text)
    write_to_file(top_words, output_filename)
    
    print(f"Top words saved to {output_filename}")


if __name__ == '__main__':
    main()
