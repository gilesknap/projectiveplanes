from typing import List, Tuple

import numpy as np

from planes.cards import VCard
from planes.symbols import Symbol


def project(order: int):
    # count of cards and symbols
    count = order ** 2 - order + 1

    print("number of cards:", count)

    # layout most of the cards in square of order - 1
    affine_plane_cards = np.empty([order - 1, order - 1], object)
    # create an array of incrementing ids for the cards
    init_arry = np.arange(affine_plane_cards.size).reshape((order - 1, order - 1))

    # use the vectorized contructor to instantiate a VCard in each cell
    affine_plane_cards[:, :] = VCard(init_arry)

    symbols = [Symbol(id=i) for i in range(count)]

    associate(affine_plane_cards, symbols, order)
    add_infinite_incidences(affine_plane_cards, symbols, order)

    show_cards(affine_plane_cards)
    verify(affine_plane_cards)


def associate(cards: np.ndarray, symbols: List[Symbol], order: int):
    # generate the patterns for the lines to pass through the square
    # arrangement of cards
    patterns = [np.array((1, 0), int)]
    for patnum in range(order - 1):
        patterns.append((patnum, 1))
    print("line paths:", patterns)

    symbol_num = 0
    for pattern in patterns:
        add_symbol(cards, pattern, symbols[symbol_num : symbol_num + order - 1], order)
        symbol_num += order - 1


def add_symbol(
    cards: np.ndarray, pattern: Tuple[int, int], symbols: List[Symbol], order: int
):
    """
    add a symbol to all cards in the affine grid by following a path described by
    pattern from eaach starting point along the top row (or left column). Each starting
    point and path gets a symbol, thus this function needs a list of symbols to apply
    of length order - 1
    """
    print("adding symbols:", symbols)

    xstep, ystep = pattern
    if ystep == 0:
        # start from cards in the left column
        start_points = [np.array((0, i), int) for i in range(order - 1)]
    else:
        # start from cards in the top row
        start_points = [np.array((i, 0), int) for i in range(order - 1)]

    for line, start in enumerate(start_points):
        point = start
        # each line is order - 1 long and may wrap around the edges of the
        # square
        for step in range(order - 1):
            cards[tuple(point)].symbols.append(symbols[line])
            # use pattern to move on to the next point in the line
            # with modulus providing a wrap around
            point = (point + pattern) % (order - 1)


def add_infinite_incidences(cards: np.ndarray, symbols: List[Symbol], order: int):
    """
    The affine_plane cards reperesent the incendences in finite space. There are
    additional cards of number <order> to add. These represent the incedences at
    infinity and there is also one more symbol to add to each of the affine_plane
    cards
    """
    # todo


def show_cards(cards: np.ndarray):
    size_x, size_y = cards.shape
    for x in range(size_x):
        for y in range(size_y):
            card = cards[x, y]
            print(f"card {card.id} ({x}, {y}) symbols: {card.symbols}")


def verify(cards: np.ndarray):
    """
    verify that every card matches a symbol with each other card
    exactly once
    """
    for card in cards.flatten():
        for symbol in card.symbols:
            # todo can I use vectorized vcard to simplify this?
            matches = []
            for match_card in cards.flatten():
                if symbol in match_card.symbols:
                    matches.append(match_card)
            matches.remove(card)
            if len(matches) != 1:
                print(
                    f"ERROR: card {card.id} symbol {symbol.id} "
                    "matches {[m.id for m in matches]}"
                )
