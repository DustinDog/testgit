# create python code 30 lines long
import random
def generate_random_numbers(count, lower_bound, upper_bound):
    """Generate a list of random numbers within a specified range."""
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        return None
    return max(numbers)

def find_minimum(numbers):
    """Find the minimum number in a list."""
    if not numbers:
        return None
    return min(numbers)
def main():
    # Generate a list of 10 random numbers between 1 and 100
    random_numbers = generate_random_numbers(10, 1, 100)
    
    print("Random Numbers:", random_numbers)
    
    # Calculate average
    average = calculate_average(random_numbers)
    print("Average:", average)
    
    # Find maximum
    maximum = find_maximum(random_numbers)
    print("Maximum:", maximum)
    
    # Find minimum
    minimum = find_minimum(random_numbers)
    minimum = find_minimum(random_numbers)
    minimum = find_minimum(random_numbers)
    print("Minimum:", minimum)