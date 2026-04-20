import numpy as np
import matplotlib.pyplot as plt

# 0 = path, 1 = wall
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

start = (10, 0)
goal = (6, 7)

rows, cols = maze.shape

# -------------------------
# 1. Find nodes
# -------------------------
nodes = []
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 0:
            nodes.append((i, j))

# -------------------------
# 2. Possible directions
# -------------------------
possible_direction = ((0,1),(0,-1),(1,0),(-1,0))

# -------------------------
# 3. Create graph
# -------------------------
graph = {}

for row, col in nodes:
    neighbors = []
    for d_row, d_col in possible_direction:
        nr = row + d_row
        nc = col + d_col

        if 0 <= nr < rows and 0 <= nc < cols:
            if maze[nr][nc] == 0:
                neighbors.append((nr, nc))

    graph[(row, col)] = neighbors

# -------------------------
# 4. DFS FUNCTION
# -------------------------
def dfs_path(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current == goal:
            break

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    if neighbor not in parent:
                        parent[neighbor] = current

    # reconstruct path
    if goal not in parent:
        return None

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path

# -------------------------
# Run DFS
# -------------------------
path = dfs_path(graph, start, goal)
print("DFS Path:", path)

# -------------------------
# 5. Display path
# -------------------------
fig, ax = plt.subplots(figsize=(8,7))
ax.imshow(maze, cmap="gray_r")

# draw grid
ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
ax.grid(which="minor", color="gray", linestyle="-", linewidth=0.5)
ax.tick_params(which="minor", bottom=False, left=False)

# plot path
if path:
    for r, c in path:
        ax.plot(c, r, "bo")  # blue dots

# labels
ax.text(start[1], start[0], "A", color="green", ha="center", va="center")
ax.text(goal[1], goal[0], "B", color="red", ha="center", va="center")

ax.set_title("DFS Path in Maze")
ax.set_xticks([])
ax.set_yticks([])
plt.show()