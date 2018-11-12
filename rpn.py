#!/usr/bin/env python3

import operator


def factorial(arg1):
    return 1 if (arg1==1 or arg1==0) else arg1 * factorial(arg1 - 1)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '//': operator.floordiv,
    '%': operator.truediv,
    '&': operator.and_,
    '|': operator.or_,
    '~': operator.inv,
    '!': factorial,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            # only for operations with ONE operand
            if token is '!' or token is '~':
                arg1 = stack.pop()
                result = function(arg1)
                stack.append(result)               
            # everything else      
            else:          
                arg2 = stack.pop()            
                arg1 = stack.pop()
                result = function(arg1, arg2)
                if token is '%':
                    result = result * 100
                stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
