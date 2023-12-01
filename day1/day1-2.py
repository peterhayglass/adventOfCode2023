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
digit_str_len = list(set(len(key) for key in digit_map))

with open("day1/input.txt") as in_file:
    sum = 0
    for line in in_file:
        digits: list[int] =  []
        for i, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
                continue
            #else:
            for length in digit_str_len:
                if line[i:i+length] in digit_map:
                    digits.append(
                        digit_map[line[i:i+length]]
                    )
                    break
        line_val = f"{digits[0]}{digits[-1]}"
        sum += int(line_val)               
    print(sum)