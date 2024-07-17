from src.finite_automata import FiniteAutomata

return_token = FiniteAutomata(
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'],
    ['e', 'n', 'r', 't', 'u'],
    {'q3': {'u': 'q4'}, 'q5': {'n': 'q6'}, 'q0': {'r': 'q1'}, 'q2': {'t': 'q3'}, 'q1': {'e': 'q2'}, 'q4': {'r': 'q5'}},
    'q0',
    ['q6'],
)
