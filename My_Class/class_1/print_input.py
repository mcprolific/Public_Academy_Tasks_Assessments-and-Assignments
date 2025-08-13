print("Hello World")

print('Alooma')
name = "Idris"
number1 = 2
number2 = 3
sum = number1 + number2
print(sum)

print("My name is" + " " + name)



# =======basic usage of print()==========
print("Hello, world!")
print("Welcome to Python programming.")



# =========using print() with variables========
name = "Aisha"
age = 25
print("Name:", name)
print("Age:", age)


# ========using f-strings with print()===========
name = "Bola"
score = 92
print(f"{name} scored {score} in the exam.")


# ========using string concatenation============
first_name = "Ada"
last_name = "Lovelace"
print("Full name: " + first_name + " " + last_name)

# =======Comma vs concatenation=======
# with comm
print("Hello", "world!", "My People")
# with concatenation
print("Hello" + " " + "world!")



# Newline (\n)
print("This is my first code in Python\nLet's learn together!!!")


# Tab (\t)
print("Name\tAge\tLocation")

print("FirstName\tLastName\tEmail\tPassword")
print("Saka\tIdris\tsaka@gmail.com\t12345Sa")

# Quote inside string
print("He said, \"Hello my friend!\"")
print('It\'s a sunny day.')

# Backslash
print("File path: C:\\Users\\Aisha\\Documents")

# Carriage return (\r)
print("123456\rABC")  # Output: ABC456 (replaces 123)

# Backspace (\b)
print("Helloo\b")  # Output: Hello

# Bell/alert (may or may not beep depending on environment)
print("\a")  # Triggers a bell sound (if supported)