#Brian Webb
#ITEC209




try:
    with open('numbers.txt', 'r') as file:
        numbers = []
        for line in file:
            try:
                number = int(line)
                numbers.append(number)
            except ValueError:
                print(f"Warning: Invalid number '{line.strip()}' in file")
        if numbers:
            average = sum(numbers) / len(numbers)
            print(f"The average of the numbers is {average}")
        else:
            print("Error: No valid numbers found in file.")
except IOError:
    print("Error: File not found or could not be read.")
