from src.tokenizator import Token

ll1 = {
    'MAIN': {
        '$': [],
        'DEF_TOKEN': ['FLIST'],
        'ID_TOKEN': ['STMT'],
        'OPEN_BRACES_TOKEN': ['STMT'],
        'INT_TOKEN': ['STMT'],
        'SEMICOLON_TOKEN': ['STMT'],
        'PRINT_TOKEN': ['STMT'],
        'RETURN_TOKEN': ['STMT'],
        'IF_TOKEN': ['STMT'],
    },
    'FLIST': {
        'DEF_TOKEN': ['FDEF', 'FLIST2'],
    },
    'FLIST2': {
        '$': [],
        'DEF_TOKEN': ['FDEF', 'FLIST2'],
    },
    'FDEF': {
        'DEF_TOKEN': ['DEF_TOKEN', 'ID_OPEN_PARENTHESES_TOKEN', 'PARLIST', 'CLOSE_PARENTHESES_TOKEN', 'OPEN_BRACES_TOKEN', 'STMTLIST', 'CLOSE_BRACES_TOKEN'],
    },
    'PARLIST': {
        'CLOSE_PARENTHESES_TOKEN': [],
        'INT_TOKEN': ['INT_TOKEN', 'ID_TOKEN', 'PARLIST2'],
    },
    'PARLIST2': {
        'CLOSE_PARENTHESES_TOKEN': [],
        'COMMA_TOKEN': ['COMMA_TOKEN', 'PARLIST'],
    },
    'STMT': {
        'ID_TOKEN': ['ATRIBST', 'SEMICOLON_TOKEN'],
        'OPEN_BRACES_TOKEN': ['OPEN_BRACES_TOKEN', 'STMTLIST', 'CLOSE_BRACES_TOKEN'],
        'INT_TOKEN': ['INT_TOKEN', 'ID_TOKEN', 'SEMICOLON_TOKEN'],
        'SEMICOLON_TOKEN': ['SEMICOLON_TOKEN'],
        'PRINT_TOKEN': ['PRINTST', 'SEMICOLON_TOKEN'],
        'RETURN_TOKEN': ['RETURNST', 'SEMICOLON_TOKEN'],
        'IF_TOKEN': ['IFSTMT'],
    },
    'ATRIBST': {
        'ID_TOKEN': ['ID_TOKEN', 'EQUAL_TOKEN', 'ATRIBST2'],
    },
    'ATRIBST2': {
        'ID_TOKEN': ['EXPR'],
        'OPEN_PARENTHESES_TOKEN': ['EXPR'],
        'ID_OPEN_PARENTHESES_TOKEN': ['FCALL'],
        'NUMBER_TOKEN': ['EXPR'],
    },
    'FCALL': {
        'ID_OPEN_PARENTHESES_TOKEN': ['ID_OPEN_PARENTHESES_TOKEN', 'PARLISTCALL', 'CLOSE_PARENTHESES_TOKEN'],
    },
    'PARLISTCALL': {
        'ID_TOKEN': ['ID_TOKEN', 'PARLISTCALL2'],
        'CLOSE_PARENTHESES_TOKEN': [],
    },
    'PARLISTCALL2': {
        'CLOSE_PARENTHESES_TOKEN': [],
        'COMMA_TOKEN': ['COMMA_TOKEN', 'PARLISTCALL'],
    },
    'PRINTST': {
        'PRINT_TOKEN': ['PRINT_TOKEN', 'EXPR'],
    },
    'RETURNST': {
        'RETURN_TOKEN': ['RETURN_TOKEN'],
    },
    'IFSTMT': {
        'IF_TOKEN': ['IF_TOKEN', 'OPEN_PARENTHESES_TOKEN', 'EXPR', 'CLOSE_PARENTHESES_TOKEN', 'STMT', 'ELSE_TOKEN', 'STMT'],
        # 'IF_TOKEN': ['IF_TOKEN', 'OPEN_PARENTHESES_TOKEN', 'EXPR', 'CLOSE_PARENTHESES_TOKEN', 'STMT'],
    },
    'STMTLIST': {
        'ID_TOKEN': ['STMT', 'STMTLIST2'],
        'OPEN_BRACES_TOKEN': ['STMT', 'STMTLIST2'],
        'INT_TOKEN': ['STMT', 'STMTLIST2'],
        'SEMICOLON_TOKEN': ['STMT', 'STMTLIST2'],
        'PRINT_TOKEN': ['STMT', 'STMTLIST2'],
        'RETURN_TOKEN': ['STMT', 'STMTLIST2'],
        'IF_TOKEN': ['STMT', 'STMTLIST2'],
    },
    'STMTLIST2': {
        'CLOSE_BRACES_TOKEN': [],
        'ID_TOKEN': ['STMT', 'STMTLIST2'],
        'OPEN_BRACES_TOKEN': ['STMT', 'STMTLIST2'],
        'INT_TOKEN': ['STMT', 'STMTLIST2'],
        'SEMICOLON_TOKEN': ['STMT', 'STMTLIST2'],
        'PRINT_TOKEN': ['STMT', 'STMTLIST2'],
        'RETURN_TOKEN': ['STMT', 'STMTLIST2'],
        'IF_TOKEN': ['STMT', 'STMTLIST2'],
    },
    'EXPR': {
        'ID_TOKEN': ['NUMEXPR', 'EXPR2'],
        'OPEN_PARENTHESES_TOKEN': ['NUMEXPR', 'EXPR2'],
        'NUMBER_TOKEN': ['NUMEXPR', 'EXPR2'],
    },
    'EXPR2': {
        'CLOSE_PARENTHESES_TOKEN': [],
        'SEMICOLON_TOKEN': [],
        'LESS_TOKEN': ['LESS_TOKEN', 'NUMEXPR'],
        'GREATER_TOKEN': ['GREATER_TOKEN', 'NUMEXPR'],
        'EQUAL_EQUAL_TOKEN': ['EQUAL_EQUAL_TOKEN', 'NUMEXPR'],
    },
    'NUMEXPR': {
        'ID_TOKEN': ['TERM', 'NUMEXPR2'],
        'OPEN_PARENTHESES_TOKEN': ['TERM', 'NUMEXPR2'],
        'NUMBER_TOKEN': ['TERM', 'NUMEXPR2'],
    },
    'NUMEXPR2': {
        'CLOSE_PARENTHESES_TOKEN': [],
        'SEMICOLON_TOKEN': [],
        'LESS_TOKEN': [],
        'GREATER_TOKEN': [],
        'EQUAL_EQUAL_TOKEN': [],
        'PLUS_TOKEN': ['PLUS_TOKEN', 'TERM', 'NUMEXPR2'],
        'MINUS_TOKEN': ['MINUS_TOKEN', 'TERM', 'NUMEXPR2'],
    },
    'TERM': {
        'ID_TOKEN': ['FACTOR', 'TERM2'],
        'OPEN_PARENTHESES_TOKEN': ['FACTOR', 'TERM2'],
        'NUMBER_TOKEN': ['FACTOR', 'TERM2'],
    },
    'TERM2': {
        'CLOSE_PARENTHESES_TOKEN': [],
        'SEMICOLON_TOKEN': [],
        'LESS_TOKEN': [],
        'GREATER_TOKEN': [],
        'EQUAL_EQUAL_TOKEN': [],
        'PLUS_TOKEN': [],
        'MINUS_TOKEN': [],
        'MULTIPLICATION_TOKEN': ['MULTIPLICATION_TOKEN', 'FACTOR', 'TERM2'],
    },
    'FACTOR': {
        'ID_TOKEN': ['ID_TOKEN'],
        'OPEN_PARENTHESES_TOKEN': ['OPEN_PARENTHESES_TOKEN', 'NUMEXPR', 'CLOSE_PARENTHESES_TOKEN'],
        'NUMBER_TOKEN': ['NUMBER_TOKEN'],
    }
}


