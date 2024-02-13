class Recursion:
    def __init__(self):
        self.n = int(input())

    def tower_of_hanoi(self, num, src, helper, dest):
        if num == 1:
            print("Move disk 1 from source", src, "to destination", dest)
            return  # Optional

        self.tower_of_hanoi(num - 1, src, dest, helper)
        print("Move disk", num, "from source", src, "to destination", dest)
        self.tower_of_hanoi(num - 1, helper, src, dest)

    def main(self):
        source = "A"  # Define source, helper, and destination rods
        helper = "B"
        destination = "C"
        self.tower_of_hanoi(self.n, source, helper, destination)

if __name__ == "__main__":
    obj = Recursion()
    obj.main()
