"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def check_num_tokens(token_list, num_arg):
    '''Check that the number of tokens matches the number of arguments needed'''

    if len(token_list) == num_arg + 1:
        return True
    else:
        return False



# Your code goes here
while True:
    userinput = raw_input('>')
    
    if userinput != "q":
        pieces = userinput.split(' ')
        # print pieces
        if pieces[0] == '+':
            if check_num_tokens(pieces, 2):
                print add(int(pieces[1]),int(pieces[2]))
            else:
                print "Wrong number of inputs."
            
        elif pieces[0] == '-':
            print subtract(int(pieces[1]),int(pieces[2]))
        
        elif pieces[0] == '*':
            print multiply(int(pieces[1]),int(pieces[2]))

        elif pieces[0] == '/':
            print divide(int(pieces[1]),int(pieces[2]))

        elif pieces[0] == 'square':
            print square(int(pieces[1]))

        elif pieces[0] == 'cube':
            print cube(int(pieces[1]))

        elif pieces[0] == 'pow':
            print power(int(pieces[1]),int(pieces[2]))

        elif pieces[0] == 'mod':
            print mod(int(pieces[1]),int(pieces[2]))

        else:
            print "I didn't understand you. Please try again."

    else:
        break

    


