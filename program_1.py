#Micah Trost
#March 23, 2026
#Name Counter

def count_file_lines():
    try:
        with open('names.txt', 'r') as file:
            line_count = sum(1 for line in file)
            print(f'The number of names in the file is: {line_count}')
    except IOError:
        print("An error occurred while trying to read the file.")

if __name__ == '__main__':
    count_file_lines()