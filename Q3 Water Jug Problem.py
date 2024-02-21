from collections import deque

# Function to check if a state is valid
def is_valid_state(state, jug1_capacity, jug2_capacity):
    jug1, jug2 = state
    return jug1 >= 0 and jug2 >= 0 and jug1 <= jug1_capacity and jug2 <= jug2_capacity

# Function to check if a state is the goal state
def is_goal_state(state, goal_amount):
    return state[0] == goal_amount

# Function to get all possible next states from the current state
def get_next_states(state, jug1_capacity, jug2_capacity):
    jug1, jug2 = state
    next_states = []
    
    # Fill jug1
    next_states.append((jug1_capacity, jug2))
    
    # Fill jug2
    next_states.append((jug1, jug2_capacity))
    
    # Empty jug1
    next_states.append((0, jug2))
    
    # Empty jug2
    next_states.append((jug1, 0))
    
    # Pour jug1 to jug2 until jug2 is full or jug1 is empty
    pour_amount = min(jug1, jug2_capacity - jug2)
    next_states.append((jug1 - pour_amount, jug2 + pour_amount))
    
    # Pour jug2 to jug1 until jug1 is full or jug2 is empty
    pour_amount = min(jug2, jug1_capacity - jug1)
    next_states.append((jug1 + pour_amount, jug2 - pour_amount))
    
    return next_states

# Function to solve the Water Jug Problem using breadth-first search
def solve_water_jug_problem(jug1_capacity, jug2_capacity, goal_amount):
    start_state = (0, 0)
    visited = set()
    queue = deque([(start_state, [])])
    
    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue
        
        visited.add(current_state)
        if is_goal_state(current_state, goal_amount):
            return path
        
        next_states = get_next_states(current_state, jug1_capacity, jug2_capacity)
        for next_state in next_states:
            if is_valid_state(next_state, jug1_capacity, jug2_capacity) and next_state not in visited:
                queue.append((next_state, path + [next_state]))
    
    return None

# Take input for jug capacities and goal amount of water
jug1_capacity = int(input("Enter the capacity of the first jug: "))
jug2_capacity = int(input("Enter the capacity of the second jug: "))
goal_amount = int(input("Enter the goal amount of water: "))

# Solve the Water Jug Problem
solution = solve_water_jug_problem(jug1_capacity, jug2_capacity, goal_amount)

# Print the solution
if solution:
    print("Solution Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
