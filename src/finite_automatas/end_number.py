
from src.finite_automata import FiniteAutomata

end_number = FiniteAutomata(
    ['q0', 'q1'],
    ['\\d', '\\w'],
    {'q0': {'\\d': 'q1', '\\w': 'q0'}, 'q1': {'\\w': 'q0', '\\d': 'q1'}},
    'q0',
    ['q1'],
)
    