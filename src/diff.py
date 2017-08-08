import ast
import re

sample = """

def test1():
    print("This world")

def test2():
    print("or the next")

print("Hello, World")
"""


tree = ast.parse(sample)

print("\nAST Dump:")
print(ast.dump(tree) + "\n")

tab = 0


def ptab():
    global tab
    o = ['\t' for x in range(0, tab)]
    print("".join(o), end="")


def tabin():
    global tab
    tab += 1


def tabdown():
    global tab
    tab -= 1


def rec_down(node):
    for fieldname, value in ast.iter_fields(node):
        print(f"{type(node)} -> ")
        tabin()
        ptab()
        print(f"{fieldname}: {value}")


print("\nNode Traversal:")
rec_down(tree)
