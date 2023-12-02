import os
from io import TextIOWrapper
from time import perf_counter


CODE_DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(CODE_DIR, 'input.txt')


def part1(input: TextIOWrapper) -> None:
    return


def part2(input: TextIOWrapper) -> None:
    return


def main():
    with open(IN_PATH) as in_file:
        start_p1 = perf_counter()
        part1(in_file)
        p1_run_time = (perf_counter() - start_p1) * 1000
        print(f"Part 1 took {p1_run_time:.4f}ms")

        start_p2 = perf_counter()
        part2(in_file)
        p2_run_time = (perf_counter() - start_p2) * 1000
        print(f"Part 2 took {p2_run_time:.4f}ms")       


if __name__ == "__main__":
    start = perf_counter()
    main()
    run_time = (perf_counter() - start) * 1000
    print(f"took {run_time:.4f}ms total")