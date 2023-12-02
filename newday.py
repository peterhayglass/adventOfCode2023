import sys
import os
import shutil


def scaffold(day_number: int) -> None:
    try:
        day = int(day_number)
    except ValueError:
        print(f"Invalid input: {day_number}. must be an int day number")
        return

    day_dir = f"day{day}"
    os.makedirs(day_dir, exist_ok=True)

    with open(os.path.join(day_dir, "input.txt"), "w") as input_file:
        pass

    try:
        shutil.copy2("template.py", os.path.join(day_dir, "main.py"))
    except FileNotFoundError:
        print("could not find template.py")
        shutil.rmtree(day_dir)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python newday.py [day_number]")
    else:
        scaffold(int(sys.argv[1]))