from utils.utils import readfile
from .day03 import extract_marked_numbers, part01, extract_gear_ratios, part02

expected_numbers = [467, 35, 633, 617, 592, 755, 664, 598]


def test_extract_marked_numbers():
    lines = readfile("day03/test-input_day03.txt")
    numbers = extract_marked_numbers(lines)
    assert numbers == expected_numbers


def test_part01():
    result = part01("day03/test-input_day03.txt")
    assert result == 4361


def test_extract_numbers_with_star():
    lines = readfile("day03/test-input_day03.txt")
    result = extract_gear_ratios(lines)
    assert result == [16345,451490]


def test_part02():
    result = part02("day03/test-input_day03.txt")
    assert result == 467835
