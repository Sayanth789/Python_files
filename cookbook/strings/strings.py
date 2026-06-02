# splitting strings on Any of Multiple Delimiters 

'''
Need to split a string into fields, but delimeters (and spacing around'em) aren't 
consistent throughout the string.

> 
'''

# line = 'asdf fdjk; afed, fdek,asdf,        foo'
# import re 
# new_line = re.split(r'[;,\s]\s*', line)
# print(new_line)



# Matching Text at the Start or End of a String 

# maybe filename or extension etc..

# filename = 'spam.txt'
# print(filename.endswith('.txt'))

# print(filename.startswith('file:'))

# url = "http://www.python.org"
# print(url.startswith('http:'))

# fact = "My name is sayanth"
# print(fact.endswith('sayanth'))

'''  The startswith() and endswith() methods provide a very convenient way to perform
basic prefix and suffix checking.


'''

# Matching Strings Using Shell Wildcard Patterns 
''' To match  text using same widlcard patterns as are commonly used 
when in Unix  shells eg: *.py, Dat[0-9]*.csv, etc

* The fnmatch module provides two functions—fnmatch() and fnmatchcase()—that
can be used to perform such matching.
'''

# from fnmatch import fnmatch, fnmatchcase

# print(fnmatch('foo.txt', '*.txt'))


# check = fnmatch('Dat45.csv', 'Dat[0-9]*')
# print(check)

# names = ['Dat1.csv', 'Dat2.csv', 'Config.ini', 'foo.py']
# print([name for name in names if fnmatch(name, 'Dat*.csv')])


''' 
Searching and replacing Text patterns in string
'''

# text = 'yeah, but no, but yeah, but no, but yeah'

# print(text.replace('yeah', 'yep'))

# For more complicated patterns we use sub() for re method 
# text = 'Today is 11/27/2012. Python starts 3/12/2013.'

# import re 
# print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# will change to 2012-11-27.


'''  
For more complicated substitutions, it’s possible to specify a substitution callback func‐
tion instead. For example:
'''
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# print(datepat.sub(r'\3-\1-\2', text))



# from calendar import month_abbr 
# def change_date(m):
#     mon_name = month_abbr[int(m.group(1))]
#     return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


# print(datepat.sub(change_date, text))


''' Searching and Replacing Case-Insensitive Text
<>You need to search for and possibly replace text in a case-insensitive manner.

'''
# import re
# text = "UPPER PYTHON, lower python , Mixed Python"
# print(re.findall('python', text, flags=re.IGNORECASE))

# print(re.sub('python', 'Language', text, flags=re.IGNORECASE))

''' 
To match the case of replaced text:

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
          return word.upper()
        elif text.islower():
          return word.lower()
        elif text[0].isupper():
          return word.capitalize()
        else:
          return word
    return replace              

re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
'''

# Normalizing Unicode Text to a Standard Representation
''' 
You’re working with Unicode strings, but need to make sure that all of the strings have
the same underlying representation.

In Unicode, certain characters can be represented by more than one valid sequence of
code points. To illustrate, consider the following example:
'''

# s1 = 'Spicy Jalape\u00f1o'
# s2 = 'Spicy Jalapen\u0303o'
# print(s1 == s2)
# print(len(s1))
# print(len(s2))

'''  
Having multiple representations is a problem for programs that compare strings. In
order to fix this, you should first normalize the text into a standard representation using
the unicodedata module:
'''

# import unicodedata 

# t1 = unicodedata.normalize('NFC', s1)
# t2 = unicodedata.normalize('NFC', s2)

# print(t1 == t2)

# print(ascii(t1))

# t3 = unicodedata.normalize('NFD', s1)
# t4 = unicodedata.normalize('NFD', s2)

# print(t3 == t4)
# print(ascii(t3))


'''  Stripping Unwanted Characters from Strings 
<> You want to strip unwanted characters, such as whitespace, from the beginning, end, or
middle of a text string.

The strip() method can be used to strip characters from the beginning or end of a
string. lstrip() and rstrip() perform stripping from the left or right side, respectively.
'''

# s = 'hello world \n'
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# character stripping 
# t = '-----hello====='

# print(t.lstrip('-'))
# print(t.strip('-='))


''' 
Sanitizing and Cleaning Up Text


'''

# s = 'pýtĥöñ\fis\tawesome\r\n'
# # cleaning whitespace
# remap = {
#     ord('\t') : ' ',
#     ord('\f') : ' ',
#     ord('\r') : None
# }

# a = s.translate(remap)
# print(a)

# The whitespace characters such as \t and \f have been remapped
# to a single space.The carriage return \r has been deleted entirely.
# import unicodedata
# import sys 
# cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))


# b = unicodedata.normalize('NFD', a)
# print(b)

# print(b.translate(cmb_chrs))

''' 
Combining and Concatenating Strings

We can combine many small strings together into a larget one.
'''

# parts = ['Is', 'Chicago', 'Not', 'Chicago?']
# print(' '.join(parts))
# print(','.join(parts))

''' 
Formatting Text into a Fixed Number of columns
'''
# s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
# the eyes, not around the eyes, don't look around the eyes, \
# look into my eyes, you're under."

# import textwrap 
# print(textwrap.fill(s, 70))
# print(textwrap.fill(s, 40))

# print(textwrap.fill(s, 40, initial_indent='   '))


''' Tokenizing Text
Need to parse left to right into a stream of tokens
For more advanced kinds of tokenizing, you may want to check out packages such as
PyParsing or PLY. 

'''
from collections import namedtuple

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)
