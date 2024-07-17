from src.finite_automata import FiniteAutomata

less_token = FiniteAutomata(
    ['q0', 'q1'],
    ['<'],
    {'q0': {'<': 'q1'}},
    'q0',
    ['q1'],
)
