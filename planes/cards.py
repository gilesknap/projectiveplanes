from typing import List
from dataclasses import dataclass
from planes.symbols import Symbol

class Card:
  id: int
  symbols: List[Symbol]