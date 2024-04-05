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


