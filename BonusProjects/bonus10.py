while True:
    try:
        width = float(input("Enter width of the rectangle: "))
        length = float(input("Enter length of the rectangle: "))
        print()
        if width == length:
            print("Please enter dimensions of a rectangle. Not a square.")
            print()
            continue
        print("Here is the area of the rectangle: ", width * length)
        break
    except ValueError:
        print()
        print("Please enter a digit.")
        print()
        continue