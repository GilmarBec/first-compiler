from src.finite_automatas.close_braces_token import close_braces_token
from src.finite_automatas.close_parentheses_token import close_parentheses_token
from src.finite_automatas.comma_token import comma_token
from src.finite_automatas.def_token import def_token
from src.finite_automatas.equal_equal_token import equal_equal_token
from src.finite_automatas.equal_token import equal_token
from src.finite_automatas.greater_token import greater_token
from src.finite_automatas.id_open_parentheses_token import id_open_parentheses_token
from src.finite_automatas.id_token import id_token
from src.finite_automatas.if_token import if_token
from src.finite_automatas.int_token import int_token
from src.finite_automatas.less_token import less_token
from src.finite_automatas.minus_token import minus_token
from src.finite_automatas.multiplication_token import multiplication_token
from src.finite_automatas.number_token import number_token
from src.finite_automatas.open_braces_token import open_braces_token
from src.finite_automatas.open_parentheses_token import open_parentheses_token
from src.finite_automatas.plus_token import plus_token
from src.finite_automatas.print_token import print_token
from src.finite_automatas.return_token import return_token
from src.finite_automatas.semicolon_token import semicolon_token

# fa, token_name, priority
finite_automatas_translator = [
    (close_braces_token, 'CLOSE_BRACES_TOKEN', 1),
    (close_parentheses_token, 'CLOSE_PARENTHESES_TOKEN', 1),
    (comma_token, 'COMMA_TOKEN', 1),
    (def_token, 'DEF_TOKEN', 1),
    (equal_equal_token, 'EQUAL_EQUAL_TOKEN', 1),
    (equal_token, 'EQUAL_TOKEN', 1),
    (greater_token, 'GREATER_TOKEN', 1),
    (id_open_parentheses_token, 'ID_OPEN_PARENTHESES_TOKEN', 0),
    (id_token, 'ID_TOKEN', 0),
    (if_token, 'IF_TOKEN', 1),
    (int_token, 'INT_TOKEN', 1),
    (less_token, 'LESS_TOKEN', 1),
    (minus_token, 'MINUS_TOKEN', 1),
    (multiplication_token, 'MULTIPLICATION_TOKEN', 1),
    (number_token, 'NUMBER_TOKEN', 1),
    (open_braces_token, 'OPEN_BRACES_TOKEN', 1),
    (open_parentheses_token, 'OPEN_PARENTHESES_TOKEN', 1),
    (plus_token, 'PLUS_TOKEN', 1),
    (print_token, 'PRINT_TOKEN', 1),
    (return_token, 'RETURN_TOKEN', 1),
    (semicolon_token, 'SEMICOLON_TOKEN', 1),
]

