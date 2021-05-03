# Graph Theory Project 2021
# Author: Emmanuel Osabuehien
# Module: Graph Theory
# 30/04/2021

# Imports
import argparse

"""Creating a program that helps you search text files"""
"""I will be using regular expression wihtin this code"""

def shunt(infix):
    """Convert infix expressions to postfix."""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # Operator precedence.
    prec = {'*': 100, '.': 90, '|': 80}
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

class State:
    """A state and its arrows in Thompson's construction."""
    def __init__(self, label, arrows, accept):
        """label is the arrow labels, arrows is a list of states to
           point to, accept is a boolean as to whether this is an accept
           state.
        """
        self.label = label
        self.arrows = arrows
        self.accept = accept
    
    def followes(self):
        """The set of states that are gotten from following this state
           and all its e arrows."""
        # Include this state in the returned set.
        states = {self}
        # If this state has e arrows, i.e. label is None.
        if self.label is None:
            # Loop through this state's arrows.
            for state in self.arrows:
                # Incorporate that state's earrow states in states.
                states = (states | state.followes())
        # Returns the set of states.    
        return states

class NFA:
    """A non-deterministic finite automaton."""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):
        """Return True if this NFA (instance) matches the string s."""
        # A list of previous states that we are still in.
        previous = self.start.followes()
        # Loop through the string, a character at a time.
        for c in s:
            # Start with an empty set of current states.
            current = set()
            # Loop throuth the previous states.
            for state in previous:
                # Check if there is a c arrow from state.
                if state.label == c:
                    # Add followes for next state.
                    current = (current | state.arrows[0].followes())
            # Replace previous with current.
            previous = current
        # If the final state is in previous, then return True. False otherwise. 
        return (self.end in previous)

    def match2():
        """Returns True or false after a file is read and infix and string have been matched"""
        words = []
        infixes = []
        #Searches and opens text files in directory
        textfile = open("infix.txt", "rt")
        textfile2 = open("infix2.txt", "rt")
        #The strip will remove any unneccessary spacing in the string that is return
        for txt in textfile:
            infixes.append(txt.strip())

        for txt2 in textfile2:
            words.append(txt2.strip())
        
        for infix in infixes:
            for word in words:
                #Function is then printed to screen
                print("Match: " + str(match(infix, word)), "Infix: " + infix, "String: " + word)
        #Close files after function is complete
        textfile.close()
        textfile2.close()

    def match3(infixes, words):
        """Return True or False after a string has been input and matched to infix, it will also print out results in a text file"""
        #Searches and opens text files in directory
        textfile = open("output.txt", "a+")
        textfile2 = open("infix.txt", "a+")
        textfile3 = open("infix2.txt", "a+")

        for infix in infixes:
            for word in words:
                print("Match: " + str(match(infix, word)), "Infix: " + infix, "String: " + word)
                #The string that is return is then output into a text file and stored
                textfile.write("{} {} {}".format("Match: %s" % str(match(infix, word)), "Infix: %s" % infix, "String: %s\n" % word))
                textfile2.write("%s\n" % infix)
                textfile3.write("%s\n" % word)

        file.close()

def re_to_nfa(postfix):
    # A stack for NFAs.
    stack = []
    # Loop through the postfix r.e. left to right.
    for c in postfix:
        # Concatenation.
        if c == '.':
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Make accept state of NFA1 non-accept.
            nfa1.end.accept = False
            # Make it point at start state of nfa2.
            nfa1.end.arrows.append(nfa2.start)
            # Make a new NFA with nfa1's start state and nfa2's end state.
            nfa = NFA(nfa1.start, nfa2.end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '|':
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old end states non-accept.
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '*':
            # Pop one NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start state.
            start.arrows.append(nfa1.start)
            # And at the new end state.
            start.arrows.append(end)
            # Make old end state non-accept.
            nfa1.end.accept = False
            # Make old end state point to new end state.
            nfa1.end.arrows.append(end)
            # Make old end state point to old start state.
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        else:
            # Create an NFA for the non-special character c.
            # Create the end state.
            end = State(None, [], True)
            # Create the start state.
            start = State(c, [], False)
            # Point new start state at new end state.
            start.arrows.append(end)
            # Create the NFA with the start and end state.
            nfa = NFA(start, end)
            # Append the NFA to the NFA stack.
            stack.append(nfa)
    
    # There should only be one NFA on the stack.
    if len(stack) != 1:
        return None
    else:
        return stack[0]

if __name__ == "__main__":
    automatons =[ ["a.(b.b)*.a", ["abba", "ab", "acc", "abbc", "accb", "caba", "abbbc", "abcb", "bac", "cab"]],
                    ["a.b", ["abba", "ab", "acc", "abbc", "accb", "caba", "abbbc", "abcb", "bac", "cab"]],
                ["(a.(b|c))*", ["abba", "ab", "acc", "abbc", "accb", "caba", "abbbc", "abcb", "bac", "cab"]],
                ["a+b.c", ["abba", "ab", "acc", "abbc", "accb", "caba", "abbbc", "abcb", "bac", "cab"]],
                ["a.(b|c).a*", ["abba", "ab", "acc", "abbc", "accb", "caba", "abbbc", "abcb", "bac", "cab"]],
                ["a.(b.b)*.c", ["abba", "ab", "acc", "abbc", "accb", "caba", "abbbc", "abcb", "bac", "cab"]],
                  ["aa.*", ["abba", "ab", "acc", "abbc", "accb", "caba", "abbbc", "abcb", "bac", "cab"]]
                ]
    print("Test")
    for automata in automatons:
        infix = automata[0]
        postfix = shunt(infix)
        nfa = re_to_nfa(postfix)
        print("infix:   %s"% infix)
        print("postfix: %s" % shunt(infix))
        print("nfa:  %s" %{re_to_nfa(postfix)})
        for s in automata[1]:
             match = nfa.match(s)
             print("The String Passes True Or False: %s"%nfa.match(s))

#Menu to display 2 of my aforementioned functions
#Menu is kinda messy so it may print out or it may not, it prints out locally on my end
def choices():
    select = True
    while select:
        option = input("\n1: Reads in a text files to compare infixes and string" +
                            "\n2: Prints out results to associated file" + "\n3: QUIT!\n")
        if option == 1:
            match2()
        elif option == 2:
            match3()
        elif option == 3:
            select = False

choices()