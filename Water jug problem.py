from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0, 0)])  # (amount in jug1, amount in jug2, steps)
    
    while queue:
        jug1, jug2, steps = queue.popleft()

        # Check if we have reached the target
        if jug1 == target or jug2 == target:
            print(f"Final state: ({jug1}, {jug2})")
            print(f"Number of steps taken: {steps}")
            return

        # Mark this state as visited
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Possible actions
        # Fill jug1
        queue.append((jug1_capacity, jug2, steps + 1))
        
        # Fill jug2
        queue.append((jug1, jug2_capacity, steps + 1))
        
        # Empty jug1
        queue.append((0, jug2, steps + 1))
        
        # Empty jug2
        queue.append((jug1, 0, steps + 1))
        
        # Pour from jug1 to jug2
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2, steps + 1))
        
        # Pour from jug2 to jug1
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1, steps + 1))

    print("No solution exists")

# Example usage
m = 3  # Capacity of first jug
n = 5  # Capacity of second jug
d = 4  # Desired amount of water

water_jug_problem(m, n, d)