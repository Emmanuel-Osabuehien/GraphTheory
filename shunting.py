import thompson

def shunt(infix):
    """Convert infix expressions to postfix."""
    postfix = ""
    stack = ""
    prec = {'*': 30, '.': 20, '|': 10}
    for c in infix:
        if c in {'*', '.', '|'}:
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            stack = stack + c
        elif c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            stack = stack[:-1]
        else:
            postfix = postfix + c

    while len(stack) != 0:
        postfix = postfix + stack[-1]
        stack = stack[:-1]
    return postfix

if __name__ == "__main__":
    automatons =[ ["a.(b.b)*.a", ["a", "b", "ab", "abb", "ba", "aaba"]],
                  ["1.(0.0)*.1", ["100  011", "11011", "01101", "111", "1010"]]
                ]
    print("Make Sure This Works")
    for automata in automatons:
        infix = automata[0]
        print("infix:   %s"% infix)
        print("postfix: %s" % shunt(infix))