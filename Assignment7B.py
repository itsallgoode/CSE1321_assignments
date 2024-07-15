class Pixel:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def changeRGB(self, new_red, new_green, new_blue):
        self.red = new_red
        self.green = new_green
        self.blue = new_blue

    def printRGB(self):
        print(f"{self.red} {self.green} {self.blue}", end=' ')


class Assignment7B:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.image = []
    
    def main(self):
        print("[Portable Pix Map Art Program]")
        width = int(input("Enter an image width: "))
        height = int(input("Enter an image height: "))
        red = int(input("Enter the fill color's red value: "))
        green = int(input("Enter the fill color's green value: "))
        blue = int(input("Enter the fill color's blue value: "))
        print()

        self.create_image(width, height, red, green, blue)

        while True:

            print("What will you do?")
            print("1) Fill in a pixel")
            print("2) Fill in a line")
            print("3) Print the image")
            print("4) Quit")
            choice = int(input("Choice? "))
            print()

            if choice == 1:
                row = int(input("Row: "))
                column = int(input("Column: "))
                red = int(input("New Red Color: "))
                green = int(input("New Green Color: "))
                blue = int(input("New Blue Color: "))
                print()
                self.fill_pixel(row, column, red, green, blue)

            elif choice == 2:
                row = int(input("Row: "))
                column = int(input("Column: "))
                length = int(input("Length: "))
                red = int(input("New Red Color: "))
                green = int(input("New Green Color: "))
                blue = int(input("New Blue Color: "))
                print()
                self.fill_row(row, column, length, red, green, blue)

            elif choice == 3:
                self.print_image()

            elif choice == 4:
                self.print_image()
                print("Closing...")
                break
        
    def create_image(self, width, height, red, green, blue):
        self.width = width
        self.height = height
        self.image = [[Pixel(red, green, blue) for _ in range(width)] for _ in range(height)]

    def print_image(self):
        print("P3")
        print(f"{self.width} {self.height}")
        print("255")
        for row in self.image:
            for pixel in row:
                pixel.printRGB()
            print()
        print()
    
    def fill_pixel(self, row, column, new_red, new_green, new_blue):
        self.image[row][column].changeRGB(new_red, new_green, new_blue)
    
    def fill_row(self, row, column, length, new_red, new_green, new_blue):
        for i in range(length):
            self.image[row][column + i].changeRGB(new_red, new_green, new_blue)
        
        
Assignment7B().main()
