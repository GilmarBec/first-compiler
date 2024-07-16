from src.finite_automata import FiniteAutomata

close_parentheses = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    [')'],
    {'q1': {')': 'q2'}, 'q2': {')': 'q2'}, 'q0': {')': 'q1'}},
    'q0',
    ['q1'],
)
