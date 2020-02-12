
import numpy as np
import PIL
from pdf2image import convert_from_path, convert_from_bytes
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fileName',help='Name of the file to convert.')
args = parser.parse_args()

fileName = args.fileName

# Util Functions
def toGrayscale(image):
	grayscale = image.convert("L")
	return grayscale

def invert(image, threshold):
	grayscale = toGrayscale(image)
	arr = np.array(grayscale)

	for i in range(0,len(arr)):
		for j in range(0,len(arr[i])):
			if arr[i][j] >= threshold:
				arr[i][j] = 20
			else:
				arr[i][j] = 255
	return PIL.Image.fromarray(arr)


# Convert to dark mode and save pdf
images = convert_from_path(fileName)
darkImages = []

for i in range(0,len(images)):
	darkImages.append(invert(images[i],125))


firstImage = darkImages.pop(0)

fileName = fileName.replace('.pdf','')
newFileName = fileName + "-dark.pdf"

firstImage.save(newFileName,append_images=darkImages)

