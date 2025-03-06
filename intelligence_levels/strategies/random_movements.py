import random
from typing import Callable

from intelligence_levels.constants import LabType, Movements, Point
from intelligence_levels.strategies import Strategy


class RandomMovements(Strategy):

    def __init__(self, move: Callable, sense: Callable):
        self.move = move
        self.sense = sense

    def run(
        self,
        matrix: LabType,
        last_position: Point,
        current_position: Point
    ):
        possible_steps = self.sense(matrix, last_position, current_position)
        if not possible_steps:
            return_vector = last_position - current_position
            return_step = Movements(return_vector)
            position, current_position = self.move(matrix, current_position, return_step)
            return position, current_position

        next_step = random.choice(possible_steps)
        position, current_position = self.move(matrix, current_position, next_step)
        return position, current_position

    # get the possible steps
    # discard the last one in which we were (avoid to return)
    # in decision points pick up a random step and move
    # if not more steps than the last one, then return