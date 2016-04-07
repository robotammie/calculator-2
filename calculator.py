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


def check_if_number(token_list):
    '''Checks if all tokens in list are whole numbers'''

    valid = True

    for token in token_list[1:]:
        if token.isdigit():
            continue
        else:
            valid = False
            break

    return valid


def master_check(token_list, num_arg):
    '''Checks for valid inputs'''

    if check_num_tokens(token_list, num_arg) and check_if_number(token_list):
        return True
    else:
        return False



# Your code goes here
while True:
    userinput = raw_input('>')
    
    if userinput != "q":
        pieces = userinput.split(' ')
        # print master_check(pieces, 2)
        if pieces[0] == '+':
            if master_check(pieces, 2):
                print add(int(pieces[1]),int(pieces[2]))
            else:
                print "I didn't understand you. Please try again."
            
        elif pieces[0] == '-':
            if master_check(pieces, 2):
                print subtract(int(pieces[1]),int(pieces[2]))
            else:
                print "I didn't understand you. Please try again."

        elif pieces[0] == '*':
            if master_check(pieces, 2):
                print multiply(int(pieces[1]),int(pieces[2]))
            else:
                print "I didn't understand you. Please try again."

        elif pieces[0] == '/':
            if master_check(pieces, 2):
                print divide(int(pieces[1]),int(pieces[2]))
            else:
                print "I didn't understand you. Please try again."

        elif pieces[0] == 'square':
            if master_check(pieces, 1):
                print square(int(pieces[1]))
            else:
                print "I didn't understand you. Please try again."

        elif pieces[0] == 'cube':
            if master_check(pieces, 1):
                print cube(int(pieces[1]))
            else:
                print "I didn't understand you. Please try again."

        elif pieces[0] == 'pow':
            if master_check(pieces, 2):
                print power(int(pieces[1]),int(pieces[2]))
            else:
                print "I didn't understand you. Please try again."

        elif pieces[0] == 'mod':
            if master_check(pieces, 2):
                print mod(int(pieces[1]),int(pieces[2]))
            else:
                print "I didn't understand you. Please try again."

        else:
            print "I didn't understand you. Please try again."

    else:
        break

    


