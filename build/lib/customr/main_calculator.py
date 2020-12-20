import operator
import os
import argparse

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.show()) != 0:
            x = self.stack.pop()
            return x
        else:
            assert len(self.show()) != 0, 'List is empty! ' + str(self.show())

    def clear(self):
        self.stack.clear()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def show(self):
        return self.stack


class Calculator:
    def __init__(self, string, stack):
        self.string: str = string
        self.array = []
        self.stack = stack
        self.operators = {
            '+': (1, operator.add),
            '-': (1, operator.sub),
            '*': (2, operator.mul),
            '/': (2, operator.truediv)
        }

    def is_seq_correct(self):
        for brace in self.string:
            if brace in '()':
                print(self.stack.show())
                if brace in '(':
                    self.stack.push(brace)  # Добавить скобку в стэк, если она открытая
                else:
                    left = self.stack.pop()
                    if left == '(':
                        right = ')'
                        if brace != right:
                            return False
        return self.stack.is_empty()

    def parse_row(self):
        data = []
        number = ''
        if self.is_seq_correct():
            print('Сырая строка: ' + self.string)
            for item in self.string:
                print(data)
                if item.isdigit():
                    number += item
                elif number:
                    data.append(number)
                    number = ''
                if item in '+-/*()':
                    data.append(item)
            if number:
                data.append(number)
        print('*******')
        return data

    def convert(self):
        result_stack = []
        temp_stack = []
        array = self.parse_row()
        '''
        self.operators = {
            '+': (1, operator.add),
            '-': (1, operator.sub),
            '*': (2, operator.mul),
            '/': (2, operator.truediv)
        }
        '''
        for item in array:
            print('Temp stack: [' + ', '.join(temp_stack) + ']' + '  Result stack: [' + ', '.join(result_stack) + ']')
            if item in self.operators.keys():
                while temp_stack and temp_stack[-1] != '(' and self.operators[item][0] <= self.operators[temp_stack[-1]][0]:
                    result_stack.append(temp_stack.pop())
                temp_stack.append(item)
            elif item == ')':
                while temp_stack:
                    x = temp_stack.pop()
                    if x == '(':
                        break
                    result_stack.append(x)
            elif item == '(':
                temp_stack.append(item)
            else:
                result_stack.append(item)
        while temp_stack:
            result_stack.append(temp_stack.pop())
        print('-------')
        return result_stack

    def calculate(self):
        final_stack = []
        array = self.convert()
        for item in array:
            if item in self.operators.keys():
                '''
                    '+': (1, operator.add),
                    '-': (1, operator.sub),
                    '*': (2, operator.mul),
                    '/': (2, operator.truediv)
                '''
                y, x = final_stack.pop(), final_stack.pop()
                result = self.operators[item][1](int(x), int(y))
                final_stack.append(result)
            else:
                final_stack.append(item)
            print(final_stack)
        print('Result: ' + str(final_stack[0]))
        return final_stack[0]


def create_parser():
    parser = argparse.ArgumentParser(description='InstaBot commands help')
    parser.add_argument('-r', '--row', action="store", dest="string", type=str)
    parser.add_argument('-t', '--text', action="store", dest="text", type=str)
    # parser.add_argument('-p', '--password', action="store", dest="password", type=str)
    # parser.add_argument('-t', '--path', action="store", default='$HOME', type=str)
    # parser.add_argument('-c', '--chromedriver', action="store", type=str)
    # parser.add_argument('-g', '--like', action="store", default='Like', type=str)

    args = parser.parse_args()
    return args


def run(string: str):
    # args = create_parser()
    # line = args.string
    print(string)
    calc = Calculator(string, stack=Stack())
    print(calc.calculate())


def console_run():
    args = create_parser()
    line = args.string
    hello = args.text
    calc = Calculator(line, stack=Stack())
    print(calc.calculate())
    print(hello)
    print(hello)
    print(hello)

# console_run()
# print(calc.is_seq_correct())
# print(calc.parse_row())
# print(calc.convert())


