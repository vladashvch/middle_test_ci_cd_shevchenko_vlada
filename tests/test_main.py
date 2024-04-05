import os
import pytest
from main import clean_text, read_text, find_top_words, write_to_file, get_output_filename, get_input_filename


@pytest.fixture
def sample_text():
    return "Hello Vlada. Sing songs. stay strong. Vlada. I live in Kyiv, Ukraine. Stay strong. Hello Harry. Vlada. Stay. stay here. stay."


@pytest.fixture
def sample_output_filename():
    return "test_top_words.txt"

