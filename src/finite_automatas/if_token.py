from src.finite_automata import FiniteAutomata

if_token = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    ['if'],
    {'q1': {'if': 'q2'}, 'q0': {'if': 'q1'}, 'q2': {'if': 'q2'}},
    'q0',
    ['q1'],
)
