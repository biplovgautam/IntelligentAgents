import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline  # Uncomment if running in a Jupyter notebook

# 0 = path (white), 1 = wall (black)
maze = np.array([
    [1,0,1,1,1,1,1,1,1,0,1,1], 
    [1,0,1,1,1,1,1,1,1,0,1,1], 
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,1,1],
    [1,0,0,0,1,1,1,1,1,1,1,1],
    [1,0,1,0,1,1,1,0,1,1,1,1],
    [1,0,1,0,0,0,1,0,1,1,1,1],
    [1,0,1,1,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1],
    [0,0,1,1,1,1,1,0,0,0,0,1]
], dtype=int)

# Start (A) and Goal (B)
start = (10, 0)
goal = (6, 7)

# --- #1. Find the nodes ---
# A "node" is just a fancy word for any spot where we're allowed to stand.
# We'll scan the maze and pick out every coordinate that is a path (0).
rows, cols = maze.shape
nodes = [(r, c) for r in range(rows) for c in range(cols) if maze[r, c] == 0]

# --- #2. Find the possible edges/neighbors ---
# An "edge" is a connection. If you're at one spot, can you move to the next?
# We check the four main directions: Up, Down, Left, and Right.
def get_neighbors(node):
    r, c = node
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    neighbors = []
    
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        # We make sure the move stays inside the maze and doesn't hit a wall
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 0:
            neighbors.append((nr, nc))
    return neighbors

# --- #3. Create a graph ---
# Think of the graph as a map's index. For every walkable spot, 
# it lists exactly which other spots it connects to.
graph = {node: get_neighbors(node) for node in nodes}

# --- #4. Apply DFS in the maze ---
# Depth First Search is like an explorer who picks a path and follows it 
# until they hit a dead end, then backtracks to try the next available turn.
def apply_dfs(graph, start, goal):
    stack = [(start, [start])] # A stack helps us keep track of where to explore next
    visited = set()            # This ensures we don't walk in circles!
    
    while stack:
        (current, path) = stack.pop() # We take the most recent path we've found
        
        if current == goal:
            return path # We found it! Send the path back.
            
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    # Add the neighbor and the updated path to the stack
                    stack.append((neighbor, path + [neighbor]))
    return None

# Let's run the search!
final_path = apply_dfs(graph, start, goal)

# --- #5. Display the path in the maze ---
# Now we take your original plotting logic and overlay our discovery.
fig, ax = plt.subplots(figsize=(8, 7))
ax.imshow(maze, cmap="gray_r", interpolation="nearest")

# Re-drawing your grid borders
ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
ax.grid(which="minor", color="gray", linestyle="-", linewidth=0.8)
ax.tick_params(which="minor", bottom=False, left=False)

# Overlaying the DFS path as a yellow line
if final_path:
    path_array = np.array(final_path)
    # path_array[:, 1] is the X (column), path_array[:, 0] is the Y (row)
    ax.plot(path_array[:, 1], path_array[:, 0], color="yellow", linewidth=4, label="DFS Path")

# Re-adding your labels for Start and Goal
ax.text(start[1], start[0], "A", ha="center", va="center", color="blue", fontsize=16, fontweight="bold")
ax.text(goal[1], goal[0], "B", ha="center", va="center", color="red", fontsize=16, fontweight="bold")

ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Maze Solved via Depth First Search (DFS)")
plt.show()