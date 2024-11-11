from collections import deque

# Function to check if a state is valid
def is_valid_state(missionaries, cannibals):
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries > 0 and missionaries < cannibals:
        return False
    return True

# Function to check if a state is the goal state
def is_goal_state(state):
    return state == (0, 0, 1)

# BFS algorithm to solve the problem
def missionaries_cannibals():
    # (missionaries_left, cannibals_left, boat_on_left_side)
    start_state = (3, 3, 0)  # All missionaries, cannibals, and the boat are on the left side
    goal_state = (0, 0, 1)   # All have moved to the right side
    
    # List of possible moves: (missionaries, cannibals)
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
    
    # Queue to store the states (BFS)
    queue = deque([(start_state, [])])  # Each entry is (state, path)
    
    # Set to store visited states
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        missionaries_left, cannibals_left, boat_on_left = current_state
        
        # If this is the goal state, print the solution
        if is_goal_state(current_state):
            return path + [current_state]
        
        # Mark the current state as visited
        visited.add(current_state)
        
        # Determine the direction of the boat
        if boat_on_left == 0:  # Boat is on the left side
            for move in moves:
                new_missionaries_left = missionaries_left - move[0]
                new_cannibals_left = cannibals_left - move[1]
                new_state = (new_missionaries_left, new_cannibals_left, 1)  # Boat moves to the right side
                
                # Check if the new state is valid and not visited
                if is_valid_state(new_missionaries_left, new_cannibals_left) and \
                   is_valid_state(3 - new_missionaries_left, 3 - new_cannibals_left) and \
                   new_state not in visited:
                    queue.append((new_state, path + [current_state]))
        
        else:  # Boat is on the right side
            for move in moves:
                new_missionaries_left = missionaries_left + move[0]
                new_cannibals_left = cannibals_left + move[1]
                new_state = (new_missionaries_left, new_cannibals_left, 0)  # Boat moves to the left side
                
                # Check if the new state is valid and not visited
                if is_valid_state(new_missionaries_left, new_cannibals_left) and \
                   is_valid_state(3 - new_missionaries_left, 3 - new_cannibals_left) and \
                   new_state not in visited:
                    queue.append((new_state, path + [current_state]))
    
    return None  # No solution found

# Function to print the solution
def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        for state in solution:
            missionaries_left, cannibals_left, boat_on_left = state
            missionaries_right = 3 - missionaries_left
            cannibals_right = 3 - cannibals_left
            boat_position = "left" if boat_on_left == 0 else "right"
            print(f"Left bank: {missionaries_left}M {cannibals_left}C | "
                  f"Boat: {boat_position} | "
                  f"Right bank: {missionaries_right}M {cannibals_right}C")
        print("Solution found!")

# Find and print the solution
solution = missionaries_cannibals()
print_solution(solution)