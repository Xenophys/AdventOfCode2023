# Day02
from src.utils import readfile


class CubeSet:
    def __init__(self, blue=0, green=0, red=0):
        self.blue = blue
        self.green = green
        self.red = red

    def set_cubes(self, count, color):
        number = int(count)
        match color:
            case "blue":
                self.blue = number
            case "green":
                self.green = number
            case "red":
                self.red = number

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            print("CubeSet type mismatch")
            return False
        if self.blue != other.blue:
            print(f"blue mismatch: {str(self.blue)} vs {str(other.blue)}")
            return False
        if self.green != other.green:
            print(f"green mismatch: {str(self.green)} vs {str(other.green)}")
            return False
        if self.red != other.red:
            print(f"red mismatch: {str(self.red)} vs {str(other.red)}")
            return False
        return True


class Game:
    def __init__(self, game_number: int):
        self.game_number = game_number
        self.cube_sets = []

    def add_cube_set(self, cube_set: CubeSet):
        self.cube_sets.append(cube_set)

    def is_possible(self, check_cube_set: CubeSet) -> bool:
        for cube_set in self.cube_sets:
            if cube_set.blue > check_cube_set.blue:
                return False
            if cube_set.green > check_cube_set.green:
                return False
            if cube_set.red > check_cube_set.red:
                return False
        return True

    def get_power(self):
        required_blue = 0
        required_green = 0
        required_red = 0
        for cube_set in self.cube_sets:
            if cube_set.blue > required_blue:
                required_blue = cube_set.blue
            if cube_set.green > required_green:
                required_green = cube_set.green
            if cube_set.red > required_red:
                required_red = cube_set.red
        return required_blue * required_green * required_red

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            print("Type mismatch")
            return False
        if not self.game_number == other.game_number:
            print("Game number mismatch")
            return False
        if len(self.cube_sets) != len(other.cube_sets):
            print(f"CubeSet length mismatch {str(len(self.cube_sets))} vs. {str(len(other.cube_sets))}")
            return False
        for index in range(0, len(self.cube_sets)):
            if self.cube_sets[index] != other.cube_sets[index]:
                print(f"CubeSet mismatch {str(self.cube_sets[index])} vs. {str(other.cube_sets[index])}")
                return False
        return True


def parse_game(line: str) -> Game:
    split_line = line.split(":")
    game_number = int(split_line[0].split(" ")[1])
    game = Game(game_number)
    for cube_set_string in split_line[1].split(";"):
        cube_set = CubeSet()
        for cubes in cube_set_string.split(","):
            split_cubes = cubes.strip().split(" ")
            cube_set.set_cubes(split_cubes[0], split_cubes[1])
        game.add_cube_set(cube_set)
    return game


def part01(input_file_name: str, cubes_to_check: CubeSet):
    lines = readfile(input_file_name)
    possible_game_numbers = []
    for line in lines:
        game = parse_game(line)
        if game.is_possible(cubes_to_check):
            possible_game_numbers.append(game.game_number)
    return sum(possible_game_numbers)


def part02(input_file_name: str):
    lines = readfile(input_file_name)
    game_powers = []
    for line in lines:
        game = parse_game(line)
        game_powers.append(game.get_power())
    return sum(game_powers)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part1_result = part01("resources/input_day02.txt", CubeSet(red=12, green=13, blue=14))
    print(f"Result of part 1: '{str(part1_result)}'")
    part2_result = part02("resources/input_day02.txt")
    print(f"Result of part 2: '{str(part2_result)}'")
