# Example Python file intentionally violating PEP 8 guidelines

# Violation 1: Importing multiple modules on the same line
import os,sys

# Violation 2: Constants should be in UPPER_CASE
my_constant = 42

# Violation 3: Class name should use CamelCase
class my_class:
    # Violation 4: Variables should be in snake_case
    def __init__(self):
        self.myProperty = None

    # Violation 5: Method name should be in snake_case
    def myMethod(self):
        print("This is my method!")

# Violation 6: Function name should be in snake_case
def my_function():
    print("Hello, World!")

# Violation 7: Inconsistent indentation
if True:
    print("Indented incorrectly.")  # Should be indented within the if block

# Violation 8: Missing docstring for function
def undocumented_function():
    pass

# Violation 9: Unused import
import unused_module

# Violation 10: Line length exceeds 79 characters
long_string = "This is a very long string that exceeds the recommended maximum line length of 79 characters in PEP 8 guidelines."

if __name__ == "__main__":
    print("Running as main program.")
