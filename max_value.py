#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 26th, 2022.
# This program generates a 10 random number between 0 and 100. It then uses a
# loop to display what position the random number is and then displays the
# max value.
import constants
import random


def find_max_value(random_num):
    max_value = random_num[0]

    # determines the max value
    for counter in range(len(random_num)):
        if max_value < random_num[counter]:
            max_value = random_num[counter]
    return max_value


def main():
    # initialize counter
    counter = 0

    # create a list
    num_random = []

    # displays random numbers
    for counter in range(constants.MAX_SIZE):
        num_random.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))

        print("{} is added to the list at position {}"
              .format(num_random[counter], counter))

    # call function & display the max value
    max = find_max_value(num_random)
    print("")
    print("The max value is: {}".format(max))


if __name__ == "__main__":
    main()
