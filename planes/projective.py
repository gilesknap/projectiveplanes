from numpy.core.defchararray import mod
from planes.cards import Card
from symbols import Symbol
import numpy as np

from typing import List, Tuple


def project(order: int):
    # count of cards and symbols
    count = order ** 2 - order + 1

    print("number of cards:", count)

    # layout most of the cards in square of order - 1
    affine_plane_cards = np.ndarray([order - 1, order - 1], Card)
    symbols = [Symbol(id=i) for i in range(count)]

    associate(affine_plane_cards, symbols, order)

    show_cards(affine_plane_cards)


def associate(cards: np.ndarray, symbols: List[Symbol], order: int):
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
    point and path gets a 
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
        for step in range(order - 1):
            cards[point].symbols += symbols[line]
            point = (point + pattern) % (order -1)

def show_cards(cards: np.ndarray):
    size_x, size_y = cards.shape
    for x in range(size_x):
        for y in range(size_y):
            card = cards[x,y]
            print("card",x,y,"symbols:", card.symbols)

 