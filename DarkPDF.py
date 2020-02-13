
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

def toDark(image, threshold):
	grayscale = toGrayscale(image)
	arr = np.array(grayscale)

	for i in range(0,len(arr)):
		for j in range(0,len(arr[i])):
			if arr[i][j] >= threshold:
				arr[i][j] = 30
			else:
				arr[i][j] = 255
	return PIL.Image.fromarray(arr)

# Convert to dark mode and save pdf
print("\n+ Retrieving " + fileName)
images = convert_from_path(fileName)
darkImages = []


for i in range(0,len(images)):
	print("+ Converting page " + str(i+1))
	darkImages.append(toDark(images[i],125))



fileName = fileName.replace('.pdf','')
newFileName = fileName + "-dark.pdf"

print("+ Saving " + newFileName)
darkImages[0].save(newFileName,format='pdf',save_all=True,append_images=darkImages[1:])
darkImages[1].save('new.pdf')

