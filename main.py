from sensors import sense
from strategies import Strategy
from constants import LabType, START_INDICATOR, END_INDICATOR, Point
from actuators import move
from strategies.memory_based import MemoryBased
from strategies.random_movements import RandomMovements
import time
import argparse


LAB = """
    X X X X X X X X X X X X X X X
    S O X O O O X O O O O O O O X
    X O X O X O X O X X X X X O X
    X O X O X O O O X O O O X O X
    X O O O X X X X X O X O O O X
    X X X O X O O O O O X X X O X
    X O O O X O X X X X X O O O X
    X O X O O O O O O O X O X O X
    X O X X X X X O X O O O X O X
    X O O O O O X O X X X O X O X
    X X X X X O X O O O X O X O X
    X O O O X O O O X O X O O O X
    X O X O X O X X X O X X X O X
    X O X O O O O O O O O O O O E
    X X X X X X X X X X X X X X X
"""

LAB1 = """
    X X X X X X X
    S O O O O O X
    X X O X O X X
    X O O O X X X
    X X O X X X X
    X X O O O O E
    X X X X X X X
"""


AVAILABLE_STRATEGIES = {
    'random': RandomMovements,
    'memory': MemoryBased,
}


def create_matrix(lab: str) -> LabType:
    return [
        [char for char in line if char != " "]
        for line in lab.strip().splitlines()
    ]


def traverse_matrix(matrix: LabType) -> None:
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            print(matrix[row][column], end=" ")
        print("\n")
        

def get_initial_point(matrix: LabType) -> Point:
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == START_INDICATOR:
                return Point(row, column)



def main(
    lab: str,
    strategy: Strategy,
    max_time: float,
    step_velocity: float
) -> None:
    steps_count = 0
    matrix = create_matrix(lab)
    current_position = get_initial_point(matrix)
    start_time = time.time()
    last_position = current_position
    end_point = None

    while True:
        if max_time is not None and time.time() - start_time > max_time:
            print(
                f"Timeout reached. Could not find the end point within "
                f"{max_time} seconds."
            )
            break
        if end_point is not None:
            elapsed_time = (time.time() - start_time) - (steps_count * step_velocity)
            print(
                f"End point (E) found at: {end_point} within "
                f"{elapsed_time:.2f} seconds."
            )
            break
        steps_count += 1
        position, next_point = strategy.run(matrix, last_position, current_position)
        print("Movement")
        traverse_matrix(matrix)
        if position == END_INDICATOR:
            end_point = next_point
        last_position, current_position = current_position, next_point
        time.sleep(step_velocity)


if __name__ == '__main__':
    # TODO implement another arg variable to read a new lab
    parser = argparse.ArgumentParser(
        description="Set up the maximum time for the maze traversal."
    )
    parser.add_argument(
        "-m",
        "--max_time",
        type=float,
        help="Maximum time allowed for the traversal."
    )
    parser.add_argument(
        '-s',
        '--strategy',
        type=str,
        default='random',
        choices=AVAILABLE_STRATEGIES.keys(),
        help="Strategy to use for the agent."
    )
    parser.add_argument(
        '-sv',
        '--step_velocity',
        type=float,
        default=0.5,
        help="Step velocity for the agent in seconds."
    )
    args = parser.parse_args()

    strategy = AVAILABLE_STRATEGIES.get(args.strategy)(
        move, sense
    )
    main(LAB, strategy, max_time=args.max_time, step_velocity=args.step_velocity)


