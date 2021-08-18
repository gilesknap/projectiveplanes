from itertools import count
from typing import List

from planes.symbols import Symbol

card_num = count()


class Card:
    """
    Represents a card containing symbols.
    """

    def __init__(self) -> None:
        global card_num
        # unique id which increments for each instantiation
        self.id: int = next(card_num)
        self.symbols: List[Symbol] = []
