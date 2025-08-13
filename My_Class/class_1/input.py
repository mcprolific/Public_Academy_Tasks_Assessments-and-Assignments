# Basic usage of input()
name = input("Enter your fullname: ")
print("Hello,", name)


# Convert input to integer
# age = int(input("Enter your age: "))
# print(f"You will be {age + 1} years old next year.")

age = int(input("Pleae, don't forget enter your age: "))
print(f"This is your new  age {age} years old.")

# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
minus_result = num1 - num2
multip_result = num1 * num2
div_result = num1 / num2
print(f"The sum of {num1} and {num2} is {sum_result}.")
print(f"The minus of {num1} and {num2} is {minus_result}.")
print(f"The multiply of {num1} by {num2} is {multip_result}.")
print(f"The divide of {num1} by {num2} is {div_result}.")