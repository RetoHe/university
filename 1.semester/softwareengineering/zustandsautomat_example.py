#ac*b Automat

def automata1(input_string):
    state = 0

    for  char in input_string:
        if state == 0 and char == "a":
            state = 1
        elif state == 1 and char == "c":
            state = 1
        elif state ==  1 and char == "b":
            state = 2
        else:
            state = 3

    return state == 2

r1 = automata1("cccbbb")
r2 = automata1("accb")

print(r1, r2)

def automata2(input_string):
    state = 0

    for char in input_string:
        if state == 0 and char == "a:" :
            state = 1
        elif state == 1 and char == "b" or char == "c":
            state = 2
        elif state == 2 and char == "a":
            state = 3
        elif state == 3 and char != "":
            state = 2

    return state == 3

r3 = ("aba")
r4 = ("acc")

def automatatest(input_string):
    state = 0

    for char in input_string:
        if state == 0 and char == "a:" :
            state = 1
        elif state == 1 and char in ("b", "c"):
            state = 3
        elif state == 3 and char == "a":
            state = 4
        else:
            state = 2

    return state == 4

r5 = automatatest("aba")
r6 = automatatest("abb")

print(r5, r6)
