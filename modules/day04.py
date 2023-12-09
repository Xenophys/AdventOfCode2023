import math
import os

from modules.utils import readfile

script_path = os.path.dirname(__file__)
resources_path = os.path.join(os.path.split(script_path)[0], "resources")

def get_winning_card_numbers(line: str):
    winning_card_numbers = []
    all_numbers_string = line.split(":")[1].strip()
    split_number_string = [x.strip() for x in all_numbers_string.split("|")]
    winning_numbers = [int(x) for x in split_number_string[0].replace("  ", " ").split(" ")]
    card_numbers = [int(x) for x in split_number_string[1].replace("  ", " ").split(" ")]
    for number in card_numbers:
        if number in winning_numbers:
            winning_card_numbers.append(number)
    return winning_card_numbers


def part01 (file_path: str):
    lines = readfile(file_path)
    card_values = []
    for line in lines:
        winning_numbers = get_winning_card_numbers(line)
        if len(winning_numbers) > 0:
            card_values.append(int(math.pow(2, len(winning_numbers) - 1)))
    return sum(card_values)


def part02 (file_path: str):
    lines = readfile(file_path)
    winning_numbers_of_card = []
    card_counts = []
    for line in lines:
        winning_numbers = get_winning_card_numbers(line)
        winning_numbers_of_card.append(len(winning_numbers))
        card_counts.append(1)
    for index in range(0, len(winning_numbers_of_card)):
        count = winning_numbers_of_card[index]
        if count > 0:
            for card_index in range(index + 1, index + count + 1):
                old_count = card_counts[card_index]
                card_counts[card_index] = old_count + card_counts[index]
    return sum(card_counts)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part01_result = part01(os.path.join(resources_path, "input_day04.txt"))
    print(f"Result of part 1: '{str(part01_result)}'")
    part02_result = part02(os.path.join(resources_path, "input_day04.txt"))
    print(f"Result of part 2: '{str(part02_result)}'")
