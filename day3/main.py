import os
import re
from io import TextIOWrapper
from time import perf_counter
from dataclasses import dataclass
from collections import defaultdict
from typing import Optional


CODE_DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(CODE_DIR, 'input.txt')


@dataclass(frozen=True)
class Coord():
    x: int
    y: int


@dataclass(frozen=True)
class Node(Coord):
    val: str


def get_neighbours(start: Coord, end: Coord) -> list[Coord]:
    """Finds all 8-connected neighbours surrounding the region bounded
    by the start and end coords
    """
    return [Coord(x, y) for x in range(start.x - 1, end.x + 2)
                        for y in range(start.y - 1, end.y + 2)
                        if (x < start.x or x > end.x or y < start.y or y > end.y)]


def get_adjacent_symbol(neighbours: list[Coord], 
                        line: str, 
                        input_text: list[str]
                        ) -> Optional[Node]:
    """Check a given set of neighbours coords, find any adjacent symbol. 
    If found, return the symbol. otherwise return None    
    
    Args:
        neighbours: list of coordinates for all the neighbour cells surrounding the potential part number
        line: the current line of input data
        input_text: the full 2d input data

    Returns:
        a Node including the coords and value of the symbol that was found, if any
        otherwise returns None
    """
    for n in neighbours:
        if n.x < 0 or (n.x + 1 >= len(input_text)):
            continue
        if n.y < 0 or (n.y + 1 >= len(line)):
            continue
        n_val = input_text[n.x][n.y]
        if (not n_val.isdigit() and n_val != '.'):
            return Node(n.x, n.y, n_val)
    return None


def find_symbols(input_text: list[str]) -> list[tuple[int, Node]]:
    """Find symbols that are adjacent to a number
    
    Args: 
        input_text: the full 2d input data 

    Returns: 
        list of tuples consisting of:
        (the value of the number that the symbol was found adjacent to,
        a Node entity representing the coords and value of the found symbol)
    """
    adjacent_symbols = []
    for x, line in enumerate(input_text):
        num_matches = list(re.finditer(r'\d+', line))

        for match in num_matches:
            num_start = match.start()
            num_end = match.end() - 1

            ne = get_neighbours(Coord(x, num_start), Coord(x, num_end))
            symbol = get_adjacent_symbol(ne, line, input_text)

            if symbol:
                adjacent_symbols.append((int(match.group()), symbol))

    return adjacent_symbols


def part1(input_text: list[str]) -> None:
    """Solve part 1, find sum of all valid part numbers"""
    adjacent_symbols = find_symbols(input_text)
    print(f"Part 1: {sum(num for num, _ in adjacent_symbols)}")


def part2(input_text: list[str]) -> None:
    """Solve part 2, find sum of all valid gear parts"""
    adjacent_symbols = find_symbols(input_text)
    gear_vals: dict[Coord, list[int]] = defaultdict(list)

    for num, symbol in adjacent_symbols:
        if symbol.val == '*':
            gear_vals[Coord(symbol.x, symbol.y)].append(num)

    gears_sum = sum(x[0] * x[1] 
                 for x in gear_vals.values() 
                 if len(x) == 2)
    
    print(f"Part 2: {gears_sum}")



def main() -> None:
    with open(IN_PATH) as in_file:
        input_text = [line.strip() for line in in_file]

        start_p1 = perf_counter()
        part1(input_text)
        p1_run_time = (perf_counter() - start_p1) * 1000
        print(f"Part 1 took {p1_run_time:.4f}ms")
    
        in_file.seek(0)
        
        start_p2 = perf_counter()
        part2(input_text)
        p2_run_time = (perf_counter() - start_p2) * 1000
        print(f"Part 2 took {p2_run_time:.4f}ms")        


if __name__ == "__main__":
    start = perf_counter()
    main()
    run_time = (perf_counter() - start) * 1000
    print(f"took {run_time:.4f}ms total")