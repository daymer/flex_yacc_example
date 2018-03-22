import ply.lex as lex
import ply.yacc as yacc
import logging
from datetime import datetime


log_to_file = False
log_level = 'INFO'
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger_inst = logging.getLogger()
logger_inst.setLevel(log_level)
if log_to_file is True:
    log_name = "main_" + str(datetime.now().strftime("%Y-%m-%d_%H_%M_%S")) + '_v0.1.log'
    fh = logging.FileHandler(log_name)
    fh.setLevel(log_level)
    fh.setFormatter(formatter)
    logger_inst.addHandler(fh)
ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.setFormatter(formatter)
logger_inst.addHandler(ch)

logger_inst.info('Main process has been initialized')
##############################################################

# List of token names.
tokens = (
    'NAME',
    'NUMBER',
    'PLUS',
    'MINUS',
    'SMALL',
    'LARGE',
    'EQUAL',
    'EQUALS',
    'WHILEE',
    'DOO',
    'FLOAT'
)

# Regular expression rules for simple tokens
t_WHILEE = r'while'
t_DOO = r'do'
t_EQUALS = r'\:\='
t_SMALL = r'<'
t_LARGE = r'>'
t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'-'
t_NAME = r'\w'
t_NUMBER = r'\d'
t_ignore = " \t"
t_FLOAT = r'\d+.\d+'

# A regular expression rules with some action code


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Error handling rule

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


# ====================================================


def p_S(p):
    'siska : kiska'
    print('S, 9 pravilo')


def p_if_statement_2(p):
    '''kiska : WHILEE statement DOO expression EQUALS comparision
             | expression EQUALS comparision'''
    # print('debug p_if_statement_2', p[1], p[2], p[3])
    try:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
        print('F, 8 pravilo', p[0])
    except:
        p[0] = (p[1], p[2], p[3])
        print('F, 7 pravilo', p[0])


def p_if_statement(p):
    '''statement : comparision SMALL comparision
                 | comparision LARGE comparision
                 | comparision EQUAL comparision'''
    #   print('debug p_if_statement', p[1], p[2], p[3])
    if p[2] == '<':
        p[0] = (p[1], p[2], p[3])
        print('T, 6 pravilo', p[0])
    if p[2] == '>':
        p[0] = (p[1], p[2], p[3])
        print('T, 5 pravilo')
    if p[2] == '=':
        p[0] = (p[1], p[2], p[3])
        print('T, 4 pravilo')


def p_comparision(p):
    '''
    comparision : comparision PLUS expression
                   | comparision MINUS expression
                   | expression
    '''
    #    print('debug p_comparision', p[1])
    try:
        if p[2] == '+':
            p[0] = (p[1], p[2], p[3])
            print('E, 3 pravilo', p[0])
        if p[2] == '-':
            p[0] = (p[1], p[2], p[3])
            print('E, 2 pravilo', p[0])
    except:
        p[0] = p[1]
        print('E, 1 pravilo', p[0])


def p_var(p):
    '''expression : NAME'''
    #   print('debug p_var', p[1])
    p[0] = p[1]


def p_num(p):
    '''expression : NUMBER'''
    #  print('debug p_num', p[1])
    p[0] = p[1]


def p_float(p):
    '''expression : FLOAT'''
    #print('debug p_FLOAT', p[1])
    p[0] = p[1]


parser = yacc.yacc(debug=False)
# =====================================
string_to_parse = 'while f<c do b:=10.5+1'
parser.parse(string_to_parse)
