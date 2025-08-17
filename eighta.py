# Associative Law Verification in Python

def associative_and(a, b, c):
    left = (a and b) and c
    right = a and (b and c)
    return left == right

def associative_or(a, b, c):
    left = (a or b) or c
    right = a or (b or c)
    return left == right

# Test all combinations of A, B, C
values = [True, False]

print("=== Associative Law for AND (∧) ===")
for A in values:
    for B in values:
        for C in values:
            print(f"A={A}, B={B}, C={C} -> {associative_and(A, B, C)}")

print("\n=== Associative Law for OR (∨) ===")
for A in values:
    for B in values:
        for C in values:
            print(f"A={A}, B={B}, C={C} -> {associative_or(A, B, C)}")

