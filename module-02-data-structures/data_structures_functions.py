# Module 2 Assignment — Data Structures and Functions
# Course: Data Science Program

# Q1 — Remove duplicates and return summary dictionary
def summarize_numbers(numbers):
    """Returns original list, unique values, and count."""
    unique_values = []
    for i in numbers:
        if i not in unique_values:
            unique_values.append(i)
    return {
        "original_list": numbers,
        "unique_values": unique_values,
        "count": len(unique_values)
    }

print(summarize_numbers([1, 1, 3, 3, 4, 4, 5, 5]))


# Q2 — Set operations with default parameters
def set_operations(set1=None, set2=None):
    """Returns union, intersection, and difference of two sets."""
    if set1 is None:
        set1 = set()
    if set2 is None:
        set2 = set()
    return {
        "union": set1.union(set2),
        "intersection": set1.intersection(set2),
        "difference": set1.difference(set2)
    }

print(set_operations({2, 3, 5}, {2, 5, 7}))


# Q3 — Tuple unpacking and comparison
mixed_tuple = (2, 3.5, "hello", True)
a, b, c, d = mixed_tuple
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

another_tuple = (2, 1.5, "hi", False)
print("Equal:", mixed_tuple == another_tuple)
print("Not equal:", mixed_tuple != another_tuple)

# Key difference — List vs Tuple:
# Lists are mutable   → elements can be changed after creation → my_list = [1, 2, 3]
# Tuples are immutable → elements cannot be changed after creation → my_tuple = (1, 2, 3)
