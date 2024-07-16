from src.finite_automata import FiniteAutomata

print_token = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    ['print'],
    {'q2': {'print': 'q2'}, 'q1': {'print': 'q2'}, 'q0': {'print': 'q1'}},
    'q0',
    ['q1'],
)
