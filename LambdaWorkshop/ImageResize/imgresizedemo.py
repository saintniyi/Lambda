import os
import sys
import uuid
import argparse
from urllib.parse import unquote_plus
from PIL import Image

def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail(tuple(x / 2 for x in image.size))
        image.save(resized_path)

def main():
    parser = argparse.ArgumentParser()
    # Set the default for the dataset argument
    parser.add_argument("image")
    parser.add_argument("resized_image")
    args = parser.parse_args()
    # Create a dictionary of the shell arguments
    resize_image(args.image, args.resized_image)

if __name__ == "__main__":
    main()
