import math
import tkinter as tk


def parse(tokens, start=0):
    code = []
    pos = start
    while pos < len(tokens):
        pass  # TODO
    return code


class PS:
    def __init__(self):
        self.stack = []
        self.words = {
            'dup': self.op_dup,
            'add': self.op_add,
            'sub': self.op_sub,
            'mul': self.op_mul,
            'div': self.op_div
        }

    def execute(self, code):
        pass  # TODO

    def op_dup(self):
        pass  # TODO

    def op_add(self):
        pass  # TODO

    def op_sub(self):
        pass  # TODO

    def op_mul(self):
        pass  # TODO

    def op_div(self):
        pass  # TODO


source = ''

ps = PS()
ast = parse(source.split())
ps.execute(ast)
print(ps.stack)