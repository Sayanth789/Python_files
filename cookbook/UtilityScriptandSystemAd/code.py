''' Accepting Script Input via Redirection, Pipes
or Input Files

<>
You want a script you’ve written to be able to accept input using whatever mechanism
is easiest for the user. This should include piping output from a command to the script,
redirecting a file into the script, or just passing a filename, or list of filenames, to the
script on the command line.

Python’s built-in fileinput module makes this very simple and concise. If you have a
script that looks like this:

#!/usr/bin/env python3 
import fileinput 

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')

'''

'''

Parsing Commnad Line Options:
><
You want to write a program that parses options supplied on the command line (found
in sys.argv).
The argparse module can be used to parse command-line options. A simple example
will help to illustrate the essential features:


'''

'''
Hypothetical command-line tool for searching a collection of
files for one or more text patterns.
'''
import argparse

# parser = argparse.ArgumentParser(description='Search some files')


# parser.add_argument(dest="filenames", metavar='filename', nargs='*')
# parser.add_argument('-p', '--pat',metavar='pattern', required=True,dest='patterns', action='append',
#                     help='text pattern to search for')

# parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
# parser.add_argument('-o', dest='outfile', action='store',
#                         help='output file')
# parser.add_argument('--speed', dest='speed', action='store',
#         choices={'slow','fast'}, default='slow', help='search speed')

# args = parser.parse_args()


# # Output collected arguments
# print(args.filenames)
# print(args.patterns)
# print(args.verbose)
# print(args.outfile)
# print(args.speed)


'''  
Getting Terminal size: To get the terminal size to properly  format the 
output of the program

'''
import os 

sz = os.get_terminal_size() 

print(sz)
print(sz.columns)
print(sz.lines)
