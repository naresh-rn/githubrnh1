"""Comprehension"""
# the shorthand syntax for creating collections and iterable objects.
# Syntax's
# 1. List Comprehension:
[ expr(item) for item in iterable ]

# 2. Set Comprehension:
{ expr(item) for item in iterable }

# 3. Dictionary Comprehension:
{ key_expr:value_expr for item in iterable }

# 4. Generator Comprehension:
( expr(item) for item in iterable)

# 5. Comprehension with If-clause:
[ expr(item) for item in iterable if predicate(item) ]

# 6. Multiple Comprehension:
values = [(x,y) for x in range(5) for y in range(3)]
"""  Normal Form
values = []
for x in range(5):
    for y in range(3):
        values.append((x,y))
""" 

[(x,y) for x in range(10) for y in range(3)]

# 7. Nested Comprehension:
"""
values = [[y*3 for y in range(x)] for x in range(10)]

values = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y*3)
    values.append(inner)"""

[[y*3 for y in range(x)] for x in range(10)]


# 