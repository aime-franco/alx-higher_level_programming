#!/usr/bin/python3
def multiple_returns(sentence):
    Mytuple = ()
    if len(sentence) == 0:
        Mytuple = 0, "None"
    else:
        Mytuple = len(sentence), sentence[0]
    return Mytuple
