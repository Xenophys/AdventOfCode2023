from src.day01 import day01_part01, day01_part02
from src.day01 import get_number_from_line, get_alphanumeric_number_from_line
from src.utils import readfile


def test_day01_part01():
    input = readfile("resources/test-input_day01_01.txt")
    expected_line_results = [12, 38, 15, 77]
    for count in range(0, len(input)):
        assert get_number_from_line(input[count]) == expected_line_results[count]
    assert day01_part01("resources/test-input_day01_01.txt") == 142


def test_day01_part02():
    input = readfile("resources/test-input_day01_02.txt")
    expected_line_results = [29, 83, 13, 24, 42, 14, 76]
    for count in range(0, len(input)):
        result = get_alphanumeric_number_from_line(input[count])
        assert result == expected_line_results[count]
    assert day01_part02("resources/test-input_day01_02.txt") == 281

def test_number_extract():
    input = ["cbcvd9", "five11eight1"]
    expected_line_results = [99, 51]
    for count in range(0, len(input)):
        result = get_alphanumeric_number_from_line(input[count])
        assert result == expected_line_results[count]
