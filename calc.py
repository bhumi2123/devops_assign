def add(num1, num2):
  """Performs addition and returns the result."""
  return num1 + num2

def subtract(num1, num2):
  """Performs subtraction and returns the result."""
  return num1 - num2

def multiply(num1, num2):
  """Performs multiplication and returns the result."""
  return num1 * num2

def divide(num1, num2):
  """Performs division and returns the result, handling division by zero."""
  if num2 == 0:
    return "Error: Division by zero is not allowed."
  else:
    return num1 / num2

def calculate(num1, operator, num2):
  """Calculates based on the provided operator and returns the result."""
  if operator == "+":
    return add(num1, num2)
  elif operator == "-":
    return subtract(num1, num2)
  elif operator == "*":
    return multiply(num1, num2)
  elif operator == "/":
    return divide(num1, num2)
  else:
    return "Error: Invalid operator."

def get_number(prompt):
  """Gets a valid number input from the user and returns it."""
  while True:
    try:
      number = float(input(prompt))
      return number
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_operator():
  """Gets a valid operator input from the user and returns it."""
  while True:
    operator = input("Enter an operator (+, -, *, /): ")
    if operator in "+-*/":
      return operator
    else:
      print("Invalid operator. Please enter +, -, *, or /.")

def main():
  """Main function that drives the calculator program."""
  print("Welcome to the Python Calculator!")

  while True:
    # Get first number
    num1 = get_number("Enter the first number: ")

    # Get operator
    operator = get_operator()

    # Get second number
    num2 = get_number("Enter the second number: ")

    # Perform calculation
    result = calculate(num1, operator, num2)

    # Display result
    print("Result:", result)

    # Ask if user wants to continue
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != 'y':
      break

  print("Thank you for using the calculator!")

if __name__ == "__main__":
  main()
