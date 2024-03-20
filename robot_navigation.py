class Grid:
    def __init__(self, grid_size, walls, initial_pos, goal_positions):
        self.grid_size = grid_size
        self.walls = self.set_walls(walls)
        self.initial_pos = initial_pos
        self.goal_positions = goal_positions

    def set_walls(self, walls):
        wall_set = set()
        for x, y, w, h in walls:
            for i in range(w):
                for j in range(h):
                    wall_set.add((x + i, y + j))
        return wall_set

    def is_free(self, position):
        return position not in self.walls and 0 <= position[0] < self.grid_size[0] and 0 <= position[1] < self.grid_size[1]

    def is_goal(self, position):
        return position in self.goal_positions

def parse_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        grid_size = tuple(map(int, lines[0].strip()[1:-1].split(',')))
        initial_pos = tuple(map(int, lines[1].strip()[1:-1].split(',')))
        goal_positions = [tuple(map(int, pos.strip()[1:-1].split(','))) for pos in lines[2].split('|')]
        walls = [tuple(map(int, wall.strip()[1:-1].split(','))) for wall in lines[3:]]

        return {
            "grid_size": grid_size,
            "initial_pos": initial_pos,
            "goal_positions": goal_positions,
            "walls": walls
        }

def dfs(grid, start, goal):
    stack = [(start, [start])]  # Stack of tuples (position, path)
    visited = set()

    while stack:
        (vertex, path) = stack.pop()  # Get the last added vertex and path
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in get_neighbors(vertex, grid):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

def get_neighbors(position, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # UP, DOWN, LEFT, RIGHT
    for d in directions:
        next_pos = (position[0] + d[0], position[1] + d[1])
        if grid.is_free(next_pos):
            neighbors.append(next_pos)
    return neighbors

if __name__ == "__main__":
    filename = "RobotNav-test.txt"
    problem_spec = parse_input_file(filename)
    grid = Grid(problem_spec['grid_size'], problem_spec['walls'], problem_spec['initial_pos'], problem_spec['goal_positions'])

    start = problem_spec['initial_pos']
    # Attempting DFS to the first goal for simplicity; adjust as needed
    goal = problem_spec['goal_positions'][0]

    path = dfs(grid, start, goal)
    print("Path to goal:", path if path else "No path found.")
