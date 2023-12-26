
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node 
        

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        

class Maze():
    def __init__(self, filename):
        """
        self.start
        self.end
        self.height
        self.width
        self.walls
        self.solution
        """

        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")
        
        # Determine height and width of maze
        content = contents.splitlines()
        self.height = len(content)
        self.width = max(len(line) for line in content)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range (self.width):
                try:
                    if content[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif content[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif content[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        #solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("🟦", end="")
                elif (i, j) == self.start or (i, j) == self.goal:
                    print("🟥", end="")
                elif self.solution is not None and (i, j) in self.solution:
                    """if solution is none, it cant iterable"""
                    print("🟧", end="")
                elif self.explored is not None and (i, j) in self.explored:
                    """if solution is none, it cant iterable"""
                    print("🟨", end="")
                else:
                    print("  ", end="")
            print()
        print()
        
    def neighbors(self, state):
        row, col = state

        # All possible actions
        candidates = [
            ((row - 1, col), 'U'),  # Up
            ((row + 1, col), 'D'),  # Down
            ((row, col - 1), 'L'),  # Left
            ((row, col + 1), 'R'),  # Right
        ]

        # Ensure actions are valid
        result = []
        for (r, c), action in candidates:
            try:
                if not self.walls[r][c]:
                    result.append((action, (r, c)))
            except IndexError:
                continue
        
        return result
    
    def solve(self):
        """Finds a solution to maze, if one exists"""

        # Keep track of number ò states explored
        self.num_explored = 0

        # Initialize frontier to jusst the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")
            
            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
            
                # Follow parent nodes to find solution
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)

                    node = node.parent
                
                actions.reverse()
                cells.reverse()

                self.solution = cells
                return
            
            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, cell in self.neighbors(node.state):
                child = Node(state=cell, parent=node, action=action)
                if child.state not in self.explored:
                    frontier.add(child)
            

maze = Maze('maze2.txt')
maze.solve()
maze.print()
print(maze.num_explored)

