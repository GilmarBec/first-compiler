from src.finite_automata import FiniteAutomata

else_token = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    ['else'],
    {'q2': {'else': 'q2'}, 'q1': {'else': 'q2'}, 'q0': {'else': 'q1'}},
    'q0',
    ['q1'],
)
