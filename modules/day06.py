import os
import re

from modules.utils import readfile

script_path = os.path.dirname(__file__)
resources_path = os.path.join(os.path.split(script_path)[0], "resources")


class BoatRace:

    def __init__(self, time: int, distance: int):
        self.time = time
        self.distance = distance

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.time == other.time and self.distance == other.distance

    def get_winning_options(self, boat_speed_per_ms: int):
        winning_options = []
        for charging_time in range(0, self.time + 1):
            driving_time = self.time - charging_time
            driving_speed = charging_time * boat_speed_per_ms
            driving_distance = driving_speed * driving_time
            if driving_distance > self.distance:
                winning_options.append(charging_time)
        return winning_options


def parse_boat_races(lines: list[str]):
    numbers_regex = re.compile('\\d+')
    times = numbers_regex.findall(lines[0])
    distances = numbers_regex.findall(lines[1])
    return [BoatRace(int(times[index]), int(distances[index])) for index in range(0, len(times))]


def parse_boat_race(lines: list[str]):
    numbers_regex = re.compile('\\d+')
    times = numbers_regex.findall(lines[0].replace(" ", ""))
    distances = numbers_regex.findall(lines[1].replace(" ", ""))
    return BoatRace(int(times[0]), int(distances[0]))


def part01(path_to_file: str):
    lines = readfile(path_to_file)
    races = parse_boat_races(lines)
    options_product = 1
    for race in races:
        winning_options = race.get_winning_options(1)
        options_count = len(winning_options)
        options_product = options_product * options_count
    return options_product


def part02(path_to_file: str):
    lines = readfile(path_to_file)
    race = parse_boat_race(lines)
    winning_options = race.get_winning_options(1)
    return len(winning_options)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part01_result = part01(os.path.join(resources_path, "input_day06.txt"))
    print(f"Result of part 1: '{str(part01_result)}'")
    part02_result = part02(os.path.join(resources_path, "input_day06.txt"))
    print(f"Result of part 2: '{str(part02_result)}'")
