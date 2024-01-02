
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# DFS
class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.newWalls = []

    def add(self, list_node):
        for node in list_node:
            self.frontier.append(node)

    def contains_state(self, state):
        return any(nodes.state == state for nodes in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node 
        
# BFS
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
# G-BFS
class Heuristic():
    def __init__(self, walls, goal):
        self.frontier = []
        self.newWalls = []
        self.Manhattan_Distance(walls, goal)

    def contains_state(self, state):
        return any(nodes.state == state for nodes in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0

    def Manhattan_Distance(self, walls, goal_point):
        for i, row in enumerate(walls):
            newRow = []
            for j, element in enumerate(row):
                if element is True:
                    newRow.append((True, None))
                elif (i, j) == goal_point:
                    newRow.append((False, 0))
                else:
                    MD = abs(goal_point[0] - i) + abs(goal_point[1] - j)
                    newRow.append((False, MD))
            self.newWalls.append(newRow)

    def add(self, list_node):
        if len(list_node) == 1:
            self.frontier.insert(0, list_node[0])
        else:
            list_node = sorted(list_node, key=lambda x: self.get_distance(x))
            self.frontier[0:0] = list_node
        
    def get_distance(self, node):
        state = node.state
        if state[0] < len(self.newWalls) and state[1] < len(self.newWalls[state[0]]):
            return self.newWalls[state[0]][state[1]][1]
        else:
            return float('inf')

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
# A*
class A_star(Heuristic):
    def __init__(self, walls, goal):
        self.potential_node = {}
        # State method
        self._step = -1
        self.frontier = []
        self.newWalls = []
        self.Manhattan_Distance(walls, goal)

    def add(self, list_node):
        for node in list_node:
            self.potential_node[node] = (self._step, self.newWalls[node.state[0]][node.state[1]][1])
        
        minimumNode = min(self.potential_node, key=lambda k: self.potential_node[k][1] + self.potential_node[k][0])
        self._step = self.potential_node[minimumNode][0]
        del self.potential_node[minimumNode]
        self.frontier.insert(0, minimumNode)
        

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            self._step += 1
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
class Maze():
    def __init__(self, filename, type):
        """
        self.start
        self.end
        self.height
        self.width
        self.walls
        self.solution
        """
        self.type = type

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
        self.step = None

    def print(self):
        #solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("🟦", end="")
                elif (i, j) == self.start or (i, j) == self.goal:
                    print("🟫", end="")
                elif self.solution is not None and (i, j) in self.solution:
                    """if solution is none, it cant iterable"""
                    print("🟧", end="")
                elif self.explored is not None and (i, j) in self.explored:
                    """if solution is none, it cant iterable"""
                    print("🟪", end="")
                else:
                    print("  ", end="")
            print()
        #print()
        
    def neighbors(self, state):
        row, col = state

        # All possible actions
        candidates = [
            ((row, col + 1), 'R'),  # Right
            ((row, col - 1), 'L'),  # Left
            ((row - 1, col), 'U'),  # Up
            ((row + 1, col), 'D'),  # Down
        ]

        # Ensure actions are valid
        result = []
        for (r, c), action in candidates:
            try:
                if not self.walls[r][c] and r in range(self.height) and c in range(self.width):
                    result.append((action, (r, c)))
            except IndexError:
                continue
        
        return result
    
    def solve(self):
        """Finds a solution to maze, if one exists"""

        # Keep track of number of states explored - path cost
        self.num_explored = 0

        # Initialize frontier to jusst the starting position
        start = Node(state=self.start, parent=None, action=None)
        if self.type == "DFS":
            frontier = StackFrontier()
        elif self.type == "BFS":
            frontier = QueueFrontier()
        elif self.type == "G-BFS":
            frontier = Heuristic(self.walls, self.goal)
        else:
            frontier = A_star(self.walls, self.goal)
        
        frontier.add([start])

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
                #cells.reverse()

                self.solution = cells
                self.step = actions
                return
            
            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            children = []
            for action, cell in self.neighbors(node.state):
                child = Node(state=cell, parent=node, action=action)
                if child.state not in self.explored and not frontier.contains_state(child.state):
                    children.append(child)
            frontier.add(children)


maze = Maze("maze/maze5.txt", 'A*')

maze.solve()

maze.print()
print(maze.num_explored)
print()



