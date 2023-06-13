import cv2
import numpy as np
import imutils
import os

Datos = 'n'
if not os.path.exists(Datos):
	print('Carpeta creada: ', Datos)
	os.makedirs(Datos)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0
while True:

	ret, frame = cap.read()
	if ret == False:  break

	cv2.imshow('frame',frame)

	k = cv2.waitKey(1)
	if k == 27: 
		break

cap.release()
cv2.destroyAllWindows()