import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
	rval, frame = vc.read()
else:
	rval = False
i=0
while rval:
	i+=1
	cv2.imshow("preview", frame)
	cv2.imwrite("frames/"+str(i)+".png", frame)
	rval, frame = vc.read()
cv2.destroyWindow("preview")