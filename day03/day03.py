from utils.utils import readfile


def is_marker(char: str) -> bool:
    return char != "." and not char.isnumeric()


def number_has_marker(row_index: int, col_index: int, lines: list[str]):
    for row in range(max(0, row_index - 1), min(row_index + 2, len(lines))):
        line = lines[row]
        for column in range(max(0, col_index - 1), min(col_index + 2, len(line))):
            if is_marker(line[column]):
                return True
    return False


def extract_marked_numbers(lines: list[str]):
    numbers: list[int] = []
    actual_number = 0
    keep_number = False
    for line_index in range(0, len(lines)):
        line = lines[line_index]
        for column_index in range(0, len(line)):
            actual_char = str(line[column_index])
            if actual_char.isnumeric():
                actual_number = actual_number * 10 + int(line[column_index])
                if not keep_number:
                    keep_number = number_has_marker(line_index, column_index, lines)
            elif is_marker(actual_char):
                if actual_number > 0:
                    numbers.append(actual_number)
                actual_number = 0
                keep_number = False
            else:
                if keep_number:
                    numbers.append(actual_number)
                actual_number = 0
                keep_number = False
        if actual_number > 0 and keep_number:
            numbers.append(actual_number)
        actual_number = 0
        keep_number = False
    return numbers


def check_and_add_number(lines, number: int, pos_x: int, pos_y:int, star_dict):
    positions = []
    for row in range(max(0, pos_y - 1), min(pos_y + 2, len(lines))):
        line = lines[row]
        for column in range(max(0, pos_x - len(str(number)) - 1), min(pos_x + 1, len(line))):
            if line[column] == "*":
                position = f"{column},{row}"
                positions.append(position)
    if len(positions) > 0:
        for position in positions:
            num_list = star_dict[position] if star_dict.get(position) else []
            num_list.append(number)
            star_dict[position] = num_list
    return star_dict


def extract_gear_ratios(lines: list[str]):
    gears = {}
    actual_number = 0
    for line_index in range(0, len(lines)):
        line = lines[line_index]
        for column_index in range(0, len(line)):
            actual_char = str(line[column_index])
            if actual_char.isnumeric():
                actual_number = actual_number * 10 + int(line[column_index])
            else:
                if actual_number > 0:
                    gears = check_and_add_number(lines, actual_number, column_index, line_index, gears)
                actual_number = 0
        if actual_number > 0:
            gears = check_and_add_number(lines, actual_number, len(line), line_index, gears)
        actual_number = 0
    gear_ratios = []
    for key in gears:
        numbers = gears.get(key)
        if len(numbers) == 2:
            gear_ratios.append(numbers[0] * numbers[1])
    return gear_ratios


def part01(input_file_name: str):
    lines = readfile(input_file_name)
    numbers = extract_marked_numbers(lines)
    return sum(numbers)


def part02(input_file_name: str):
    lines = readfile(input_file_name)
    gear_ratios = extract_gear_ratios(lines)
    return sum(gear_ratios)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part01_result = part01("input_day03.txt")
    print(f"Result of part 1: '{str(part01_result)}'")
    part02_result = part02("input_day03.txt")
    print(f"Result of part 2: '{str(part02_result)}'")
