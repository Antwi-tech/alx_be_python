# oop/class_static_methods_demo.py

class Calculator:
    """
    Calculator class demonstrating the use of static methods and class methods.
    """

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        Does not depend on class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that returns the product of two numbers.
        Prints the calculation type using the class attribute.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
