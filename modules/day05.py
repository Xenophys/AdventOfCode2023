import os

from modules.utils import readfile

script_path = os.path.dirname(__file__)
resources_path = os.path.join(os.path.split(script_path)[0], "resources")


def parse_almanac(lines: list[str]):
    pass


def part01(path_to_file: str):
    lines = readfile(path_to_file)
    return 0


def part02(path_to_file: str):
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part01_result = part01(os.path.join(resources_path, "input_day05.txt"))
    print(f"Result of part 1: '{str(part01_result)}'")
    part02_result = part02(os.path.join(resources_path, "input_day05.txt"))
    print(f"Result of part 2: '{str(part02_result)}'")