
from src.finite_automata import FiniteAutomata

substring_11 = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    ['1', '0'],
    {'q2': {'0': 'q2', '1': 'q2'}, 'q0': {'0': 'q0', '1': 'q1'}, 'q1': {'1': 'q2', '0': 'q0'}},
    'q0',
    ['q2'],
)
    