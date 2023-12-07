import os
from io import TextIOWrapper
from time import perf_counter
from math import ceil, sqrt


CODE_DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(CODE_DIR, 'input.txt')


def part1(input: TextIOWrapper) -> None:
    lines = input.readlines()
    _, times_str = lines[0].split(':')
    _, dists_str = lines[1].split(':')
    times = [int(n) for n in times_str.split()]
    dists = [int(n) for n in dists_str.split()]

    result = 1
    for time, target_dist in zip(times, dists):
        wins = 0
        for holdtime in range(1, time):
            speed = holdtime
            dist = speed * (time - holdtime)
            if dist > target_dist:
                wins += 1
        result *= wins

    print(f"part 1: {result}")


def part2(input: TextIOWrapper) -> None:
    lines = input.readlines()
    _, times_str = lines[0].split(':')
    _, dists_str = lines[1].split(':')
    times = [n for n in times_str.split()]
    dists = [n for n in dists_str.split()]
    realtime = int(''.join(times))
    realdist = int(''.join(dists))

    root1 = ceil((-realtime + sqrt(realtime**2 - 4 * (-1) * -realdist)) / (2 * (-1)))
    root2 = round((-realtime - sqrt(realtime**2 - 4 * (-1) * -realdist)) / (2 * (-1)))

    print(f"part 2: {(root2 - root1 + 1):d}")


def main() -> None:
    with open(IN_PATH) as in_file:       
        start_p1 = perf_counter()
        part1(in_file)
        p1_run_time = (perf_counter() - start_p1) * 1000
        print(f"Part 1 took {p1_run_time:.4f}ms")
    
        in_file.seek(0)
        
        start_p2 = perf_counter()
        part2(in_file)
        p2_run_time = (perf_counter() - start_p2) * 1000
        print(f"Part 2 took {p2_run_time:.4f}ms")        


if __name__ == "__main__":
    start = perf_counter()
    main()
    run_time = (perf_counter() - start) * 1000
    print(f"took {run_time:.4f}ms total")