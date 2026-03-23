#Micah Trost
#March 23, 2026
#Item Counter

def count_file_lines():
    open_file = open('names.txt', 'r')
    print('The number of names in the file is:', len(open_file.readlines()))
    print('In the count_file_lines function')

if __name__ == '__main__':
    count_file_lines()