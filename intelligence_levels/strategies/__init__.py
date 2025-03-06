from typing import Callable
from abc import ABC, abstractmethod

from intelligence_levels.constants import LabType, Point


class Strategy(ABC):

    move: Callable
    sense: Callable

    @abstractmethod
    def run(
        self, matrix: LabType,
        last_position: Point,
        current_position: Point
    ):
        """Run certain strategy to complete the lab"""