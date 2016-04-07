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

    # make it so the for loop only does something if it needs to
    for token in token_list[1:]:
        if not token.isdigit():
            return False

    return True


# def master_check(token_list, num_arg):
#     '''Checks for valid inputs'''

#     return check_num_tokens(token_list, num_arg) and check_if_number(token_list)



# Your code goes here
while True:
    userinput = raw_input('>')
    
    if userinput != "q":
        pieces = userinput.split(' ')
        
        if not check_if_number(pieces):
            print "error message"

        else:
            for number in pieces[1:]:
                number = int(number)
                print type(number)

            print pieces
            print number
            # PROBLEM ^ number is overwritten in for loop, find a way to keep all numbers for future use.

            if pieces[0] == '+':
                if check_num_tokens(pieces, 2):
                    print add(pieces[1],pieces[2])
                else:
                    print "I didn't understand you. Please try again."
                
            elif pieces[0] == '-':
                if check_num_tokens(pieces, 2):
                    print subtract(pieces[1],pieces[2])
                else:
                    print "I didn't understand you. Please try again."

            elif pieces[0] == '*':
                if check_num_tokens(pieces, 2):
                    print multiply(pieces[1],pieces[2])
                else:
                    print "I didn't understand you. Please try again."

            elif pieces[0] == '/':
                if check_num_tokens(pieces, 2):
                    print divide(pieces[1],pieces[2])
                else:
                    print "I didn't understand you. Please try again."

            elif pieces[0] == 'square':
                if check_num_tokens(pieces, 1):
                    print square(pieces[1])
                else:
                    print "I didn't understand you. Please try again."

            elif pieces[0] == 'cube':
                if check_num_tokens(pieces, 1):
                    print cube(pieces[1])
                else:
                    print "I didn't understand you. Please try again."

            elif pieces[0] == 'pow':
                if check_num_tokens(pieces, 2):
                    print power(pieces[1],pieces[2])
                else:
                    print "I didn't understand you. Please try again."

            elif pieces[0] == 'mod':
                if check_num_tokens(pieces, 2):
                    print mod(pieces[1],pieces[2])
                else:
                    print "I didn't understand you. Please try again."

            else:
                print "I didn't understand you. Please try again."

    # execute if the user types in 'q'
    else:
        break

    


