from typing import Any, List, Tuple

import numpy as np

from planes.cards import Card
from planes.symbols import Symbol


class Projective:
    """
    A class to hold the functions for generating a projective plane
    """

    def __init__(self, order: int) -> None:
        self.order = order
        # the width of the affine plane cards square
        self.width = order - 1

        # count of cards and symbols
        self.count = order ** 2 - order + 1

        # create affine plane cards in square of size width
        cards = [Card() for i in range(self.width ** 2)]
        self.affine_plane_cards = np.array(cards, object).reshape(
            self.width, self.width
        )

        # initialise a set of symbols with unique ids
        self.symbols = [Symbol(id=i) for i in range(self.count)]

        # create lists of coords for top row and left column
        self.left_col = [np.array((0, i), int) for i in range(self.width)]
        self.top_row = [np.array((i, 0), int) for i in range(self.width)]

    def project(self):
        """
        entry point for generating the projective plane
        """
        self.associate()
        all_cards = self.add_infinite_incidences()

        self.show_cards(all_cards)
        self.verify(all_cards)

    def associate(self):
        """
        generate the patterns for the lines to pass through the square
        arrangement of cards. The pattern represents the xstep, ystep to perform
        to find the next point in each line. Each line starts at all of the
        cards in the top row (or left column)
        """
        patterns: List[Tuple[int, int]] = [(1, 0)]
        for patnum in range(self.width):
            patterns.append((patnum, 1))

        symbol_num = 0
        for pattern in patterns:
            self.add_symbol(pattern, self.symbols[symbol_num : symbol_num + self.width])
            symbol_num += self.width

    def add_symbol(self, pattern: Tuple[int, int], symbols: List[Symbol]):
        """
        add a symbol to all cards in the affine grid by following a path described by
        pattern from each starting point along the top row (or left column).
        Each starting point and path gets a symbol, thus this function needs a
        list of symbols to apply of length width
        """
        _, ystep = pattern
        start_points = self.left_col if ystep == 0 else self.top_row

        for line, start in enumerate(start_points):
            point = start
            # each line is width long and may wrap around the edges of the
            # square
            for step in range(self.width):
                self.affine_plane_cards[tuple(point)].symbols.append(symbols[line])
                # use pattern to move on to the next point in the line
                # with modulus providing a wrap around
                point = (point + pattern) % (self.width)

    def add_infinite_incidences(self) -> Any:
        """
        The affine_plane cards reperesent the incendences in finite space. There are
        additional cards of number <order> to add. These represent the incidences at
        infinity and there is also one more symbol to add to each of these
        """
        all_cards = self.affine_plane_cards.flatten()

        for i in range(self.order):
            these_symbols = self.symbols[i * (self.width) : (i + 1) * (self.width)] + [
                self.symbols[-1]
            ]
            next_card = Card(symbols=these_symbols)

            all_cards = np.append(all_cards, next_card)

        return all_cards

    def show_cards(self, cards):
        """
        ouput a representation of the card deck
        """
        print("\nCARD SUMMARY")
        for card in cards.flatten():
            print(f"card {card.id} symbols: {card.symbols}")

    def verify(self, cards: np.ndarray):
        """
        verify that every card matches a symbol with each other card
        exactly once
        """
        result = True
        for card in cards.flatten():
            for match_card in cards.flatten():
                if match_card.id == card.id:
                    continue
                matches = []
                for symbol in card.symbols:
                    if symbol in match_card.symbols:
                        matches.append(symbol)
                if len(matches) != 1:
                    print(
                        f"ERROR: cards {card.id} and {match_card.id} share symbols "
                        f"{[m.id for m in matches]}"
                    )
                    result = False
        return result
