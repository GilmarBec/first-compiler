from src.finite_automata import FiniteAutomata

open_braces_token = FiniteAutomata(
    ['q0', 'q1'],
    ['{'],
    {'q0': {'{': 'q1'}},
    'q0',
    ['q1'],
)
