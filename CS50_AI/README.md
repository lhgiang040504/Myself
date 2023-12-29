# SEARCH
## agent
    Entity that perceives its environment and acts upon that environment.
## state
    A configuration of the agent and its environment.
    INITIAL STATE : The state in which the agent begins.
## actions
    Choices that can be made in a state.
    ACTIONS(s) return the set of actions that can be executed in state s.
## trasition model
    A description of what state results from performing any applicable action in any state.
    RESULTS(s, a) return the sate resulting from performing action a in state s.
## state space
    The set of all states reachable from the initial state by any sequence of actions (graph).
## goad test
    Way to determine whether a ginven state is a goal state.
## path cost
    Numerical cost associated with a given path.
## search problem
* solution
    A sequence of actions that leads from the initial state to a goal state.
    OPTIMAL SOLUTION: a solution that ahs the lowest path cost among all solutions.
* node
    A data structure that keeps ttrack of 
    - a state
    - a parent (node that generated this node)
    - an action (action applied to parent to get node)
    - a path cost (from initial state to node)
* frontier
    The frontier is going to repersent all of the things that we could explore next that we havent yet explored or visited.
* approach 
    - Start with a frontier that contains the initial state.
    - Repeat:
        - If the frontier is empty, then no solution.
        - Remove a node from the frontier.
        - If node contains goal state, return the solution.
        - Expand node, add all neighbors of that node to the frontier.
* revised approach
    - Start with a frontier that contains the initial state.
    - Start with an empty explored set.
    - Repeat:
        - If the frontier is empty, then no solution.
        - Remove a node from the frontier.
        - If node contains goal state, return the solution.
        - Add the node to the explored set.
        - Expand node, add all neighbors of that node to the frontier if they arent already in the frontier or explored set.
* glossed step - remove node
    * stack
        last-in first-out data type.
        DFS - Depth First Search: always expands the deepest node in the frontier.
    * queue
        first0in first-out data type.
        BFS - Beadth First Search: always expands the shallowest node in the frontier.
## uninform-search adn inform-search
* UNINFORM SEARCH
    Search strategy that uses no problem-specific knowledge.
    /*Basic above*/
* INFORM SEARCH
    Search strategy that uses problem-specific knowledge to find solutions more efficient.
    - GREEDY BEST-FIRST SEARCH (G-BFS): Search algorith that expands the node that is closest to the goal, as estimated by a heuristic function h(n).
    Manhatan distance
    - A* search
    

# KNOWLEDGE
# UNCERTAINTY
# OPTIMIZATION
# LEARNING
# NEURAL NETWORKS
# LANGUAGE