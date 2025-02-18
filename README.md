## Intelligence levels:
- Random Behavior
- Reactive behavior
- Proactive behavior
- Memory based behavior


## Bibliography
- Russell, S., & Norvig, P. (2021). "Artificial Intelligence: A Modern Approach" (4th ed.). Pearson.
- An Introduction to MultiAgent Systems
- Introduction to AI Robotics

### Random Behavior

This guide provides an explanation of how to set up and run the maze traversal program. 
The program uses a defined strategy to navigate through a maze represented as a grid 
matrix. It supports both time-based and endpoint-driven execution.

### Memory Behavior
The strategy leverages memory to optimize movement through a maze. 
It records each position and its possible moves to avoid revisiting paths 
unnecessarily. 
When faced with blocked routes, it backtracks to the last decision point and 
tries alternate paths. 
If multiple paths are available, it prioritizes unexplored ones, and, if needed, 
revisits known paths. 
By using memory and logical backtracking, this strategy ensures efficient exploration while minimizing redundant movements.


### **How to Run the Program**
#### **Requirements**
1. **Python Version:** Python 3.9 or above.
2. **Dependencies:** Ensure all necessary constants, strategies, sensors, and actuators files are in place, as provided in the project.

#### **Setup**
To run the program, ensure the following:
- Use the provided maze (`LAB`) string or customize your maze based on the format specified in the examples below.
- Select the strategy for movement and sensing.
- Optionally, select the newly added `memory` strategy for efficient maze traversal. (NEW)

#### **Run the Program**
Run the program using the command-line interface (CLI):
``` bash
  python main.py --max_time <time_in_seconds>
```
#### **Parameters**
- `--max_time`: _(Optional)_ Specifies the maximum execution time (in seconds). If omitted, the program will run until the endpoint (`E`) is reached.
- `--strategy`: _(Optional)_ Specify the traversal strategy (`random`, `memory`, etc.). Defaults to `random`.
- `--step_velocity`: _(Optional)_ Specify the change velocity in each step

### **Examples**
#### Example 1: Run with a time limit of 10 seconds
``` bash
  python main.py --max_time 10
```
This will run the program for a maximum of 10 seconds. If the endpoint (`E`) is not found within this time, it will stop execution.
#### Example 2: Run without a time limit
``` bash
  python main.py --strategy memory
```
This will run the program until the endpoint (`E`) is reached, regardless of the time taken.

### **Code Overview**
#### **Key Modules**
1. `main.py`:
    - Parses arguments (`max_time`).
    - Sets up the maze (`LAB`) and initializes the strategy.
    - Executes the traversal logic.

2. `sensors.py`:
    - Contains the logic to detect valid movements around a point in the maze.
    - Filters valid steps based on allowed (`O`) and endpoint (`E`) steps.

3. `actuators.py`
    - Controls how movements are performed and updates the matrix dynamically. 

4. `strategies`:
    - `random_movements.py`: Implements a strategy that makes random moves in the maze.
    - `memory_based.py`: Implements an advanced strategy leveraging memory to avoid revisiting the same paths. (NEW)
    - `actuators.py`: Controls how movements are performed and updates the matrix dynamically.

5. `constants.py`:
    - Defines all constants, such as the maze format, movement directions, start, end points, etc.

### **Workflow**
1. **Initialize the Maze:**
    - The maze is defined in the `LAB` string variable.
    - It is represented as a grid containing:
        - `S`: Start point
        - `E`: End point
        - `X`: Blocked path
        - `O`: Open path

2. **Select a Strategy:**
    - The program currently supports the `RandomMovements` and `MemoryBased` strategies.

3. **Run the Loop:**
    - Two termination conditions:
        - If `max_time` is provided, the loop stops after the specified time.
        - If `max_time` is `None`, the loop continues until the endpoint (`E`) is reached.

4. **Output:**
    - The program displays the maze state at every step of the strategy execution.
    - Outputs coordinates of the endpoint (`E`) when found or indicates a timeout.

## **Customization**
### **Modifying the Maze**
To change the maze, update the `LAB` variable in `main.py` with a new maze string. Example:
``` python
LAB = """
    X X X X
    S O O X
    X O O E
    X X X X
"""
```
### **Adding New Strategies**
- To add a new strategy, create a new Python file in the `strategies/` directory.
- Subclass the `Strategy` class and implement the `run` method:
``` python
from strategies import Strategy


class YourCustomStrategy(Strategy):
    def __init__(self, move, sense):
        self.move = move
        self.sense = sense

    def run(self, matrix, current_position, last_position):
        # Your custom logic here
        pass
```
- Use the new strategy in `main.py` by replacing the strategy initialization:
``` python
strategy = YourCustomStrategy(move, sense)
```
### Example Maze Run Output
#### Input Maze:
``` text
    X X X X
    S O O X
    X O O E
    X X X X
```
#### Output:
``` bash
    Movement
    X X X X
    O S O X
    X O O E 
    X X X X
    
    Movement
    X X X X 
    O O O X
    X S O E
    X X X X
    
    Movement
    X X X X 
    O O O X
    X O S E
    X X X X
    
    Movement
    X X X X 
    O O O X
    X O O S
    X X X X
    
    End point (E) found at: (2, 4)
```
