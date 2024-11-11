from itertools import permutations

def crypt_arithmetic(puzzle):
    # Split the puzzle into left and right parts
    left, right = puzzle.split('==')
    words = left.split('+')
    
    # Get unique letters
    letters = set(''.join(words) + right.strip())
    
    # Check if there are more than 10 unique letters
    if len(letters) > 10:
        print("No solution found: More than 10 unique letters.")
        return
    
    # Try all permutations of digits for the unique letters
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        # Skip if any leading letter is mapped to 0
        if any(mapping[word[0]] == 0 for word in words) or mapping[right.strip()[0]] == 0:
            continue
        
        # Calculate the left side value
        left_value = sum(int(''.join(str(mapping[letter]) for letter in word)) for word in words)
        
        # Calculate the right side value
        right_value = int(''.join(str(mapping[letter]) for letter in right.strip()))
        
        # Check if they are equal
        if left_value == right_value:
            print("Final Solution:")
            for letter in sorted(mapping.keys()):
                print(f"{letter} = {mapping[letter]}")
            return
    
    print("No solution found.")

# Get user input
puzzle = input("Enter the cryptarithmetic puzzle (e.g., SEND + MOST == SENSE): ")
crypt_arithmetic(puzzle)