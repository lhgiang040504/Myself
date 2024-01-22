"""
Naive backtracking search without any heristics or inference.

import random

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
RESULT = []

def backtrack(assignment):
    Runs backtracking search to find an assignment.

    # Check if assignment is complete
    if len(assignment) == len(VARIABLE):
        if assignment not in RESULT:
            RESULT.append(assignment)
            return assignment
        return False
    
    # Try a new variable
    var = select_unassigned_variable(assignment)
    
    values = ["Monday", "Tuesday", "Wednesday"]
    random.shuffle(values)
    for value in values:
        new_assignment = assignment.copy()
        new_assignment[var] = value
        if consistent(new_assignment):
            result = backtrack(new_assignment)
            if result != None:
                return result
    return None

def select_unassigned_variable(assignment):
    Choose a variable not yet assigned, in order.
    for variable in VARIABLE:
        if variable not in assignment:
            return variable
    return None

def consistent(assignment):
    Check to see if an assignment is consistent.
    for (x, y) in CONSTRAINTS:

        # Only consider arcs where both are assigned
        if x not in assignment or y not in assignment:
            continue

        # If both have same value, then not consistent
        if assignment[x] == assignment[y]:
            return False
        
    # If nothing inconsistent, then assignment is consistent
    return True
for _ in range(10):
    solution = backtrack(dict())
    print(solution)
"""
import random

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
RESULT = []

def backtrack(assignment, results):
    """Runs backtracking search to find an assignment."""
    # Check if assignment is complete
    if len(assignment) == len(VARIABLE):
        if assignment not in results:
            results.append(assignment)
        return

    # Try a new variable
    var = select_unassigned_variable(assignment)

    values = ["Monday", "Tuesday", "Wednesday"]
    random.shuffle(values)
    for value in values:
        new_assignment = assignment.copy()
        new_assignment[var] = value
        if consistent(new_assignment):
            backtrack(new_assignment, results)

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

        # If both have the same value, then not consistent
        if assignment[x] == assignment[y]:
            return False

    # If nothing inconsistent, then assignment is consistent
    return True

backtrack({}, RESULT)
for solution in RESULT:
    print(solution)