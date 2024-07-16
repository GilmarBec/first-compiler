from src.finite_automata import FiniteAutomata

equal_equal_token = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    ['=', '=='],
    {'q2': {'==': 'q2'}, 'q1': {'==': 'q2'}, 'q0': {'=': 'q1'}},
    'q0',
    ['q1'],
)
