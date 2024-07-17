from src.finite_automata import FiniteAutomata

int_token = FiniteAutomata(
    ['q0', 'q1', 'q2', 'q3'],
    ['i', 'n', 't'],
    {'q0': {'i': 'q1'}, 'q2': {'t': 'q3'}, 'q1': {'n': 'q2'}},
    'q0',
    ['q3'],
)
