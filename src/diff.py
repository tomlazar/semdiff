import ast

sample = """
print("Hello, World")
"""

tree = ast.parse(sample)

print(ast.dump(tree))
