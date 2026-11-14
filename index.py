
# ========== SET PROGRAMS ==========

# 1. Add Element to a Set
# Problem: Add an item to a given set.
# Explanation: Use add() method.
# Input: {1, 2, 3}, add 4
# Output: {1, 2, 3, 4}
s = {1, 2, 3}
s.add(4)
print("1.", s)


# 2. Remove Element from Set
# Problem: Remove a specific element from a set.
# Explanation: Use remove() or discard() to avoid KeyError.
# Input: {1, 2, 3}, remove 2
# Output: {1, 3}
s = {1, 2, 3}
s.discard(2)
print("2.", s)


# 3. Union of Two Sets
# Problem: Find union of two sets.
# Explanation: Use | operator or union() method.
# Input: {1, 2}, {2, 3}
# Output: {1, 2, 3}
a = {1, 2}
b = {2, 3}
print("3.", a | b)


# 4. Intersection of Sets
# Problem: Find common elements in two sets.
# Explanation: Use & operator or intersection().
# Input: {1, 2}, {2, 3}
# Output: {2}
print("4.", a & b)


# 5. Difference of Sets
# Problem: Find elements in first set but not second.
# Explanation: Use - or difference().
# Input: {1, 2, 3}, {2, 3}
# Output: {1}
print("5.", {1, 2, 3} - {2, 3})


# 6. Check Subset
# Problem: Check whether one set is a subset.
# Explanation: Use issubset().
# Input: {1, 2}, {1, 2, 3}
# Output: True
print("6.", {1, 2}.issubset({1, 2, 3}))


# 7. Set Length
# Problem: Find number of elements in set.
# Explanation: Use len().
# Input: {1, 2, 3}
# Output: 3
print("7.", len({1, 2, 3}))


# 8. Clear a Set
# Problem: Remove all elements from a set.
# Explanation: Use clear().
# Input: {1, 2, 3}
# Output: set()
s = {1, 2, 3}
s.clear()
print("8.", s)


# 9. Symmetric Difference
# Problem: Find elements in either set but not both.
# Explanation: Use ^ or symmetric_difference().
# Input: {1, 2, 3}, {2, 3, 4}
# Output: {1, 4}
print("9.", {1, 2, 3} ^ {2, 3, 4})


# 10. Convert List to Set
# Problem: Remove duplicates using set.
# Explanation: Use set() constructor.
# Input: [1, 2, 2, 3]
# Output: {1, 2, 3}
print("10.", set([1, 2, 2, 3]))


# ========== DICTIONARY PROGRAMS ==========

# 11. Create Dictionary from Two Lists
# Explanation: Use zip().
# Input: ["a", "b"], [1, 2]
# Output: {"a": 1, "b": 2}
print("11.", dict(zip(["a", "b"], [1, 2])))


# 12. Update Dictionary Value
# Explanation: Use dict[key] = value.
# Input: {"a": 1}, update a to 2
# Output: {"a": 2}
d = {"a": 1}
d["a"] = 2
print("12.", d)


# 13. Remove Key from Dictionary
# Explanation: Use del or pop().
# Input: {"a": 1, "b": 2}, remove b
# Output: {"a": 1}
d = {"a": 1, "b": 2}
d.pop("b")
print("13.", d)


# 14. Check Key Existence
# Explanation: Use in operator.
# Input: {"x": 1}, key = "x"
# Output: True
print("14.", "x" in {"x": 1})


# 15. Iterate Over Dictionary
# Explanation: Use items() in loop.
# Input: {"a": 10, "b": 20}
# Output: a 10, b 20
d = {"a": 10, "b": 20}
for k, v in d.items():
    print(k, v)


# 16. Dictionary Length
# Explanation: Use len().
# Input: {"x": 1, "y": 2}
# Output: 2
print("16.", len({"x": 1, "y": 2}))


# 17. Merge Two Dictionaries
# Explanation: Use unpacking or update().
# Input: {"a": 1}, {"b": 2}
# Output: {"a": 1, "b": 2}
print("17.", {**{"a": 1}, **{"b": 2}})


