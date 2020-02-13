
import numpy as np
import PIL
from pdf2image import convert_from_path, convert_from_bytes
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fileName',help='Name of the file to convert.')
args = parser.parse_args()

fileName = args.fileName

def invert(image):
	arr = np.array(image)
	for i in range(0,len(arr)):
		for j in range(0,len(arr[i])):
			arr[i][j] = 1 - arr[i][j]
	return PIL.Image.fromarray(arr)


# Convert to dark mode and save pdf
images = convert_from_path(fileName)
darkImages = []

for i in range(0,len(images)):
	invert(images[i])


