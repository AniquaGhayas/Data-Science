# A. Arithmetic Operations
a = 15
b = 4
print("--- Arithmetic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print()

# B. Data Types and Type Conversion
print("--- Data Types & Conversion ---")
x = 10          
y = 5.7         
z = "123"       
print("Original types:", type(x), type(y), type(z))
conv_x = float(x)
conv_z = int(z)
print("Converted values:", conv_x, type(conv_x), "and", conv_z, type(conv_z))
print()

# C. String Operations
print("--- String Operations ---")
text = " Data Science "
print("Uppercase:", text.upper())
print("Strip spaces:", text.strip())
print("Substring (Slice):", text[1:5])
print("Concatenation:", text.strip() + " Lab")
print()

# D. List Operations
print("--- List Operations ---")
my_list = [1, 2, 3]
my_list.append(4)
my_list.extend([5, 6])
print("List after appends:", my_list)
my_list.remove(3)
print("After removing 3:", my_list)
print("Slicing list:", my_list[1:4])
print()

# E. Tuple Operations
print("--- Tuple Operations ---")
my_tuple = (10, 20, 30, 20)
print("Tuple:", my_tuple)
print("Count of 20:", my_tuple.count(20))
print("Index of 30:", my_tuple.index(30))
print()

# F. Dictionary Operations
print("--- Dictionary Operations ---")
my_dict = {"name": "Alice", "course": "Data Science"}
my_dict["year"] = 2026
print("Dictionary:", my_dict)
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))
print()

# G. Set Operations
print("--- Set Operations ---")
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
print("Union:", set_A.union(set_B))
print("Intersection:", set_A.intersection(set_B))
print("Difference (A - B):", set_A.difference(set_B))