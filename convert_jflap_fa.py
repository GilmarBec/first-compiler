# python3 convert_jflap_fa.py 'jflap/first.jff' 'first'

import sys
import xmltodict


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) < 1:
        raise 'Jflap File path not given (arg 1)'
    if len(args) < 2:
        raise 'Automata unique name not given (arg 2)'

    filename = args[0]
    automata_name = args[1].replace(' ', '_')

    file = open(filename, "r")
    xml_dict = xmltodict.parse(file.read(), force_list=('initial', 'final'))
    file.close()

    # print(xml_dict['structure']['automaton'])
    # raise ':P'

    if xml_dict['structure']['type'] != 'fa':
        raise 'Converter only works with Jflap FA files'

    xml_state = xml_dict['structure']['automaton']['state']
    xml_transitions = xml_dict['structure']['automaton']['transition']
    if 'note' in xml_dict['structure']['automaton'].keys():
        xml_note = xml_dict['structure']['automaton']['note']

    states = []
    id_to_state = {}
    initial_state = None
    final_states = []
    for state in xml_dict['structure']['automaton']['state']:
        states.append(state['@name'])
        id_to_state[state['@id']] = state['@name']

        if 'initial' in state.keys():
            initial_state = state['@name']

        if 'final' in state.keys():
            final_states.append(state['@name'])

    alphabeth_set = set()
    activation_function = {}
    for transition in xml_transitions:
        from_state = id_to_state[transition['from']]
        to_state = id_to_state[transition['to']]
        value_received = transition['read']

        alphabeth_set.add(value_received)

        if from_state not in activation_function.keys():
            activation_function[from_state] = {}

        activation_function[from_state][value_received] = to_state

    alphabeth = list(alphabeth_set)

    file = open(f'src/finite_automatas/{automata_name}.py', mode='w')
    file.write(f"""
from src.finite_automata import FiniteAutomata

{automata_name} = FiniteAutomata(
    {states},
    {alphabeth},
    {activation_function},
    '{initial_state}',
    {final_states},
)
    """)

    print('JFile sucessfully converted!  ˆ𐃷ˆ')
