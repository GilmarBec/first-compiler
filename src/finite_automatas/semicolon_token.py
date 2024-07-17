from src.finite_automata import FiniteAutomata

semicolon_token = FiniteAutomata(
    ['q0', 'q1'],
    [';'],
    {'q0': {';': 'q1'}},
    'q0',
    ['q1'],
)
