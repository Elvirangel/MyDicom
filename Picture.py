import numpy as np
import pydicom
import matplotlib.pyplot as plt
import cv2

path="H:/PROJECTS/DICOM/DCM_source/29.dcm"
global listFilesDCM, fileNumber, imArray
RefDs = pydicom.read_file(path)
imArray = RefDs.pixel_array
# plt.imshow(imArray, cmap=plt.cm.bone)
plt.imsave("orginal1.jpg", imArray,cmap='gray')
imArray[imArray<100]=0
imArray = np.uint8(imArray)
cv2.imwrite("original22.jpg", imArray)
# plt.title("Oringal")
# plt.show()

# 图像的维度
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns))
# print(ConstPixelDims)

# 获取图像的标记，最小路径
I = imArray.copy()
