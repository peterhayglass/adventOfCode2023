from time import perf_counter
from typing import Dict, Sequence


digit_map = {
    "one": 1, 
    "two": 2, 
    "three": 3, 
    "four": 4,
    "five": 5,
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9
}
reversed_digit_map = {key[::-1]: value for key, value in digit_map.items()}
digit_str_len = list(set(len(key) for key in digit_map))


def get_first_digit(line: Sequence[str], digit_map: Dict[str, int]) -> int:
    """Find the first digit in a string or list of chars,
    either in numerical form or spelled out,
    and return it as an int."""
    for i, char in enumerate(line):
        if char.isdigit():
            return int(char)
        for length in digit_str_len:
            slice = ''.join(line[i:i+length])
            if slice in digit_map:
                return digit_map[slice]
    return 0


def main() -> None:
    start = perf_counter()

    with open("day1/input.txt") as in_file:
        sum = 0
        for line in in_file:
            first = get_first_digit(line, digit_map)
            
            reversed_line = list(reversed(line))
            second = get_first_digit(reversed_line, reversed_digit_map)

            line_val = first * 10 + second
            sum += int(line_val)               
        print(sum)

    end = perf_counter()
    run_time = (end - start) * 1000
    print(f"took {run_time}ms")


if __name__ == "__main__":
    main()