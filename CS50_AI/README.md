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
    - A* search: optimal if :
        - h(n) is admissible (never overestimates the true cost)
        - h(n) is consistent (for every node n and successor n' with step cost c, h(n) <= h(n') + c)
## Adversarial Search
* MiniMax
    X win : 1
    O win : -1
    nobody win : 0
    MAX (X) aim to maximize score
    MIN (O) aim to minimize score

    Given a state s:
        MAX picks action a in ACTIONS(s) that produces hightest value of Min-Value(result(s, a))

        MIN picks action a in ACTIONS(s) that produces smallest value of MAX-VALUE(result(s, a))
* Opimal - Alpha Beta Pruning
* Depth-Limited Minimax
* Additional Feature - evaluation function

# KNOWLEDGE
## knowledge-based agents
    agents that reason by operating on internal representations of knowledgeff
## sentence
    an assertion about the world in a knowledge represenetation language
## Propositional Logic
    Logical Connective : not, and, or, implication, bicondition
- not
    |     a    |   not(a) |
    |----------|----------|
    | true     | false    |
    | false    | true     |

- and
    | a and b  | true     | false    |
    |----------|----------|----------|
    | true     | true     | false    |
    | false    | false    | false    |

- or
    | a or b   | true     | false    |
    |----------|----------|----------|
    | true     | true     | true     |
    | false    | true     | false    |

- implication
    | a -> b   | true     | false    |
    |----------|----------|----------|
    | true     | true     | false    |
    | false    | true     | true     |

- bicondition
    | a <=> b  | true     | false    |
    |----------|----------|----------|
    | true     | true     | false    |
    | false    | false    | true     |
## model : assignment of a truth value to every propositional symbol (a "possible world")
## knowledge base : a set of sentence known by a knowledge-based agent
    ENTAILMENT
## inference : inference algorithm
## Model Checking
    To determine if KB entail alpha:
    1. Enumerate all possible models.
    2. If in every model where KB is true, alpha is also true, reference KB entail alpha.
    3. Ohterwise, KB does not entail alpha
## Optimal : better way to make inference
- Inference Rules : translate into new forms of knowledge
    - Model-checking : Looking at all the possible worlds
    - Modus Ponens : Not looking at any specific world, we just dealing with the knowledge we know and what conlusions we can arrive at based in that
    - And Elimination : a and b, so just a or likewise just b
    - Double Negation Elimination
    - Implication Elimination
    - Biconditional Elimination
    - De Morgan's Law
    - Distributive Property
- Theorom Proving
    - Resolution Rule
    - Clause:  a disjunction of literals
    - Each literal is either positive or negative (propositional symbols)
    - conjunction normal form (cnf): logical sentence that is a conjunction of clauses
- Convert to CNF
    - Eliminate biconditionals
    - Eliminate implications
    - Move Not inwards using De Morgan's Laws
    - Use distribute law to distribute Or wherever possible
- => Inference by Resolution : Make the contradiction
    - To determine if KB entails alpha:
        - Convert (KB and Not(alpha)) to Conjunctive Normal Form
        - Keep checking to see if we can use resolution to produce a new clause
            - If ever we produce the empty clause (quivalent to False), we have a contradiction, and KB entails alpha
            - Otherwise, if we cannot add new clauses, no entailment
## Limitation of propositional Logic and New Method
- Propositional Logic: Need a lot of propositional symbols in order to represent some fairly basc ideas.

- First-Order Logic: more powerful : Constant symbol and Predicate symbol
    - Universal quantifier: ALL
    - Existential Quantifier: EXISTS

# UNCERTAINTY
## OMEGA - possible word
## SIMA
## unconditional probability
    degree of belief in a proposition in the absence of any other evidence
## conditional ptobability
    degree of belief in a proposition given some evidence that has already been revealed
## Boolean variable and random variable
- Boolean Variable: only two values true/false
- Random Variable: can take on multiple values
    a variable in probability theory with a domain of possible values it can take on
## probability distribution
- independence
- Bayes' Rule
- Joint Probability Distribution
## probability rule
- Negation: P(Not(a)) = 1 - p(a) 
- Inclusion - Exclusion: P(a or b) = P(a) + P(b) - P(a and b)
- Marginalization: P(a) = P(a and b) + P(a nd Not(b))
- Conditioning: 
    P(a|b) = [P(a and b)] / P(b)
    P(a|Not(b)) = [P(a and Not(b))] / P(Not(b))
    Sum that
## Markov Chains
## Bayesian Network
A graphical representation of set of variables and their conditional dependencies.
## inference - inference by enumurations
- Generate all possible worlds
- For each world, calculate the probabilities for each statement
- Choose the most probable one as the result
## CPT - Conditional Probability Table  
Each row represents an outcome of a parent variable, and each column represents an outcome of a child variable
Each row represents an outcome of a parent variable, and each column represents an outcome of a child variable
A table used to describe the joint probability distribution over a set of variables, given the values of
some (or none) of the other variables.
## Kernel - smoothing function
## Approximate Inference
- Sampling: Rejection Sampling
- Likelihood Weighting
## Uncertainty over Time

# OPTIMIZATION
# LEARNING
# NEURAL NETWORKS
# LANGUAGE