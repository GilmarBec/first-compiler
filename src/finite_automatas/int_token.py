from src.finite_automata import FiniteAutomata

int_token = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    ['int', '}'],
    {'q1': {'int': 'q2'}, 'q0': {'int': 'q1'}, 'q2': {'}': 'q2'}},
    'q0',
    ['q1'],
)
