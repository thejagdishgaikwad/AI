# Predicate Logic Example in Python

def Batsman(x):
    return x == "Sachin"

def Cricketer(x):
    # Rule: If x is a batsman, then x is a cricketer
    if Batsman(x):
        return True
    return False

# Fact
sachin = "Sachin"

print("Sachin is Batsman:", Batsman(sachin))
print("Therefore, Sachin is Cricketer:", Cricketer(sachin))

