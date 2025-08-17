# Family knowledge base

# --- Facts ---
male = {"Ramesh", "Anil", "Ravi"}
female = {"Sita", "Meena", "Priya"}

# Parent relationships
parent = {
    ("Ramesh", "Anil"),
    ("Sita", "Anil"),
    ("Ramesh", "Meena"),
    ("Sita", "Meena"),
    ("Anil", "Ravi"),
    ("Meena", "Priya")
}

# --- Rules ---
def father(x, y):
    return (x, y) in parent and x in male

def mother(x, y):
    return (x, y) in parent and x in female

def grandfather(x, y):
    return any(father(x, p) and (p, y) in parent for p in male | female)

def grandmother(x, y):
    return any(mother(x, p) and (p, y) in parent for p in male | female)

def brother(x, y):
    return x in male and any((p, x) in parent and (p, y) in parent for p in male | female) and x != y

def sister(x, y):
    return x in female and any((p, x) in parent and (p, y) in parent for p in male | female) and x != y

def uncle(x, y):
    return any(brother(x, p) and (p, y) in parent for p in male | female)

def aunt(x, y):
    return any(sister(x, p) and (p, y) in parent for p in male | female)

def cousin(x, y):
    return any((p1, x) in parent and (p2, y) in parent and (p1 != p2) and
               (any((gp, p1) in parent and (gp, p2) in parent for gp in male | female))
               for p1 in male | female for p2 in male | female)

# --- Demo ---
print("Father (Ramesh, Anil):", father("Ramesh", "Anil"))
print("Mother (Sita, Meena):", mother("Sita", "Meena"))
print("Grandfather (Ramesh, Ravi):", grandfather("Ramesh", "Ravi"))
print("Brother (Anil, Meena):", brother("Anil", "Meena"))
print("Cousin (Ravi, Priya):", cousin("Ravi", "Priya"))

