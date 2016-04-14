import numpy as np
import cv2

def nothing(x):
	pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Color")

iLowH = 0
iHighH = 179

iLowS = 0
iHighS = 255

iLowV = 0
iHighV = 255

cv2.createTrackbar("LowH", "Color", iLowH, 179, nothing); #Hue (0 - 179)
cv2.createTrackbar("HighH", "Color", iHighH, 179, nothing);

cv2.createTrackbar("LowS", "Color", iLowS, 255, nothing); #Saturation (0 - 255)
cv2.createTrackbar("HighS", "Color", iHighS, 255, nothing);

cv2.createTrackbar("LowV", "Color", iLowV, 255, nothing); #Value (0 - 255)
cv2.createTrackbar("HighV", "Color", iHighV, 255, nothing);

while(True):
	iLowH = cv2.getTrackbarPos('LowH','Color')
	iHighH = cv2.getTrackbarPos('HighH','Color')

	iLowS = cv2.getTrackbarPos('LowS','Color')
	iHighS = cv2.getTrackbarPos('HighS','Color')

	iLowV = cv2.getTrackbarPos('LowV','Color')
	iHighV = cv2.getTrackbarPos('HighV','Color')

	ret, frame = cap.read()
	
	imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	imgThresholded = cv2.inRange(imgHSV, (iLowH, iLowS, iLowV), (iHighH, iHighS, iHighV))
	
	imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)));
	imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)));
	
	imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))); 
	imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)));
		
	cv2.imshow("Thresholded Image", imgThresholded); #show the thresholded image
	cv2.imshow("Original", frame); #show the original image
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()