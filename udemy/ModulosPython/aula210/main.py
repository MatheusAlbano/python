
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.jpeg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpeg'

pil_image = Image.open(ORIGINAL)

width, height = pil_image.size
exif = pil_image.info['exif']

# width ... new width
# height ... ??
new_width = 640
new_height = round(new_width * height/ width)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    exif=exif,
)