ll1 = {
    'MAIN': {
        '$': 'MAIN -> ε',
        'ε': 'MAIN -> FLIST',
        'def': 'MAIN -> FLIST',
        'id': 'MAIN -> STMT',
        '{': 'MAIN -> STMT',
        'int': 'MAIN -> STMT',
        ';': 'MAIN -> STMT',
        'print': 'MAIN -> STMT',
        'return': 'MAIN -> STMT',
        'if': 'MAIN -> STMT',
    },
    'FLIST': {
        'def': 'FLIST -> FDEF FLIST2',
    },
    'FLIST2': {
        '$': 'FLIST2 -> ε',
        'def': 'FLIST2 -> FDEF FLIST2',
    },
    'FDEF': {
        'def': 'FDEF -> def id(PARLIST){STMTLIST}',
    },
    'PARLIST': {
        ')': 'PARLIST -> ε',
        'int': 'PARLIST -> int id PARLIST2',
    },
    'PARLIST2': {
        ')': 'PARLIST2 -> ε',
        ',': 'PARLIST2 -> , PARLIST2',
    },
    'STMT': {
        'id': 'STMT -> ATRIBST;',
        '{': 'STMT -> {STMTLIST}',
        'int': 'STMT -> int id;',
        ';': 'STMT -> ;',
        'print': 'STMT -> PRINTST;',
        'return': 'STMT -> RETURNST;',
        'if': 'STMT -> IFSTMT',
    },
    'ATRIBST': {
        'id': 'ATRIBST -> id = ATRIBST2',
    },
    'ATRIBST2': {
        'id': 'ATRIBST2 -> EXPR',
        '(': 'ATRIBST2 -> EXPR',
        'id(': 'ATRIBST2 -> FCALL',
        'num': 'ATRIBST2 -> EXPR',
    },
    'FCALL': {
        'id(': 'FCALL -> id(PARLISTCALL)',
    },
    'PARLISTCALL': {
        'id': 'PARLISTCALL -> id PARLISTCALL2',
        ')': 'PARLISTCALL -> ε',
    },
    'PARLISTCALL2': {
        ')': 'PARLISTCALL2 -> ε',
        ',': 'PARLISTCALL2 -> , PARLISTCALL2',
    },
    'PRINTST': {
        'print': 'PRINTST -> print EXPR',
    },
    'RETURNST': {
        'return': 'RETURNST -> return'
    },
    'IFSTMT': {
        'if': 'IFSTMT -> if(EXPR) STMT else STMT',
        'if': 'IFSTMT -> if(EXPR) STMT',
    },
    'STMTLIST': {
        'id': 'STMTLIST -> STMT STMTLIST2',
        '{': 'STMTLIST -> STMT STMTLIST2',
        'int': 'STMTLIST -> STMT STMTLIST2',
        ';': 'STMTLIST -> STMT STMTLIST2',
        'print': 'STMTLIST -> STMT STMTLIST2',
        'return': 'STMTLIST -> STMT STMTLIST2',
        'if': 'STMTLIST -> STMT STMTLIST2',
    },
    'STMTLIST2': {
        'ε': 'STMTLIST2 -> ε',
        'id': 'STMTLIST2 -> STMT STMTLIST2',
        '{': 'STMTLIST2 -> STMT STMTLIST2',
        '}': 'STMTLIST2 ->  ε',
        'int': 'STMTLIST2 -> STMT STMTLIST2',
        ';': 'STMTLIST2 -> STMT STMTLIST2',
        'print': 'STMTLIST2 -> STMT STMTLIST2',
        'return': 'STMTLIST2 -> STMT STMTLIST2',
        'if': 'STMTLIST2 -> STMT STMTLIST2',
    },
    'EXPR': {
        'id': 'EXPR -> NUMEXPR EXPR2',
        '(': 'EXPR -> NUMEXPR EXPR2',
        'num': 'EXPR -> NUMEXPR EXPR2',
    },
    'EXPR2': {
        ')': 'EXPR2-> ε',
        ';': 'EXPR2-> ε',
        '<': 'EXPR2-> < NUMEXPR',
        '>': 'EXPR2-> > NUMEXPR',
        '==': 'EXPR2-> == NUMEXPR',
    },
    'NUMEXPR': {
        'id': 'NUMEXPR -> TERM NUMEXPR2',
        '(': 'NUMEXPR -> TERM NUMEXPR2',
        'num': 'NUMEXPR -> TERM NUMEXPR2',
    },
    'NUMEXPR2': {
        ')': 'NUMEXPR2 -> ε',
        ';': 'NUMEXPR2 -> ε',
        '<': 'NUMEXPR2 -> ε',
        '>': 'NUMEXPR2 -> ε',
        '==': 'NUMEXPR2 -> ε',
        '+': 'NUMEXPR2 -> + TERM NUMEXPR2',
        '-': 'NUMEXPR2 -> - TERM NUMEXPR2',
    },
    'TERM': {
        'id': 'TERM -> FACTOR TERM2',
        '(': 'TERM -> FACTOR TERM2',
        'num': 'TERM -> FACTOR TERM2',
    },
    'TERM2': {
        ')': 'TERM2 -> ε',
        ';': 'TERM2 -> ε',
        '<': 'TERM2 -> ε',
        '>': 'TERM2 -> ε',
        '==': 'TERM2 -> ε',
        '+': 'TERM2 -> ε',
        '-': 'TERM2 -> ε',
        '*': 'TERM2 -> *FACTOR TERM2',
    },
    'FACTOR': {
        'id': 'FACTOR -> id',
        '(': 'FACTOR -> (NUMEXPR)',
        'num': 'FACTOR -> num',
    }
}
