import os

from modules.day04 import get_winning_card_numbers, part01, part02
from modules.utils import readfile

script_path = os.path.dirname(__file__)
resources_path = os.path.join(os.path.split(script_path)[0], "resources")

expected_winning_numbers = [[83, 86, 17, 48], [61, 32], [21, 1], [84], [], []]


def test_get_winning_card_numbers():
    lines = readfile(os.path.join(resources_path, "test-input_day04.txt"))
    for index in range(0, len(lines)):
        result = get_winning_card_numbers(lines[index])
        assert result == expected_winning_numbers[index]


def test_part01():
    result = part01(os.path.join(resources_path, "test-input_day04.txt"))
    assert result == 13


def test_part02():
    result = part02(os.path.join(resources_path, "test-input_day04.txt"))
    assert result == 30
