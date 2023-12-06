from src.day03 import extract_marked_numbers, part01
from src.utils import readfile

expected_numbers = [467, 35, 633, 617, 592, 755, 664, 598]


def test_extract_marked_numbers():
    lines = readfile("tests/resources/test-input_day03.txt")
    numbers = extract_marked_numbers(lines)
    assert numbers == expected_numbers


def test_part01():
    result = part01("tests/resources/test-input_day03.txt")
    assert result == 4361
