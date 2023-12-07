import os
from io import TextIOWrapper
from time import perf_counter
from dataclasses import dataclass
from functools import cached_property


CODE_DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(CODE_DIR, 'input.txt')


CARD_POWER = {
    card: power for power, card in 
    enumerate(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']), 1)
}

CARD_POWER_2 = {
    card: power for power, card in 
    enumerate(reversed(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']), 1)
}


@dataclass(frozen=True)
class Hand():
    counts: dict[str, int]
    bid: int
    cards: str
    
    @cached_property
    def power(self) -> list[int]:
        return sorted([count for count in self.counts.values()], reverse=True)
    
    @cached_property
    def tiebreaker(self) -> list[int]:
        return [CARD_POWER[card] for card in self.cards]
    
    @cached_property
    def power2(self) -> list[int]:
        if self.cards == 'JJJJJ':
            return [5]
        power_counts = sorted(
                [count for card, count in self.counts.items() if card != 'J'], 
                reverse=True
             )
        if 'J' in self.cards:
            Jcount = self.cards.count('J')
            power_counts[0] += Jcount
        return power_counts
    
    @cached_property
    def tiebreaker2(self) -> list[int]:
        return [CARD_POWER_2[card] for card in self.cards]
        

def part1(input: TextIOWrapper) -> None:
    lines = [line for line in input]
    hands: list[Hand] = []
    
    for line in lines:
        hand_str, bid_str = line.split()
        hands.append(
            Hand(
                cards = hand_str,
                counts = {char: hand_str.count(char) for char in set(hand_str)},
                bid = int(bid_str)
            )
        )

    sorted_hands = sorted(hands, key=lambda hand: (hand.power, hand.tiebreaker))
    winnings = 0

    for rank, hand in enumerate(sorted_hands, start=1):
        winnings += rank * hand.bid
    
    print(f"part 1: {winnings}")
  

def part2(input: TextIOWrapper) -> None:
    lines = [line for line in input]
    hands: list[Hand] = []

    for line in lines:
        hand_str, bid_str = line.split()
        hands.append(
            Hand(
                cards = hand_str,
                counts = {char: hand_str.count(char) for char in set(hand_str)},
                bid = int(bid_str)
            )
        )
    sorted_hands = sorted(hands, key=lambda hand: (hand.power2, hand.tiebreaker2))
    winnings = 0

    for rank, hand in enumerate(sorted_hands, start=1):
        winnings += rank * hand.bid
    print(f"part 2: {winnings}")


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