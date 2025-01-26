from constants import LabType, ALLOWED_STEP, START_INDICATOR, Movements, Point


def move(
    matrix: LabType,
    start_point: Point,
    direction: Movements
) -> tuple[str, Point]:
    matrix[start_point.x][start_point.y] = ALLOWED_STEP
    next_step = start_point + direction.value

    position = matrix[next_step.x][next_step.y]
    matrix[next_step.x][next_step.y] = START_INDICATOR
    return position, next_step