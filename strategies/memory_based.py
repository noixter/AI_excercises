import random
from typing import Callable

from constants import LabType, Point, Movements, END_INDICATOR
from sensors import get_next_step_value
from strategies import Strategy


class MemoryBased(Strategy):

    steps_memory: dict[Point, dict[str, list[Point | Movements]]] = {}

    def __init__(self, move: Callable, sense: Callable):
        self.move = move
        self.sense = sense

    def run(
        self,
        matrix: LabType,
        last_position: Point,
        current_position: Point
    ):
        if current_position in self.steps_memory:
            possible_steps = self.steps_memory[current_position].get('unknown')
        else:
            possible_steps = self.sense(matrix, last_position, current_position)

        if not possible_steps:
            if not current_position in self.steps_memory:
                return self.calculate_return(matrix, current_position, last_position)
            else:
                return_step = self.steps_memory[current_position]['known'][0]
                position, current_position = self.move(matrix, current_position, return_step)
                return position, current_position

        for step in possible_steps:
            next_step_value = get_next_step_value(matrix, current_position, step)
            if next_step_value == END_INDICATOR:
                next_step = step
                break
        else:
            next_step = random.choice(possible_steps)

        possible_steps.remove(next_step)
        if len(possible_steps) >= 1:
            self.steps_memory[current_position] = {
                'unknown': possible_steps,
                'known': [Movements(last_position - current_position)]
            }

        position, current_position = self.move(matrix, current_position, next_step)
        return position, current_position

    def calculate_return(self, matrix: LabType, current_position: Point, last_position: Point):
        return_step = Movements(last_position - current_position)
        position, current_position = self.move(matrix, current_position, return_step)
        return position, current_position

    # get the possible movements
    # save in memory last position and its possible movements
    # move to the first one possible movement and remove them from the list
    # if movement gets block, return to the last decision point known
    # choose another movement from the list
    # if movement gets block again, return to the visited option in list of possible
    # options