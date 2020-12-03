

def automate(input_string):
    result = False

    state = 0
    for char in input_string:
        if state == 0 and char == "a":
            state = 1
        elif state == 1 and char == "b":
            state = 2
        elif state == 2 and char == "c":
            state = 3
        elif state in (3, 4, 5) and char == "a":
            state = 4
        elif state in (1, 5) and char == "d":
            state = 5
        else:
            state = 6

    return state == 4


r1 = automate("abcaa")
r2 = automate("addda")
r3 = automate("aaa")
r4 = automate("aaad")
r5 = automate("ab")

print(r1, r2, r3, r4, r5) #False, True