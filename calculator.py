"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    userinput = raw_input()
    
    if userinput != "q":
        pieces = userinput.split(' ')
        # print pieces
        if pieces[0] == '+':
            result = add(int(pieces[1]),int(pieces[2]))
            print result
    

    else:
        break

    


