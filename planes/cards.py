from itertools import count
from typing import List

from planes.symbols import Symbol

card_num = count()


class Card:
    """
    Represents a card containing symbols.
    """

    def __init__(self, id: int = None, symbols: List[Symbol] = None) -> None:
        global card_num
        # unique id which increments for each instantiation
        self.id: int = id or next(card_num)
        self.symbols: List[Symbol] = symbols or []
