from src.day02 import Game, CubeSet, parse_game, part01, part02
from src.utils import readfile


def build_expected_games():
    games = []
    game = Game(1)
    cube_set = CubeSet()
    cube_set.set_cubes("3", "blue")
    cube_set.set_cubes("4", "red")
    game.add_cube_set(cube_set)

    cube_set = CubeSet()
    cube_set.set_cubes("1", "red")
    cube_set.set_cubes("2", "green")
    cube_set.set_cubes("6", "blue")
    game.add_cube_set(cube_set)

    cube_set = CubeSet()
    cube_set.set_cubes("2", "green")
    game.add_cube_set(cube_set)
    games.append(game)

    game = Game(2)
    cube_set = CubeSet()
    cube_set.set_cubes("1", "blue")
    cube_set.set_cubes("2", "green")
    game.add_cube_set(cube_set)

    cube_set = CubeSet()
    cube_set.set_cubes("3", "green")
    cube_set.set_cubes("4", "blue")
    cube_set.set_cubes("1", "red")
    game.add_cube_set(cube_set)

    cube_set = CubeSet()
    cube_set.set_cubes("1", "green")
    cube_set.set_cubes("1", "blue")
    game.add_cube_set(cube_set)
    games.append(game)

    game = Game(3)
    cube_set = CubeSet()
    cube_set.set_cubes("8", "green")
    cube_set.set_cubes("6", "blue")
    cube_set.set_cubes("20", "red")
    game.add_cube_set(cube_set)

    cube_set = CubeSet()
    cube_set.set_cubes("5", "blue")
    cube_set.set_cubes("4", "red")
    cube_set.set_cubes("13", "green")
    game.add_cube_set(cube_set)

    cube_set = CubeSet()
    cube_set.set_cubes("5", "green")
    cube_set.set_cubes("1", "red")
    game.add_cube_set(cube_set)
    games.append(game)

    game = Game(4)
    cube_set = CubeSet()
    cube_set.set_cubes("1", "green")
    cube_set.set_cubes("3", "red")
    cube_set.set_cubes("6", "blue")
    game.add_cube_set(cube_set)

    cube_set = CubeSet()
    cube_set.set_cubes("3", "green")
    cube_set.set_cubes("6", "red")
    game.add_cube_set(cube_set)

    cube_set = CubeSet()
    cube_set.set_cubes("3", "green")
    cube_set.set_cubes("15", "blue")
    cube_set.set_cubes("14", "red")
    game.add_cube_set(cube_set)
    games.append(game)

    game = Game(5)
    cube_set = CubeSet()
    cube_set.set_cubes("6", "red")
    cube_set.set_cubes("1", "blue")
    cube_set.set_cubes("3", "green")
    game.add_cube_set(cube_set)

    cube_set = CubeSet()
    cube_set.set_cubes("2", "blue")
    cube_set.set_cubes("1", "red")
    cube_set.set_cubes("2", "green")
    game.add_cube_set(cube_set)

    games.append(game)
    return games


def test_parse_game():
    lines = readfile("tests/resources/test-input_day02_01.txt")
    expected = build_expected_games()
    for index in range(0, len(lines)):
        game = parse_game(lines[index])
        expected_game = expected[index]
        assert game == expected_game


def test_part01():
    test_cube_set = CubeSet(red=12, green=13, blue=14)
    solution = part01("tests/resources/test-input_day02_01.txt", test_cube_set)
    assert solution == 8


def test_part02():
    solution = part02("tests/resources/test-input_day02_01.txt")
    assert solution == 2286
