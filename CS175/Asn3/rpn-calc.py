# rpn-calc.py
# Evaluates lines that contain expressions written in postfix notation.
#
# Copyright 2011, Mark Tupala.
# All rights reserved.
#
# Created: Mark Tupala (tupala@ualberta.ca)

import fileinput
import sys
from operator import add, sub, mul, truediv, floordiv, mod, neg
import linkedlists

class PostfixCalculator(object):
    divide_operations = ['/', 'div', 'mod']
    binary_operations = {'+': add, '-': sub, '*': mul, 
                                   '/': truediv, 'div': floordiv, 'mod': mod}
    unary_operations = {'chs': neg, 'int': int}
    operations = binary_operations.keys() | unary_operations.keys()
    insufficient_error = 'Error: insufficient arguments for operation '
    invalid_error = 'Error: divide by 0 for operation '
    modulo_error = 'Error: non-natural number argument for operation mod'
    
    def __init__(self, eval_stack):
        self.eval_stack = eval_stack
    
    def feed(self, tokens):
        self.show_evaluation(tokens)
        for token in tokens:
            self.process(token)
    
    def show_evaluation(self, tokens):
        print('Evaluating: ', end='')
        for token in tokens:
            print(token, end=' ')
        print('')
    
    def process(self, token):
        if token in self.operations:
            self.process_operator(token)
        elif token == 'sum':
            self.sum()
        elif token == 'print':
            self.show()
        else:
            self.process_number(token)

    def process_operator(self, operator):
        if operator in self.binary_operations:
            num_args = 2
        elif operator in self.unary_operations:
            num_args = 1
        if not self.check_arguments(num_args):
            self.eval_stack.push(self.insufficient_error + operator)
        elif operator in self.divide_operations and not self.check_denom():
            self.eval_stack.push(self.invalid_error + operator)
        elif operator == 'mod' and not self.check_modulo():
            self.eval_stack.push(self.modulo_error)
        else:
            self.operate(operator, num_args)

    def process_number(self, token):
        clean_token = _str_to_num(token)
        self.eval_stack.push(clean_token)

    def check_arguments(self, needed):
        if len(self.eval_stack) < needed:
            return False
        else:
            return True
    
    def check_denom(self):
        if self.eval_stack.peek() == 0: return False
        else: return True
    
    def check_modulo(self):
        x = self.eval_stack.pop()
        if x < 1 or x % 1 != 0:
            self.eval_stack.push(x)
            return False
        y = self.eval_stack.pop()
        if y < 1 or y % 1 != 0: ans = False
        else: ans = True
        self.eval_stack.push(y)
        self.eval_stack.push(x)
        return ans
    
    def operate(self, oper, num_args):
        x = self.eval_stack.pop()
        if num_args == 1:
            self.eval_stack.push(self.unary_operations[oper](x))
        elif num_args == 2:
            y = self.eval_stack.pop()
            self.eval_stack.push(self.binary_operations[oper](y, x))

    def sum(self):
        if len(self.eval_stack) == 0: self.eval_stack.push(0)
        else:
            while self.check_arguments(2):
                self.operate('+', 2)
    
    def show(self):
        self.eval_stack.rev_print()
    

def _str_to_num(input):
    """Checks if input is a valid number, otherwise an exception is thrown."""
    try:
        return int(input)
    except ValueError:
        try:
            return float(input)
        except ValueError:
            return


# Command Loop
if __name__ == "__main__":

    print("Enter each expression on its own line.")
    print("Control-D (Control-Z on windows) to finish entering expression")
    print("to be evaluated. Put 'quit' on its own line to exit.")
    
    calculator = PostfixCalculator(linkedlists.Stack())
    
    for input_line in fileinput.input():
        input_line = input_line.rstrip("\n")
        if input_line == 'quit':
            sys.exit(1)

        calculator.eval_stack.clear()
        tokens = input_line.split()
        calculator.feed(tokens)
        
        print("Answer as final contents of stack are (top to bottom):")
        while len(calculator.eval_stack) > 0:
            print(calculator.eval_stack.pop() )
        print("Bottom")

