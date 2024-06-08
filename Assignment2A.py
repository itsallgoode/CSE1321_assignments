
# Name: Charles Goode
# Section: E01

print("[Image Encoding Checker]")

width = int(input("What is the image width? "))
height = int(input("What is the image height? "))
file_size = int(input("What is the file size (in bytes)? "))
print(" ")

if width <= 0 or height <= 0 or file_size <= 0:
    print("The information is invalid - please re-enter it.")
else:
    bits = file_size * 8
    pixels = width * height
    bpc = int(bits / (pixels * 4))

    if bpc in (8, 16, 32):
        print(f"The image is encoded with {bpc} bits per pixel")
    else:
        print("The information is invalid - please re-enter it")



