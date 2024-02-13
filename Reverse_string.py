class Recursion:
    def __init__(self):
        self.s = input("Enter a string: ")

    def reverseString(self, index):
        if index < 0:
            return  # Base case: reached the end of the string

        print(self.s[index], end="")  # Print the current character
        self.reverseString(index - 1)  # Recursive call for the rest of the string

    def main(self):
        self.reverseString(len(self.s) - 1)  # Start recursion from the last character

if __name__ == "__main__":
    obj = Recursion()
    obj.main()
