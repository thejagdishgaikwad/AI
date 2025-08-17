# Distributive Law Verification in Python

def distributive_and_over_or(a, b, c):
    left = a and (b or c)
    right = (a and b) or (a and c)
    return left == right

def distributive_or_over_and(a, b, c):
    left = a or (b and c)
    right = (a or b) and (a or c)
    return left == right

# Test all combinations of A, B, C
values = [True, False]

print("=== Distributive Law: A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C) ===")
for A in values:
    for B in values:
        for C in values:
            print(f"A={A}, B={B}, C={C} -> {distributive_and_over_or(A, B, C)}")

print("\n=== Distributive Law: A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C) ===")
for A in values:
    for B in values:
        for C in values:
            print(f"A={A}, B={B}, C={C} -> {distributive_or_over_and(A, B, C)}")

