#Micah Trost
#March 23, 2026
#Random Number Writer

import random
def write_random_numbers():
    
    num_of_randoms = int(input('How many random numbers do you want to write to the file? (up to 1000) '))
    if num_of_randoms > 1000:
        print('Please enter a number less than or equal to 1000.')
        return
    with open('random_numbers.txt', 'w') as file:
        for _ in range(num_of_randoms):
            random_number = random.randint(1, 500)
            file.write(f"{random_number}\n")
    print(f'{num_of_randoms} random numbers have been written to random_numbers.txt')

if __name__ == '__main__':
    write_random_numbers()