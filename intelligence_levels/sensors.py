from typing import Optional

from constants import LabType, ALLOWED_STEP, END_INDICATOR, Movements, Point


def sense(
    matrix: LabType,
    last_position: Point,
    current_position: Point,
    depth: int = 1
) -> list[Optional[Movements]]:
    possible_steps = []
    if depth == 0:
        raise ValueError("Depth cannot be zero")

    for movement in Movements:
        new_movement = current_position + movement.value
        new_movement *= depth
        if new_movement.x < 0 or new_movement.y < 0:
            continue

        # dont return to the last position
        if last_position == new_movement:
            continue

        # next step out of the lab boundaries
        try:
            next_step = matrix[new_movement.x][new_movement.y]
        except IndexError:
            continue

        # movement allowed
        if next_step == ALLOWED_STEP or next_step == END_INDICATOR:
            possible_steps.append(movement)

    return possible_steps


def get_next_step_value(matrix: LabType, current_position: Point, next_step: Movements):
    new_position = current_position + next_step.value
    try:
        next_step = matrix[new_position.x][new_position.y]
        return next_step
    except IndexError:
        return False