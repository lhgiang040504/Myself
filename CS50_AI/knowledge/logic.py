import itertools

class Sentence():

    def evaluate(self, model):
        """Evaluates the logical sentence."""
        raise Exception("nothing to evaluate")
    
    def formula(self):
        """Return string formula representing logical sentence."""
        return set()
    
    @classmethod
    def validate(cls, sentence):
        if not isinstance(sentence, Sentence):
            raise TypeError('Sentence must be an instance of Sentence, must be a logical sentence')
        
    @classmethod
    def parenthesize(cls, sentence):
        """Parenthesizes an expression if not already parenthesized."""
        def balance(sentence):
            """Checks if a string has balanced parentheses"""
            count = 0
            for char in sentence:
                if char == '(':
                    count += 1
                elif char == ')':
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0
        # Check if sentence is already parenthesized or it is a single character or it is a empty sentence
        if not len(sentence) or sentence.isalpha() or (
            sentence[0] == "(" and sentence[-1] == ")" and balance(sentence[1:-1])
        ):
            return sentence
        else:
            return f"({sentence})"
        
class Symbol(Sentence):
    def __init__(self, name):
        self.name = name
    
    
    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name
    
    # Hash value
    def __hash__(self):
        return hash(("symbol", self.name))
    
    # String representation of the object
    def __repr__(self):
        return self.name
    
    def evaluate(self, model):
        try:
            return bool(model[self.name])
        except KeyError:
            raise (f"variable {self.name} not in model")
        
    # String representation of the object but for other format
    def formula(self):
        return self.name
    
    def symbols(self):
        return {self.name}
    
class Not(Sentence):
    def __init__(self, operand):
        Sentence.validate(operand)
        self.operand = operand

    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand
    
    def __hash__(self):
        return hash(("not", hash(self.operand)))
    
    def __repr__(self):
        return f"Not ({self.operand})"
    
    def evaluate(self, model):
        return not self.operand.evaluate(model)
    
    def formula(self):
        return "¬" + Sentence.parenthesize(self.operand.formula())
    
    def symbols(self):
        return self.operand.symbols()
    
class And(Sentence):
    def __init__(self, *conjuncts):
        for conjunct in conjuncts:
            Sentence.validate(conjunct)
        self.conjuncts = list(conjuncts)

    def __eq__(self, other):
        return isinstance(other, And) and self.conjuncts == other.conjuncts

    def __hash__(self):
        return hash(("and", tuple(hash(conjunct) for conjunct in self.conjuncts)))

    def __repr__(self):
        return f"And({', '.join(repr(conjunct) for conjunct in self.conjuncts)})"

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)

    def formula(self):
        return " ∧ ".join(Sentence.parenthesize(conjunct.formula()) for conjunct in self.conjuncts)

    def add(self, conjunct):
        Sentence.validate(conjunct)
        self.conjuncts.append(conjunct)

    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])

class Or(Sentence):
    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
        self.disjuncts = list(disjuncts)

    def __eq__(self, other):
        return isinstance(other, Or) and self.disjuncts == other.disjuncts

    def __hash__(self):
        return hash(("or", tuple(hash(disjunct) for disjunct in self.disjuncts)))

    def __repr__(self):
        return f"Or({', '.join(repr(disjunct) for disjunct in self.disjuncts)})"

    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)

    def formula(self):
        return " ∨ ".join(Sentence.parenthesize(disjunct.formula()) for disjunct in self.disjuncts)

    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])

class Implication(Sentence):
    def __init__(self, antecedent, consequent):
        Sentence.validate(antecedent)
        Sentence.validate(consequent)
        self.antecedent = antecedent
        self.consequent = consequent

    def __eq__(self, other):
        return (isinstance(other, Implication) 
                and self.antecedent == other.antecedent
                and self.consequent == other.consequent)

    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))

    def __repr__(self):
        return f"Implication({repr(self.antecedent)}, {repr(self.consequent)})"

    def evaluate(self, model):
        return (not self.antecedent.evaluate(model)) or self.consequent.evaluate(model)

    def formula(self):
        antecedent_formula = Sentence.parenthesize(self.antecedent.formula())
        consequent_formula = Sentence.parenthesize(self.consequent.formula())
        return f"{antecedent_formula} → {consequent_formula}"
    
    def symbols(self):
        return set.union(self.antecedent.symbols(), self.consequent.symbols())

class Biconditional(Sentence):
    def __init__(self, left, right):
        Sentence.validate(left)
        Sentence.validate(right)
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (isinstance(other, Biconditional) and
                self.left == other.left and
                self.right == other.right)

    def __hash__(self):
        return hash(("biconditional", hash(self.left), hash(self.right)))

    def __repr__(self):
        return f"Biconditional({repr(self.left)}, {repr(self.right)})"

    def evaluate(self, model):
        return self.left.evaluation(model) == self.right.evaluate(model)
        # return (self.left.evaluate(model) and self.right.evaluate(model)) or (not self.left.evaluate(model) and not self.right.evaluate(model))

    def formula(self):
        left_formula = Sentence.parenthesize(self.left.formula())
        right_formula = Sentence.parenthesize(self.right.formula())
        return f"{left_formula} ↔ {right_formula}"
    
    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())
    
def model_check(knowledge, query):
    """Checks if knowledge base entails query. """

    def check_all(knowledge, query, symbols, model):
        """ Checks if knowledge base entails query, given a particular model."""
        # If model has an assignment for each symbol
        if not symbols:

            # If knowledge base is true in model, then query must also be true
            if knowledge.evaluate(model):
                return query.evaluate(model)
            return True
        else:

            # Choose one the remaining unused symbols
            remaining = symbols.copy()
            p = remaining.pop()

            # Create a model where the symbol is true
            model_true = model.copy()
            model_true[p] = True

            # Create a model where the symbol is false
            model_false = model.copy()
            model_false[p] = False

            # Ensure entailment holds in both models
            return (check_all(knowledge, query, remaining, model_true) and 
                    check_all(knowledge, query, remaining, model_false))
        
    # Get all symbols in both knowledge and query
    symbols = set.union(knowledge.symbols(), query.symbols())

    # Check that knowledge entails query
    return check_all(knowledge, query, symbols, dict())