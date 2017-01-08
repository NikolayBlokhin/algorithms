#!/bin/env python3
# -*- coding: utf-8 -*-


class Stack:

    def __init__(self):
        self.stack = []

    def __str__(self):
        out = 'Stack ['
        for i in self.stack:
            out += '{0}, '.format(i)
        out = out.rstrip(', ')
        out += ']'
        return out

    def clear(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)


if __name__ == '__main__':

    s = Stack()
    s.push('First')
    s.push('Second')
    s.push('Third')
    s.push('Fourth')

    print('Stack size: {0}'.format(s.size()))
    print(s)
    print(s.pop())
    print('Stack size: {0}'.format(s.size()))
    print(s)
    s.clear()
    print('Stack size: {0}'.format(s.size()))
    print(s)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    s.push(1)
    s.push(2)
    s.push(3)

    def func_1():
        a = s.pop()
        b = s.pop()
        result = a + b
        s.push(result)

    def func_2():
        a = s.pop()
        b = s.pop()
        return (a, b, a + b)

    print('\n\n')
    print(s)
    func_1()
    print(func_2())
    print(s)







