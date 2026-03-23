#Micah Trost
#March 23, 2026
#Number Summer

def sum_numbers_from_file():
    try:
        with open('numbers.txt', 'r') as file:
            total = 0
            for line in file:
                try:
                    number = int(line.strip())
                    total += number
                except ValueError:
                    print(f"Warning: '{line.strip()}' is not a valid integer and will be skipped.")
            print(f"The total of the numbers in the file is: {total}")
    except IOError:
        print("An error occurred while trying to read the file.")
    print('In the sum_numbers_from_file function')

if __name__ == '__main__':
    sum_numbers_from_file()