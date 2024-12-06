from HelperCode.ImageData import ImageData

starry_night_palette = [
            245, 237, 252,
            223, 194, 246,
            201, 151, 240,
            178, 108, 233,
            156, 66, 227,
            133, 30, 213,
            106, 24, 171,
            80, 18, 128,
            53, 12, 85,
            26, 6, 42,
            255, 255, 255
        ]

starry_night = ImageData(
    image="images/white.jpg", # image file location
    square_length=20, # desired pixel chunk size
    palette=starry_night_palette, # desired color palette for quantization or None
    color_count=20, # number of colors in palette or desired number of colors for quantization
    output="StarryNight" # name for output image file
)