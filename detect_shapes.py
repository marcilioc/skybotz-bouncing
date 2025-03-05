# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import imutils
import cv2

def detectShapes(frame):
	# convert the image to grayscale, blur it slightly,
	# and threshold it
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

	# Shows B&W image for debugging
	# cv2.imshow('Geometric shapes', thresh)

	# find contours in the thresholded image and initialize the
	# shape detector
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	sd = ShapeDetector()

	# loop over the contours
	for c in cnts:
		# compute the center of the contour, then detect the name of the
		# shape using only the contour
		M = cv2.moments(c)
		cX = 0
		cY = 0
		shape = ''
		if M["m00"] == 0 :
			continue
		else:  
			cX = int((M["m10"] / M["m00"]))
			cY = int((M["m01"] / M["m00"]))
			shape = sd.detect(c)

		# multiply the contour (x, y)-coordinates by the resize ratio,
		# then draw the contours and the name of the shape on the image
		c = c.astype("float")
		c = c.astype("int")
		cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
		cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, (255, 255, 255), 2)

		# return the output image
		return frame
