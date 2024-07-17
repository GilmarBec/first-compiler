from src.finite_automata import FiniteAutomata

close_parentheses_token = FiniteAutomata(
    ['q0', 'q1'],
    [')'],
    {'q0': {')': 'q1'}},
    'q0',
    ['q1'],
)
