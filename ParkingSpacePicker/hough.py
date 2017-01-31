# Not very good at finding the lines in the parking lots
# this is just a basic run though
# we could try some image processing before sending it to the hough lines
import cv2
import numpy as np

img = cv2.imread('cat.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

# cv2.imwrite('houghlines5.jpg',img)
cv2.imshow('image', img)
cv2.waitKey(0)
