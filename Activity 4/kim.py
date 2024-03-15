
def generate_multiplication_table(number):
    """
    Generates multiplication table up to the given number.

    :param number: The number up to which the multiplication table should be generated.
    :return: None
    """
    # Loop through each number up to the given number
    for i in range(1, number + 1):
        # Loop through each number up to the given number again
        for j in range(1, number + 1):
            # Calculate the product of the two numbers
            product = i * j
            # Print the product in formatted table
            print(f"{i} x {j} = {product}")
        # Add a newline character to separate each row of the table
        print()

    # Call the function with a given  number
    generate_multiplication_table(12)
