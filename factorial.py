#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: November, 2025
# This program asks the user for a number and finds the factorial


def main():
    # get user input and handle exceptions
    user_num = input("Please enter a positive integer: ")
    try:
        user_num = int(user_num)
        if user_num < 0:
            print("Please enter a positive integer.")
        else:
            # initialize counter and factorial answer
            counter = 0
            factorial_answer = 1

            # loop to calculate factorial
            while True:
                counter = counter + 1
                factorial_answer = factorial_answer * counter

                # break loop if counter is greater than or equal to user_num
                if counter >= user_num:
                    break

            # display output
            print("The factorial of", user_num, "is", factorial_answer)
    # exception handling
    except ValueError:
        print(user_num, "is not an integer.")

    # display end message
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
