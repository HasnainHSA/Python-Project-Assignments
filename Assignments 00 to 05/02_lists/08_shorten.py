# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, 
# which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. 
# We've written a main() function for you which gets a list and passes it into your 
# function once you run the program. For the autograder to pass you will need 
# MAX_LENGTH to be 3, but feel free to change it around to test your program.

MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print("Removed:", removed)

def main():
    lst = []
    while True:
        item = input("Enter a list item (or just press enter to finish): ")
        if item == "":
            break
        lst.append(item)

    print("Original list:", lst)
    shorten(lst)
    print("Shortened list:", lst)

if __name__ == '__main__':
    main()
