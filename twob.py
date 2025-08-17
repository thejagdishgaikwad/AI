def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve Tower of Hanoi problem.
    n        : number of disks
    source   : the rod where disks are initially placed
    target   : the rod to move disks to
    auxiliary: helper rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} → {target}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)
    # Move the largest disk to target
    print(f"Move disk {n} from {source} → {target}")
    # Move the n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source)


# Example usage:
n = 3  # number of disks
print(f"Steps to solve Tower of Hanoi with {n} disks:\n")
tower_of_hanoi(n, "A", "C", "B")

