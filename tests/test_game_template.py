import pytest
from madlib_cli.madlib import read_template, parse_template, merge

def make_video_game():
    story_template = "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}! What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."

    # Parse the template and get the parts
    stripped_template, parts = parse_template(story_template)

    # Prompt the user for words to fill in the parts
    words = {}
    for part in parts:
        words[part] = input(f"Enter a {part}: ")

    # Merge the words with the template
    story = merge(stripped_template, tuple(words.values()))

    return story

def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")
    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected

def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
