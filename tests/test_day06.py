import os

from modules.day06 import BoatRace, parse_boat_races, part01, parse_boat_race, part02
from modules.utils import readfile

script_path = os.path.dirname(__file__)
resources_path = os.path.join(os.path.split(script_path)[0], "resources")


def test_parse_boat_races():
    lines = readfile(os.path.join(resources_path, "test-input_day06.txt"))
    expected_races = [BoatRace(7,9), BoatRace(15, 40), BoatRace(30,200)]
    parsed_races = parse_boat_races(lines)
    assert parsed_races == expected_races


def test_get_winning_options():
    lines = readfile(os.path.join(resources_path, "test-input_day06.txt"))
    expected_winning_options = [[2, 3, 4, 5], [4, 5, 6, 7, 8, 9, 10, 11], [11, 12, 13, 14, 15, 16, 17, 18, 19]]
    races = parse_boat_races(lines)
    for index in range(0, len(races)):
        winning_options = races[index].get_winning_options(1)
        assert winning_options == expected_winning_options[index]


def test_part01():
    result = part01(os.path.join(resources_path, "test-input_day06.txt"))
    assert result == 288


def test_parse_boat_race():
    lines = readfile(os.path.join(resources_path, "test-input_day06.txt"))
    expected_race = BoatRace(71530, 940200)
    parsed_race = parse_boat_race(lines)
    assert parsed_race == expected_race


def test_part02():
    result = part02(os.path.join(resources_path, "test-input_day06.txt"))
    assert result == 71503
