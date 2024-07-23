from src.finite_automata import FiniteAutomata

else_token = FiniteAutomata(
    ['q0', 'q1', 'q2', 'q3', 'q4'],
    ['e', 'l', 's'],
    {'q0': {'e': 'q1'}, 'q2': {'s': 'q3'}, 'q3': {'e': 'q4'}, 'q1': {'l': 'q2'}},
    'q0',
    ['q4'],
)
