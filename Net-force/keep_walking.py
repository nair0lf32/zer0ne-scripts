#!/usr/bin/python
"""keep walking"""
X = 1
Y = 1
PREV = 1
ANSWER = X * Y + PREV + 3

while X != 525:
    X += 1
    Y += 1
    PREV = ANSWER
    ANSWER = X * Y + PREV + 3

print(ANSWER)
