# Graph Theory Project 2021
# Author: Emmanuel Osabuehien
# Module: Graph Theory
# 30/04/2021

# Imports
import argparse

"""Creating a program that helps you search text files"""
"""I will be using regular expression wihtin this code"""

# parser = argparse.ArgumentParser()                                               
# parser.add_argument("--file", "-f", type=str, required=True)
# args = parser.parse_args()

# findText = open("randomtext2.txt")
# find = findText.read()         
# findText.close()                  
# print(find)      

def shunt(infix):
    """Convert infix expressions to postfix."""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # Operator precedence.
    prec = {'*': 30, '.': 20, '|': 10}
    # Loop through the input a character at a time.
    for c in infix:
        # c is an operator.
        if c in {'*', '.', '|'}:
            # Check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Push c to stack.
            stack = stack + c
        elif c == '(':
            # Push c to stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
                # c is a non-special.
        else:
            # Push it to the output.
            postfix = postfix + c

    # Empty the operator stack.
    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    # Return the postfix version of infix.
    return postfix

    if __name__ == "__main__":
        automatons = [  ["a.(b.b)*.a", ["a", "b", "ab", "abb", "ba", "aaba"]]
             , ["1.(0.0)*.1", ["100  011", "11011", "01101", "111", "1010"]]
    ]

    for automata in automatons:
        infix = automatons[0]
        print(f"infix:   {infix}")
        print(f"postfix: {shunt(infix)}")
  