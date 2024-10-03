#!/usr/bin/env python3

if __name__ == '__main__':

    name = input('Greetings! What is your name? ').capitalize()

    try:
        year_now = int(input('What year is it today? '))
        year_born = int(input('What year were you born? '))

        if year_now < year_born:
            print('Invalid input.')
        else:
            age = year_now - year_born

            print()
            print(f'Hello, {name}. It is good to meet you.')
            print(f'This year you will be {age} years old.')

    except ValueError:
        print('Invalid input.')
