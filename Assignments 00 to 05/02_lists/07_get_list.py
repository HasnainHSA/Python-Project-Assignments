# Problem Statement
# Write a program which continuously asks the user to enter values which are added 
# one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


def main():
    values = []

    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)

    print("Here's the list:", values)

if __name__ == '__main__':
    main()
