from src.day02 import part01, part02, CubeSet

# Press the green button in the gutter to run the script.
part1_result = part01("../src/resources/input_day02.txt", CubeSet(red=12, green=13, blue=14))
print(f"Result of part 1: '{str(part1_result)}'")
part2_result = part02("../src/resources/input_day02.txt")
print(f"Result of part 2: '{str(part2_result)}'")
