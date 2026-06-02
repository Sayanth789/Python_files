'''
For Complicated Gammars we can use Prsing tools such as
PLY or PyParsing 


'''

from ply import lex 
from ply.yacc import yacc 


tokens = [ 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN' ]

# Ignored characters 
t_ignore = ' \t\n'

# Token  Specifications (as regexs)
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Token processing functions 
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling 
def t_error(t):
    print(f"Bad character: {t.value[0]!r}")
    t.lexer.skip(1)

# Build the lexer 
lexer = lex.lex()

# Grammar rules and handler functions 
def p_expr(p):
    '''
     expr : expr PLUS term
          | expr MINUS term
    '''

    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expr_term(p):
    '''   
    expr : term
    '''        
    p[0] = p[1]

def p_term(p):
    '''    
    term : term TIMES factor 
         | term DIVIDE factor
    '''    
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def  p_term_factor(p):
    '''   
    term : factor
    '''          
    p[0] = p[1]

def p_factor(p):
    '''   
    factor : NUM
    '''    

    p[0] = p[1]

def p_factor_group(p):
    '''   
    factor : LPAREN expr RPAREN
    '''  
    p[0] = p[2]

def p_error(p):
    print('Syntax error')

parser = yacc()        


print(parser.parse("22 * 3 + 5"))
print(parser.parse('2+(3+4)*5'))
result = parser.parse("2 + 3 * 4")
print(result)

'''  
Check ::::: python’s own ast module is also worth a look.
'''