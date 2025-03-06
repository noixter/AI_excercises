from typing import Callable
from abc import ABC, abstractmethod

from intelligence_levels.constants import LabType


class Strategy(ABC):

    move: Callable
    sense: Callable

    @abstractmethod
    def run(
        self, matrix: LabType,
        last_position: tuple[int, int],
        current_position: tuple[int, int]
    ):
        """Run certain strategy to complete the lab"""