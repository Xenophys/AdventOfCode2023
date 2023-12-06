# Day01
from src.utils import readfile

number_strings = dict(one="1", two="2", three="3", four="4", five="5", six="6", seven="7", eight="8", nine="9")


def get_number_from_line(input_line):
    numbers = []
    for x in input_line:
        if x.isnumeric():
            numbers.append(int(x))
    return int(numbers[0]) * 10 + int(numbers[-1])


def get_number(input_line, last=False):
    line = str(input_line)
    found_index = -1 if last else 999
    number = None
    for i in range(1, 10):
        if last:
            index = line.rfind(str(i))
            if 0 <= index > found_index:
                found_index = index
                number = str(i)
        else:
            index = line.find(str(i))
            if 0 <= index < found_index:
                found_index = index
                number = str(i)
    for num in number_strings.keys():
        if last:
            index = line.rfind(str(num))
            if 0 <= index > found_index:
                found_index = index
                number = number_strings[num]
        else:
            index = line.find(str(num))
            if 0 <= index < found_index:
                found_index = index
                number = number_strings[num]
    return number


def get_alphanumeric_number_from_line(input_line):
    first_number = int(get_number(input_line))
    last_number = int(get_number(input_line, True))
    number = 10 * first_number + last_number
    return number


def day01_part01(input_file_name):
    lines = readfile(input_file_name)
    line_numbers = []
    for line in lines:
        line_number = get_number_from_line(line)
        line_numbers.append(line_number)
    result = sum(line_numbers)
    return result


def day01_part02(input_file_name):
    lines = readfile(input_file_name)
    line_numbers = []
    for line in lines:
        line_number = get_alphanumeric_number_from_line(line)
        line_numbers.append(line_number)
    assert len(lines) == len(line_numbers)
    result = sum(line_numbers)
    return result


