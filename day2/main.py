import os
from io import TextIOWrapper
from time import perf_counter
from collections import defaultdict


CODE_DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(CODE_DIR, 'input.txt')
LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_possible(totals: dict[str, list[int]]) -> bool:
    for colour in totals:
        for count in totals[colour]:
            if count > LIMITS[colour]:
                return False
    return True


def process_samples(samples_str: str) -> dict[str, list[int]]:
    samples = samples_str.split(';')
    totals = defaultdict(list)

    for sample in samples:
        for colour in sample.split(','):
            count, name = colour.strip().split(' ', 1)
            totals[name].append(int(count))
    
    return totals


def part1(input: TextIOWrapper) -> None:
    valid_game_ids: list[int] = []

    for line in input:
        game_id_str, samples_str = line.strip().split(':')
        game_id = int(game_id_str.split(' ')[-1])
        totals = process_samples(samples_str)

        if is_possible(totals):
            valid_game_ids.append(game_id)

    print(f"part 1 solution: {sum(valid_game_ids)}")


def part2(input: TextIOWrapper) -> None:
    total_power = 0

    for line in input:
        _, samples_str = line.strip().split(':')
        totals = process_samples(samples_str)

        requirements = [max(counts) for counts in totals.values()]
        power = 1
        for req in requirements:
            power *= req

        total_power += power

    print(f"Part 2: {total_power}")


def main() -> None:
    with open(IN_PATH) as in_file:       
        start_p1 = perf_counter()
        part1(in_file)
        p1_run_time = (perf_counter() - start_p1) * 1000
        print(f"Part 1 took {p1_run_time:.4f}ms")
    
    with open(IN_PATH) as in_file:
        start_p2 = perf_counter()
        part2(in_file)
        p2_run_time = (perf_counter() - start_p2) * 1000
        print(f"Part 2 took {p2_run_time:.4f}ms")       


if __name__ == "__main__":
    start = perf_counter()
    main()
    run_time = (perf_counter() - start) * 1000
    print(f"took {run_time:.4f}ms total")