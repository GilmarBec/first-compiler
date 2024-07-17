from src.finite_automata import FiniteAutomata

open_parentheses_token = FiniteAutomata(
    ['q0', 'q1'],
    ['('],
    {'q0': {'(': 'q1'}},
    'q0',
    ['q1'],
)
