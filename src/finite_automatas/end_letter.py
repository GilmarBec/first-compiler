
from src.finite_automata import FiniteAutomata

end_letter = FiniteAutomata(
    ['q0', 'q1'],
    ['\\w', '\\d'],
    {'q0': {'\\d': 'q1'}, 'q1': {'\\w': 'q0'}},
    'q0',
    ['q1'],
)
    