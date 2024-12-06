# stores all information related to converting image to diamond painting template
class ImageData:
    def __init__(self, image, square_length, palette, color_count, output):
        self.image = image # image file location
        self.square_length = square_length # desired pixel chunk size
        self.palette = palette # desired color palette for quantization or None
        self.color_count = color_count # number of colors in palette or desired number of colors for quantization
        self.output = output # name for output image file
