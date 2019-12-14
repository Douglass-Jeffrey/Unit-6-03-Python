#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This gets random numbers then finds the smallest using an array

import random


def calculate(array_of_numbers):
    # This function finds the largest number from the given list

    # Variables
    smallest_array_num = 100

    # Process
    for repeater in array_of_numbers:
        if smallest_array_num > repeater:
            smallest_array_num = repeater

    # Output
    return smallest_array_num


def main():
    # This function creates an array and prints out all numbers from it

    # Array
    number_array = []

    # Adding numbers to an array
    for repeater in range(10):
        random_number = random.randint(1, 100)
        print("Random Number " + str(repeater + 1) + " is " +
              str(random_number))
        number_array.append(random_number)

    # Process
    smallest_number = calculate(number_array)

    # Output
    print("The smallest generated number in the array is: ", smallest_number)


if __name__ == "__main__":
    main()
