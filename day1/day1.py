with open("day1/input.txt") as in_file:
    sum = 0
    for line in in_file:
        numbers = [char for char in line if char.isdigit()]
        line_val = f"{numbers[0]}{numbers[-1]}"
        sum += int(line_val)
    print(sum)