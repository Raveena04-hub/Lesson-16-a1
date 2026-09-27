def sum_of_whole_numbers(n):
    """
    Function to calculate the sum of whole numbers from 1 to n.
    Argument:
        n (int): The upper limit of whole numbers.
    Returns:
        int: The sum of numbers from 1 to n.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage:
num = int(input("Enter a whole number: "))
print("The sum of whole numbers up to", num, "is:", sum_of_whole_numbers(num))