def parse(input_tokens: [Token or str], stack=None):
    if stack is None:
        stack = ['MAIN', '$']

    input_tokens.append(Token('$', '$'))

    while stack[0] != '$':
        if stack[0] == input_tokens[0].type:
            print('Match found:', input_tokens[0])
            stack.pop(0)
            input_tokens.pop(0)
        elif stack[0] not in ll1.keys():
            error_msg = f"Expected: {stack[0]} gotten {input_tokens[0]}"
            print(error_msg)
            raise ValueError(error_msg)
        elif input_tokens[0].type not in ll1[stack[0]].keys():
            error_msg = (f"\n\nProduction not found, {stack[0]} -> {input_tokens[0].type}\n"
                         f"Expected: {stack[0]} -> {' | '.join(ll1[stack[0]].keys())}\n"
                         f"Gotten: {input_tokens[0]}")
            print(error_msg)
            raise ValueError(error_msg)
        else:
            next_not_terminal = stack.pop(0)
            if next_not_terminal == 'IFSTMT':
                cases = (
                    ['IF_TOKEN', 'OPEN_PARENTHESES_TOKEN', 'EXPR', 'CLOSE_PARENTHESES_TOKEN', 'STMT', 'ELSE_TOKEN', 'STMT'],
                    ['IF_TOKEN', 'OPEN_PARENTHESES_TOKEN', 'EXPR', 'CLOSE_PARENTHESES_TOKEN', 'STMT'],
                )

                try:
                    print(f'trying to add to stack {next_not_terminal} -> {' '.join(cases[0])}')
                    return parse([Token(x.type, x.value) for x in input_tokens], cases[0] + stack)
                except ValueError:
                    print(f'trying to add to stack {next_not_terminal} -> {' '.join(cases[1])}')
                    return parse(input_tokens, cases[1] + stack)

            to_add_to_stack = ll1[next_not_terminal][input_tokens[0].type]
            print(f'Add 2 stack: {next_not_terminal} -> {' '.join(to_add_to_stack) if to_add_to_stack != [] else 'ε'}')
            stack = to_add_to_stack + stack

    return input_tokens[0].type == '$'
