class FiniteAutomata:
    def __init__(self, states: [str], alphabet: [str], activation_function: dict,
                 initial_state: str, final_states: [str]):

        self.states = states
        self.alphabet = alphabet
        self.activation_function = activation_function
        self.initial_state = initial_state
        self.final_states = final_states

    def execute(self, _input: str) -> bool:  # Python has input as a build-in function >:P
        # Verify all input is on alphabet
        for char in set(_input):  # Using set to get only unique chars
            if self.alphabet_match(char) is None:
                print(f'Input has chars outside of alphabet {self.alphabet}, character {char}')
                return False

        current_state = self.initial_state
        buffer = ''
        for char in _input:
            buffer += char
            next_state = self.get_next_state(current_state, buffer)

            # String not in a possible state, soo add more chars to buffer
            if not next_state:
                continue

            buffer = ''
            current_state = next_state

        return current_state in self.final_states

    def get_next_state(self, current_state: str, _input: str) -> str or None or False:
        expr = self.alphabet_match(_input)
        if expr is None:
            return None

        next_state = self.activation_function[current_state][expr]
        if next_state is None:
            # raise ValueError(f'Invalid state: {current_state} -> {next_state}')
            return False

        return next_state

    def alphabet_match(self, _input: str) -> str or None:
        for expr in self.alphabet:
            if expr == _input:
                return expr

        return None
