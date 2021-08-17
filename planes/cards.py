from typing import List

import numpy as np

from planes.symbols import Symbol


class Card:
    """
    Represents a card containing symbols.
    """

    def __init__(self, identifier: int) -> None:
        self.id: int = identifier
        self.symbols: List[Symbol] = []


# vectorize Card so that it can be constructed across a numpy array of VCard
VCard = np.vectorize(Card)
