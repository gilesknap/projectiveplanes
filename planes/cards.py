from typing import ClassVar, List

import numpy as np
from numpy.lib.function_base import vectorize

from planes.symbols import Symbol


class Card:
  """
  Represents a card containing symbols. 
  """
  def __init__(self, id:int) -> None:
      self.id: int = id
      self.symbols: List[Symbol] = []

# vectorize Card so that it can be constructed across a numpy array of VCard
VCard = np.vectorize(Card)
