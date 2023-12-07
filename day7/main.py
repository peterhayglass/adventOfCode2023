import os
from io import TextIOWrapper
from time import perf_counter
from dataclasses import dataclass
from functools import cached_property
from collections import deque


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
    def power(self) -> int:
        if len(self.counts) == 1:
            #5 of a kind
            return 7 
        if len(self.counts) == 2:
            if set(self.counts.values()) == set([4,1]):
                #4 of a kind
                return 6
            if set(self.counts.values()) == set([2,3]):
                #full house
                return 5
        if 3 in self.counts.values():
            #3 of a kind
            return 4
        if list(self.counts.values()).count(2) == 2:
            #two pair
            return 3
        if list(self.counts.values()).count(2) == 1:
            #one pair
            return 2
        #else high card
        return 1
    
    @cached_property
    def tiebreaker(self) -> list[int]:
        return [CARD_POWER[card] for card in self.cards]
        

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
        


@dataclass
class Hand2():
    counts: dict[str, int]
    bid: int
    cards: str
    
    def power(self, _counts: dict[str, int]) -> int:
        if len(_counts) == 1:
            #5 of a kind
            return 7 
        if len(_counts) == 2:
            if set(_counts.values()) == set([4,1]):
                #4 of a kind
                return 6
            if set(_counts.values()) == set([2,3]):
                #full house
                return 5
        if 3 in _counts.values():
            #3 of a kind
            return 4
        if list(_counts.values()).count(2) == 2:
            #two pair
            return 3
        if list(_counts.values()).count(2) == 1:
            #one pair
            return 2
        #else high card
        return 1
    

    @cached_property
    def Jpower(self) -> int:
        if 'J' not in self.cards:
            return self.power(self.counts)
        elif self.cards == 'JJJJJ':
            return 7
        else:
            _no_j_counts = self.counts.copy()
            _no_j_counts.pop('J')
            possible_counts = self.get_Jcounts(_no_j_counts, self.cards.count('J'))

            max_power = -1
            for count in possible_counts:
                max_power = max(max_power, self.power(count))

            return max_power


    def get_Jcounts(self, _counts: dict[str, int], Jcount: int) -> list[dict[str, int]]:
        queue = deque([(_counts, Jcount)])
        generated_counts = []

        while queue:
            cur_counts, remaining_J = queue.popleft()

            if remaining_J == 0:
                generated_counts.append(cur_counts)
            else:
                for key in cur_counts.keys():
                    if cur_counts[key] > 0:
                        new_counts = cur_counts.copy()
                        new_counts[key] += 1
                        queue.append((new_counts, remaining_J - 1))

        return generated_counts
    
    @cached_property
    def tiebreaker(self) -> list[int]:
        return [CARD_POWER_2[card] for card in self.cards]


def part2(input: TextIOWrapper) -> None:
    lines = [line for line in input]
    hands: list[Hand2] = []
    for line in lines:
        hand_str, bid_str = line.split()
        hands.append(
            Hand2(
                cards = hand_str,
                counts = {char: hand_str.count(char) for char in set(hand_str)},
                bid = int(bid_str)
            )
        )

    sorted_hands = sorted(hands, key=lambda hand: (hand.Jpower, hand.tiebreaker))
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