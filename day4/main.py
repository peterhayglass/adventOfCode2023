import os
from io import TextIOWrapper
from time import perf_counter
from dataclasses import dataclass


CODE_DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(CODE_DIR, 'input.txt')


def part1(input: TextIOWrapper) -> None:
    total_score = 0
    for line in input:
        w, h = line.split('|')
        _, winners_str = w.split(':')
        have = [int(char) for char in h.split()]
        winners = [int(char) for char in winners_str.split()]
        score = 0
        for num in have:
            if num not in winners:
                continue
            if score == 0:
                score = 1
            else:
                score *= 2
        total_score += score

    print(f"Part 1: {total_score}")
        

@dataclass
class Game():
    count: int
    line: str


def part2(input: TextIOWrapper) -> None:
    games = [Game(1, line) for line in input]
    count = len(games)
    extras_count = 0
    
    for game_num, game in enumerate(games, start=1):
        line = game.line
        w, h = line.split('|')
        _, winners_str = w.split(':')
        have = [int(char) for char in h.split()]
        winners = [int(char) for char in winners_str.split()]
        matches = sum(num in winners for num in have)

        for k in range(matches):
            if game_num + k < len(games):
                games[game_num + k].count += game.count
                extras_count += game.count

    print(f"Part 2: {count+extras_count}")


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