from time import perf_counter


start = perf_counter()

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
reversed_digit_map = {
    "eno": 1, 
    "owt": 2, 
    "eerht": 3, 
    "ruof": 4,
    "evif": 5,
    "xis": 6, 
    "neves": 7, 
    "thgie": 8,
    "enin": 9
}
digit_str_len = list(set(len(key) for key in digit_map))

with open("day1/input.txt") as in_file:
    sum = 0
    for line in in_file:
        first = 0
        second = 0
        for i, char in enumerate(line):
            if char.isdigit():
                first = int(char)
                break
            #else:
            for length in digit_str_len:
                if line[i:i+length] in digit_map:
                    first = digit_map[line[i:i+length]]
                    break
            if first != 0:
                break
        
        rline = list(reversed(line))
        for i, char in enumerate(rline):
            if char.isdigit():
                second = int(char)
                break
            #else:
            for length in digit_str_len:
                if ''.join(rline[i:i+length]) in reversed_digit_map:
                    second = reversed_digit_map[''.join(rline[i:i+length])]
                    break
            if second != 0:
                break
            
        line_val = f"{first}{second}"
        sum += int(line_val)               
    print(sum)

end = perf_counter()
run_time = (end - start) * 1000
print(f"took {run_time}ms")