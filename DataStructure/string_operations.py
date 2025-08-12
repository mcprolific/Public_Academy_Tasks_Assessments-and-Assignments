# Indexing Operations Strings
print("Examples for Indexing Operations Strings!!!")
word = "Python is my best program"
print(word[0])  # P
print(word[-1]) # n for Python
print(word[2]) # t
print(word[-1]) # m

# Slicing Operation Strings
print("Examples for Slicing Operation Strings!!!")
word = "Python"
print(word[0:4])   # Pyth
print(word[2:])    # thon
print(word[:3])    # Pyt
print(word[::2])   # Pto
print(word[::-1])
print(word[2:5])

# String Concatenation & Repetition

# Concatenation
print("Example for Concatenations")
a = "Hello"
b = "World"
print(a + " " + b)  # Hello World


# Repetition
word = "Hi! "
print(word * 3)  # Hi! Hi! Hi!

# String Searching & Checking


# Membership
text = "Python programming"
print("Python" in text)   # True
print("Java" not in text) # True

# find() / rfind()
text = "Hello World"
print(text.find("o"))   # 4
print(text.rfind("o"))  # 7


# index() / rindex()
# (Like find() but raises an error if not found)

text = "Hello World"
print(text.index("World"))   # 6


# startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data"))  # True
print(filename.endswith(".csv"))    # True


# String Methods
# Creating and manipulating strings.

#   - upper()
#   - lower()
#   - title()
#   - strip()
#   - replace()