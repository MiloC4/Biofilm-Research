from PIL import Image

from HelperCode.ImageEffects import pixelate

# import desired image python file
from PaintingsData.StarryNight import starry_night

# select python file to produce diamond painting from
selected_image = starry_night

square_length = selected_image.square_length

# access image and crop it to perfectly fit desired pixel chunk size
input_image = Image.open(selected_image.image)

init_width, init_height = input_image.size

width = init_width - (init_width % square_length)
height = init_height - (init_height % square_length)

input_image = input_image.crop((0, 0, width, height))

# increase abstraction of image by grouping pixels into pixel chunks and reducing image size
pixel_map = pixelate(input_image, square_length, width, height)

# quantize pixel_map image; Use palette if provided
if selected_image.palette is not None:
    palette = selected_image.palette

    color_count = selected_image.color_count
    num_bands = len("RGB")
    num_entries = len(palette) // num_bands
    palette.extend(palette[:num_bands] * (color_count - num_entries))

    arbitrary_size = 16, 16
    pal_image = Image.new('P', arbitrary_size)
    pal_image.putpalette(palette)

    pixel_map = pixel_map.quantize(palette=pal_image)
else:
    pixel_map = pixel_map.quantize(colors=selected_image.color_count, method=2, dither=Image.Dither.RASTERIZE)

# re-size image to original size
pixel_map = pixel_map.resize((width, height))

# save diamond painting
pixel_map.save("Outputs/" + selected_image.output, format="png")

# display diamond painting
pixel_map.show()