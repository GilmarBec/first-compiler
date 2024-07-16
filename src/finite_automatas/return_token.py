from src.finite_automata import FiniteAutomata

return_token = FiniteAutomata(
    ['q0', 'q1', 'q2'],
    ['return'],
    {'q0': {'return': 'q1'}, 'q2': {'return': 'q2'}, 'q1': {'return': 'q2'}},
    'q0',
    ['q1'],
)
