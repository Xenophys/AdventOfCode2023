from modules.day01 import day01_part01, day01_part02
from modules.day01 import get_number_from_line, get_alphanumeric_number_from_line
from modules.utils import readfile
import os

script_path = os.path.dirname(__file__)
resources_path = os.path.join(os.path.split(script_path)[0], "resources")

def test_day01_part01():
    lines = readfile(os.path.join(resources_path, "test-input_day01-01.txt"))
    expected_line_results = [12, 38, 15, 77]
    for count in range(0, len(lines)):
        assert get_number_from_line(lines[count]) == expected_line_results[count]
    assert day01_part01(os.path.join(resources_path, "test-input_day01-01.txt")) == 142


def test_day01_part02():
    lines = readfile(os.path.join(resources_path, "test-input_day01-02.txt"))
    expected_line_results = [29, 83, 13, 24, 42, 14, 76]
    for count in range(0, len(lines)):
        result = get_alphanumeric_number_from_line(lines[count])
        assert result == expected_line_results[count]
    assert day01_part02(os.path.join(resources_path, "test-input_day01-02.txt")) == 281


def test_number_extract():
    lines = ["cbcvd9", "five11eight1"]
    expected_line_results = [99, 51]
    for count in range(0, len(lines)):
        result = get_alphanumeric_number_from_line(lines[count])
        assert result == expected_line_results[count]
