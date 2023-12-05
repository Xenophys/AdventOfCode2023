from src import utils

def is_marker(char:str)->bool:
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


def part01(input_file_name: str):
    lines = utils.readfile(input_file_name)
    numbers = extract_marked_numbers(lines)
    return sum(numbers)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part01_result = part01("resources/input_day03.txt")
    print(f"Result of part 1: '{str(part01_result)}'")
