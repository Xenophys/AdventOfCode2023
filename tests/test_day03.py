from modules.utils import readfile
from modules.day03 import extract_marked_numbers, part01, extract_gear_ratios, part02
import os

script_path = os.path.dirname(__file__)
resources_path = os.path.join(os.path.split(script_path)[0], "resources")
expected_numbers = [467, 35, 633, 617, 592, 755, 664, 598]


def test_extract_marked_numbers():
    lines = readfile(os.path.join(resources_path, "test-input_day03.txt"))
    numbers = extract_marked_numbers(lines)
    assert numbers == expected_numbers


def test_part01():
    result = part01(os.path.join(resources_path, "test-input_day03.txt"))
    assert result == 4361


def test_extract_numbers_with_star():
    lines = readfile(os.path.join(resources_path, "test-input_day03.txt"))
    result = extract_gear_ratios(lines)
    assert result == [16345,451490]


def test_part02():
    result = part02(os.path.join(resources_path, "test-input_day03.txt"))
    assert result == 467835
