from collections import deque

# Initialize the puzzle
def initializePuzzle(startState):
    return startState

# Print the puzzle
def printPuzzle(puzzle):
    for row in puzzle:
        print(row)
    print()

# Get possible moves
def getPossibleMoves(puzzle):
    moves = []
    zero_pos = [(i, row.index(0)) for i, row in enumerate(puzzle) if 0 in row][0]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for d in directions:
        new_pos = (zero_pos[0] + d[0], zero_pos[1] + d[1])
        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
            new_puzzle = [list(row) for row in puzzle]
            new_puzzle[zero_pos[0]][zero_pos[1]], new_puzzle[new_pos[0]][new_pos[1]] = new_puzzle[new_pos[0]][new_pos[1]], new_puzzle[zero_pos[0]][zero_pos[1]]
            moves.append(tuple(map(tuple, new_puzzle)))

    return moves

# Check for goal state
def isGoalState(puzzle):
    return puzzle == ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Depth-First Search (DFS)
def dfs(startState):
    stack = [(startState, [])]

    while stack:
        currentPuzzle, path = stack.pop()
        if isGoalState(currentPuzzle):
            return path
        for move in getPossibleMoves(currentPuzzle):
            if move not in path:  # Avoid cycles
                stack.append((move, path + [move]))

    return "No solution found"

# Breadth-First Search (BFS)
def bfs(startState):
    queue = deque([(startState, [])])

    while queue:
        currentPuzzle, path = queue.popleft()
        if isGoalState(currentPuzzle):
            return path
        for move in getPossibleMoves(currentPuzzle):
            if move not in path:  # Avoid cycles
                queue.append((move, path + [move]))

    return "No solution found"

# Main function
def main():
    startState = ((1, 2, 3), (4, 0, 5), (7, 8, 6))  # Example initial state
    print("Initial Puzzle:")
    printPuzzle(startState)

    print("Solving using DFS:")
    dfsSolution = dfs(startState)
    print("DFS Solution Path:", dfsSolution)

    print("Solving using BFS:")
    bfsSolution = bfs(startState)
    print("BFS Solution Path:", bfsSolution)

if __name__ == "__main__":
    main()
