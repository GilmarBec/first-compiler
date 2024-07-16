from src.finite_automata import FiniteAutomata

def_token = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    ['def'],
    {'q2': {'def': 'q2'}, 'q1': {'def': 'q2'}, 'q0': {'def': 'q1'}},
    'q0',
    ['q1'],
)
