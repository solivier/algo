#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def oldIsBalanced(s):
    stack = []
    for c in s:
        #print(c)
        if c == '(':
            stack.append(0)
        elif c == ')':
            if len(stack) > 0 and stack[-1] == 0:
                stack.pop()
            else:
                return "NO"
        elif c == '[':
            stack.append(2)
        elif c == ']':
            if len(stack) > 0 and stack[-1] == 2:
                stack.pop()
            else:
                return "NO"
        if c == '{':
            stack.append(4)
        elif c == '}':
            if len(stack) > 0 and stack[-1] == 4:
                stack.pop()
            else:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


def my_is_balanced(s):
    stack = []
    for char in s:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            if len(stack) == 0:
                return 'NO'
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return 'NO'

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = my_is_balanced(s)
        print(result)
