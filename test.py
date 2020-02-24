import numpy as np
import cv2
import pydicom

path="H:/PROJECTS/DICOM/DCM_source/29.dcm"

RefDs=pydicom.read_file(path)
imArray=RefDs.pixel_array
print((imArray).shape)
# 必须转换成uint8
#imArray=cv2.imread("H:/PROJECTS/DICOM/newImage22.png",0)
imArray = np.uint8(imArray)
cv2.imshow("imArray",imArray)

ret,thresh=cv2.threshold(imArray,100,1024,cv2.THRESH_BINARY)
cv2.imshow("threshold",thresh)


image,contours,hier=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
black = cv2.cvtColor(np.zeros((imArray.shape[0], imArray.shape[1]), dtype=np.uint8), cv2.COLOR_GRAY2BGR)

cv2.namedWindow("Contours",0)
cv2.resizeWindow("Contours",360,256)
cv2.drawContours(black,contours,-1,(255,0,0,2),1)
cv2.imshow("Contours",black)
cv2.imwrite("29.jpg",thresh)
cv2.waitKey()