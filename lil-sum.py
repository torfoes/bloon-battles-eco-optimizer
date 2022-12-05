import os
from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS

# open the image
image = Image.open("img.jpg")

# extracting the exif metadata
exifdata = image.getexif()

# looping through all the tags present in exifdata
for tagid in exifdata:
    # getting the tag name instead of tag id
    tagname = TAGS.get(tagid, tagid)

    # passing the tagid to get its respective value
    value = exifdata.get(tagid)

    # printing the final result
    print(f"{tagname:25}: {value}")


def change_file_names():
    # Get the current time
    current_time = datetime.now()

    # Get the name of the file that you want to rename
    filename = "my_file.txt"

    # Generate a new file name based on the current time
    new_filename = current_time.strftime("%Y-%m-%d_%H-%M-%S") + ".webp"

    # Rename the file
    os.rename(filename, new_filename)