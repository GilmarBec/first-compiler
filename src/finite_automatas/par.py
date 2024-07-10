
from src.finite_automata import FiniteAutomata

par = FiniteAutomata(
    ['q0', 'q1'],
    ['0', '1'],
    {'q0': {'0': 'q1', '1': 'q1'}, 'q1': {'0': 'q0', '1': 'q0'}},
    'q0',
    ['q0'],
)
    