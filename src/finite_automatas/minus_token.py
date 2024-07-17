from src.finite_automata import FiniteAutomata

minus_token = FiniteAutomata(
    ['q0', 'q1'],
    ['-'],
    {'q0': {'-': 'q1'}},
    'q0',
    ['q1'],
)
