"""
Naive backtracking search without any heristics or inference.
"""

VARIABLE = ["A", "B", "C", "E", "F", "G"]
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "F"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]

def backtrack(assignment):
    """Runs backtracking search to find an assignment."""

    # Check if assignment is complete
    if len(assignment) == len(VARIABLE):
        return assignment
    
    # Try a new variable
    var = select_unassigned_variable(assignment)
    for value in ["Monday", "Tuesday", "Wednesday"]:
        new_assignment = assignment.copy()
        new_assignment[var] = value
        if consistent(new_assignment):
            result = backtrack(new_assignment)
            if result != None:
                return result
    return None

def select_unassigned_variable(assignment):
    """Choose a variable not yet assigned, in order."""
    for variable in VARIABLE:
        if variable not in assignment:
            return variable
    return None

def consistent(assignment):
    """Check to see if an assignment is consistent."""
    for (x, y) in CONSTRAINTS:

        # Only consider arcs where both are assigned
        if x not in assignment or y not in assignment:
            continue

        # If both have same value, then not consistent
        if assignment[x] == assignment[y]:
            return False
        
    # If nothing inconsistent, then assignment is consistent
    return True

solution = backtrack(dict())
print(solution)