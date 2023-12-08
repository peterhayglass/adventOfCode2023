from __future__ import annotations
import os
from io import TextIOWrapper
from time import perf_counter
from dataclasses import dataclass


CODE_DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(CODE_DIR, 'input.txt')


@dataclass
class Node():
    name: str
    left: str
    right: str


def parse_nodes(lines: list[str]) -> dict[str, Node]:
    nodes: dict[str, Node] = {}
    for line in lines[2:]:
        name, links = line.split('=')
        left, right = links.split(',')
        name = name.strip()
        left = left.strip(' \n()')
        right = right.strip(' \n()')
        nodes[name] = Node(name, left, right)
    return nodes


def part1(input: TextIOWrapper) -> None:
    lines = [line for line in input]
    moves = lines[0].strip()
    nodes: dict[str, Node] = parse_nodes(lines)
    
    i = 0
    steps = 0
    cur = nodes['AAA']
    while i < len(moves):
        steps += 1
        if moves[i] == 'L':
            cur = nodes[cur.left]
            
        elif moves[i] == 'R':
            cur = nodes[cur.right]
            
        if cur.name == 'ZZZ':
            break

        if i == len(moves) - 1:
            i = 0
        else:
            i += 1
    
    print(f"part 1: {steps}")


def gcd(x: int, y: int) -> int:
    """Find greatest common divisor of two integers."""
    while True:
        r = x % y
        if not r:
            break
        x = y
        y = r
    return y


def lcm(x: int, y: int) -> int:
    """Find lowest common multiple of two integers."""
    return (
        (x * y) 
        //
        gcd(x, y)
    )


def part2(input: TextIOWrapper) -> None:
    lines = [line for line in input]
    moves = lines[0].strip()
    
    nodes: dict[str, Node] = parse_nodes(lines)
    
    node_ptrs: list[Node] = []
    for node in nodes.values():
        if node.name.endswith('A'):
            node_ptrs.append(node)

    stepcounts: list[int] = []
    for cur in node_ptrs:
            steps = 0    
            i = 0
            while i < len(moves):
                steps += 1
                if moves[i] == 'L':
                    cur = nodes[cur.left]
                    
                elif moves[i] == 'R':
                    cur = nodes[cur.right]
                    
                if cur.name.endswith('Z'):
                    break

                if i == len(moves) - 1:
                    i = 0
                else:
                    i += 1
            stepcounts.append(steps)
    
    _lcm = lcm(stepcounts[0], stepcounts[1])
    i = 2
    while i < len(stepcounts):
        _lcm = lcm(_lcm, stepcounts[i])
        i += 1
    
    print(f"part 2: {_lcm}")
    

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