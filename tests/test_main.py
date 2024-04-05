import os
import pytest
from main import clean_text, read_text, find_top_words, write_to_file, get_output_filename, get_input_filename


@pytest.fixture
def sample_text():
    return "Hello Vlada. Sing songs. stay strong. Vlada. I live in Kyiv, Ukraine. Stay strong. Hello Harry. Vlada. Stay. stay here. stay."


@pytest.fixture
def sample_output_filename():
    return "test_top_words.txt"


@pytest.fixture
def expected_top_words():
    return [('hello', 2), ('i', 1), ('in', 1), ('kyiv', 1), ('live', 1), ('sing', 1), ('songs', 1), ('stay', 5), ('strong', 2), ('vlada', 3)]


def test_clean_text(sample_text):
    cleaned_text = clean_text(sample_text)
    assert cleaned_text == "hello vlada  sing songs  stay strong  vlada  i live in kyiv  ukraine  stay strong  hello harry  vlada  stay  stay here  stay "


def test_read_text(tmpdir, sample_text):
    file_path = os.path.join(tmpdir, "test_read_text.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(sample_text)

    read_text_content = read_text(file_path)
    assert read_text_content == sample_text


def test_find_top_words(sample_text, expected_top_words):
    top_words = find_top_words(sample_text)
    top_words = sorted(top_words, key=lambda x: x[0])
    expected_top_words = sorted(expected_top_words, key=lambda x: x[0])
    assert top_words == expected_top_words


