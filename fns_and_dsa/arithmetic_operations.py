def perform_operation(num1, num2 , operation ):
    """
    Performs basic arithmetic operations based on the provided operation string.

    Parameters:
        num1: First number
        num2: Second number
        operation: One of 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        The result of the operation, or an error message string
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero error"
        return num1 / num2
    else:
        return "Invalid operation"
