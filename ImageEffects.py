from PIL import Image

# increase abstraction of image by grouping pixels into pixel chunks and reducing image size
def pixelate(input_image, square_length, width, height):
    shrink_width = width // square_length
    shrink_height = height // square_length
    p_map = Image.new("RGB", (shrink_width, shrink_height), (0, 0, 0))

    for x in range(0, width, square_length):
        for y in range(0, height, square_length):
            square_r, square_g, square_b = 0, 0, 0

            for sub_x in range(x, x + square_length):
                for sub_y in range(y, y + square_length):
                    r, g, b, = input_image.getpixel((sub_x, sub_y))
                    square_r += r
                    square_g += g
                    square_b += b

            square_area = square_length * square_length
            square_r /= square_area
            square_g /= square_area
            square_b /= square_area

            p_map.putpixel((int(x / square_length), int(y / square_length)), (
            int(square_r), int(square_g), int(square_b)))

    return p_map