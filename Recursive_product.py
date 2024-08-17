def recursive_product(numbers):
    # Base case: when the list has only one number, return that number
    if len(numbers) == 1:
        return numbers[0]
    # Recursive case: multiply the first number by the product of the remaining numbers
    else:
        return numbers[0] * recursive_product(numbers[1:])

def get_user_input():
    numbers = []
    for i in range(5):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")
    return numbers

def main():
    print("Please enter five numbers to calculate their product.")
    numbers = get_user_input()
    result = recursive_product(numbers)
    print(f"The product of the numbers {numbers} is: {result}")

if __name__ == "__main__":
    main()
