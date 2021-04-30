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
        states = {self}
        if self.label is None:
            for state in self.arrows:
                states = (states | state.followes())
        return states

class NFA:
    """A non-deterministic finite automaton."""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):
        """Return True iff this NFA (instance) matches the string s."""
        text = ""
        words = []
        
        for c in s:
            if c in ["", "\n"]:
                text = c + text
            else: 
                words.append(text)
                text = ""
        words.append(text)

        for i in range(len(words)):
            previous = self.start.followes()
            for c in s:
                current = set()
                for state in previous: 
                    if state.label == c:
                        current = (current | state.arrows[0].follows())
                previous = current
        return (self.end in previous)
            
def re_to_nfa(postfix):
    stack = []
    for c in postfix:
        if c == '.':
            nfa2 = stack[-1]
            stack = stack[:-1]
            nfa1 = stack[-1]
            stack = stack[:-1]
            nfa1.end.accept = False
            nfa1.end.arrows.append(nfa2.start)
            nfa = NFA(nfa1.start, nfa2.end)
            stack.append(nfa)
        elif c == '|':
            nfa2 = stack[-1]
            stack = stack[:-1]
            nfa1 = stack[-1]
            stack = stack[:-1]
            start = State(None, [], False)
            end = State(None, [], True)
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            nfa1.end.accept = False
            nfa2.end.accept = False
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            nfa = NFA(start, end)
            stack.append(nfa)
        elif c == '*':
            nfa1 = stack[-1]
            stack = stack[:-1]
            start = State(None, [], False)
            end = State(None, [], True)
            start.arrows.append(nfa1.start)
            start.arrows.append(end)
            nfa1.end.accept = False
            nfa1.end.arrows.append(end)
            nfa1.end.arrows.append(nfa1.start)
            nfa = NFA(start, end)
            stack.append(nfa)
        else:
            end = State(None, [], True)
            start = State(c, [], False)
            start.arrows.append(end)
            nfa = NFA(start, end)
            stack.append(nfa)

    if len(stack) != 1:
        return None
    else:
        return stack[0]

if __name__ == "__main__":
    for postfix in ["abb.*.a.", "100.*.1.", 'ab|']:
        print("postfix: %s" %postfix)
        print("nfa: %s" %{re_to_nfa(postfix)})