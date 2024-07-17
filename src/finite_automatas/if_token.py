from src.finite_automata import FiniteAutomata

if_token = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    ['f', 'i'],
    {'q0': {'i': 'q1'}, 'q1': {'f': 'q2'}},
    'q0',
    ['q2'],
)
