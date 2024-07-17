from src.finite_automata import FiniteAutomata

print_token = FiniteAutomata(
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5'],
    ['i', 'n', 'p', 'r', 't'],
    {'q3': {'n': 'q4'}, 'q2': {'i': 'q3'}, 'q1': {'r': 'q2'}, 'q0': {'p': 'q1'}, 'q4': {'t': 'q5'}},
    'q0',
    ['q5'],
)
