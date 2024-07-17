from src.finite_automata import FiniteAutomata

def_token = FiniteAutomata(
    ['q0', 'q1', 'q2', 'q3'],
    ['d', 'e', 'f'],
    {'q0': {'d': 'q1'}, 'q1': {'e': 'q2'}, 'q2': {'f': 'q3'}},
    'q0',
    ['q3'],
)