# 18. Get Value with Default
# Explanation: Use get().
# Input: {"a": 1}, get "b" with default 0
# Output: 0
print("18.", {"a": 1}.get("b", 0))


# 19. Count Frequency of Elements
# Explanation: Use dictionary to count frequency.
# Input: [1, 2, 2, 3]
# Output: {1: 1, 2: 2, 3: 1}
lst = [1, 2, 2, 3]
d = {}
for x in lst:
    d[x] = d.get(x, 0) + 1
print("19.", d)


# 20. Invert a Dictionary
# Explanation: Swap keys and values.
# Input: {"a": 1, "b": 2}
# Output: {1: "a", 2: "b"}
d = {"a": 1, "b": 2}
print("20.", {v: k for k, v in d.items()})


# 21. Find Key with Maximum Value
# Explanation: Use max() with key=d.get.
# Input: {"a": 10, "b": 20, "c": 15}
# Output: "b"
d = {"a": 10, "b": 20, "c": 15}
print("21.", max(d, key=d.get))


# 22. Sort Dictionary by Values
# Explanation: Use sorted() and lambda.
# Input: {"a": 3, "b": 1, "c": 2}
# Output: [('b', 1), ('c', 2), ('a', 3)]
d = {"a": 3, "b": 1, "c": 2}
print("22.", sorted(d.items(), key=lambda x: x[1]))


# 23. Create Dictionary of Squares
# Explanation: Use dictionary comprehension.
# Input: range(1, 4)
# Output: {1: 1, 2: 4, 3: 9}
print("23.", {x: x**2 for x in range(1, 4)})


# 24. Filter Dictionary by Value
# Explanation: Use dictionary comprehension and if.
# Input: {"a": 10, "b": 5, "c": 15}, condition > 10
# Output: {"c": 15}
d = {"a": 10, "b": 5, "c": 15}
print("24.", {k: v for k, v in d.items() if v > 10})


# 25. Combine Values of Duplicate Keys
# Explanation: Use get() to add common key values.
# Input: {"a": 1, "b": 2}, {"a": 3, "c": 4}
# Output: {"a": 4, "b": 2, "c": 4}
a = {"a": 1, "b": 2}
b = {"a": 3, "c": 4}
d = a.copy()
for k, v in b.items():
    d[k] = d.get(k, 0) + v
print("25.", d)


# 26. Count Word Frequency
# Explanation: Use split() and dictionary.
# Input: "apple banana apple"
# Output: {"apple": 2, "banana": 1}
words = "apple banana apple".split()
d = {}
for w in words:
    d[w] = d.get(w, 0) + 1
print("26.", d)


# 27. Remove Duplicate Values
# Explanation: Use values() to check duplicates.
# Input: {"a": 1, "b": 2, "c": 1}
# Output: {"a": 1, "b": 2}
d = {"a": 1, "b": 2, "c": 1}
result = {}
for k, v in d.items():
    if v not in result.values():
        result[k] = v
print("27.", result)


# 28. Find Common Keys
# Explanation: Use keys() and & operator.
# Input: {"a": 1, "b": 2}, {"b": 3, "c": 4}
# Output: ["b"]
a = {"a": 1, "b": 2}
b = {"b": 3, "c": 4}
print("28.", list(a.keys() & b.keys()))


# 29. Swap Keys and Values Safely
# Explanation: Use dictionary comprehension.
# Input: {"x": 1, "y": 2}
# Output: {1: "x", 2: "y"}
d = {"x": 1, "y": 2}
print("29.", {v: k for k, v in d.items()})


# 30. Delete Items by Value
# Explanation: Use dictionary comprehension.
# Input: {"a": 1, "b": 2, "c": 1}, value = 1
# Output: {"b": 2}
d = {"a": 1, "b": 2, "c": 1}
print("30.", {k: v for k, v in d.items() if v != 1})
