import imutils
import cv2

def preprocess(image, width, height):
	# grab the dimension of the image,then
	# initiate the padding value
	(h, w) = image.shape[:2]
	if h > w:
		image = imutils.resize(image, height=height)

	else:
		image = imutils.resize(image, width=width)

	padH = int((height - image.shape[0]) / 2.0)
	padW = int((width - image.shape[1]) / 2.0)

	cv2.copyMakeBorder(image, padH, padH, padW, padW, cv2.BORDER_REPLICATE)
	image = cv2.resize(image, (width, height))

	return image
