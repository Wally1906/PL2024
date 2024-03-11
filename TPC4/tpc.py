from ply import lex, yacc
import sys

tokens = [
    "SELECT",
    "FROM",
    "WHERE",
    "PLUS",
    "MINUS",
    "MULT",
    "DIV",
    "MEQUAL",
    "LEQUAL",
    "EQUAL",
    "MORE",
    "LESS",
    "COMANDO",
    "ATRIBUTO",
    "DELIMITADOR",
    "NR",
    "FINAL"
]
t_SELECT = "select"

t_FROM = "from"

t_WHERE = "where"

t_PLUS = r'\+'

t_MINUS = r'\-'

t_MULT = r'\*'

t_DIV = r'/'

t_MEQUAL = r'>='

t_LEQUAL = r'<='

t_MORE = r'>'

t_LESS = r'<'

t_EQUAL = r'>='

t_DELIMITADOR = r','

t_NR = r'\d+(\.'

t_FINAL = r';'


def t_COMANDO(t):
    r"\b[a-zA-Z]+\b"
    if reserved.get(t.value.lower()):
        t.type = "COMANDO"
    else:
        t.type = "ATRIBUTO"
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def main (args):
    if len(args) < 2:
        return
    with open(args[1], 'r') as file:
        data = file.read()
        lexer = lex.lex() 
        lexer.input(data)
        for tok in lexer:
            print(tok) 

if __name__ == '__main__':
    main(args=sys.argv)
