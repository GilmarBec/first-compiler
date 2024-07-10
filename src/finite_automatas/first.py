
from src.finite_automata import FiniteAutomata

first = FiniteAutomata(
    ['q1', 'q2'],
    ['1', '0'],
    {'q1': {'0': 'q1', '1': 'q2'}, 'q2': {'1': 'q2', '0': 'q1'}},
    'q1',
    ['q2'],
)
    