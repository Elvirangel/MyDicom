import os
import pydicom
import numpy as np
import matplotlib.pyplot as plt
from Point import Point
import random

pathDicom = "DCM_source"

sX, sY = (138, 129)
cost = 0
iters = 2000
threshold=100


# 设置
# temp=np.array([[1,0.5,1],[2,0,2],[1,0.5,1]],dtype=float)
temp = np.array([[1, 0.5, 1], [4, 0, 4], [1, 0.5, 1]], dtype=float)
print(id(temp))
alph = 0.02
temp = temp * alph
temp.tolist()
print(id(temp))
print(temp)

# 读取文件夹内图像列表
listFilesDCM = []
fileNumber = 0

for diName, subdirList, fileList in os.walk(pathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():
            print(filename)
            listFilesDCM.append(os.path.join(diName, filename))

# 获取指定序号的图像内容
RefDs = pydicom.read_file(listFilesDCM[fileNumber])
imArray = RefDs.pixel_array
plt.imshow(imArray, cmap=plt.cm.bone)
plt.show()

# 图像的维度
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns))
print(ConstPixelDims)

MaxPoint = Point(0, sX, sY, imArray[sX][sY])
MinPoint = Point(0, sX, sY, imArray[sX][sY])
PointList = []

I = imArray.copy()
flag = np.empty((512, 512), dtype=bool)
flag[:, :] = False
minPath = np.zeros((512, 512))
plt.imshow(minPath, cmap=plt.cm.bone)
plt.show()


LinYu = np.zeros((3, 3))


def findLY(sX, sY):
    lis = []
    LinYu[:, :] = 0
    k = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            LinYu[1 + i, 1 + j] = imArray[sX + i, sY + j]
            ll = Point(k, sX + i, sY + j, imArray[sX + i, sY + j])
            lis.append(ll)
            k += 1
    # print(LinYu)
    # return lis,LinYu
    return lis


lis = findLY(sX, sY)

for i in lis:
    i.displayPiont()


def normalLY(lis):

    minpix = min(lis, key=lambda ll: ll.pix).pix
    maxpix = max(lis, key=lambda ll: ll.pix).pix
    mm = maxpix - minpix

    k = 0
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            lis[k].pix = (lis[k].pix - minpix) * 1.0 / mm + temp[i][j]
            k += 1

    lis.sort(key=lambda ll: ll.pix, reverse=True)
    '''
    for i in range(0,3):
        for j in range(0,3):
            LinYu[i][j]=(LinYu[i][j]-minpix) * 1.0 / mm +temp[i][j]
    '''

    # return lis,LinYu
    return lis


# lis,LinYu=normalLY(lis)
lis = normalLY(lis)


for i in lis:
    i.displayPiont()




Find = True
pointfind = 0
curLY = []
N = 0
curPoint = Point(0, sX, sY, 0)
flag[sX][sY] = True
minPath[sX][sY] = 1
# 栈存储访问过的点
invisted = []
invistPoint = Point(1, sX, sY, imArray[sX][sY])
invisted.append(invistPoint)
rap = 0
id = 1


def findPoint(sX,sY):
    global imArray,flag,id
    Find = False
    curPoint=Point(id,sX,sY,imArray[sX,sY])
    curLY = findLY(sX, sY)
    curLY = normalLY(curLY)
    for i in range(0, 8):
        point = curLY[i]
        sX = point.x
        sY = point.y
        if flag[sX][sY] == False and imArray[sX][sY] > threshold:
            curPoint = curLY[i]
            flag[sX][sY] = True
            Find=True
            break
    return curPoint,Find


# while(N < iters):
#     Find = False
#     curLY = findLY(sX, sY)
#     curLY = normalLY(curLY)
#     for i in range(0, 8):
#         point = curLY[i]
#         sX = point.x
#         sY = point.y
#         if flag[sX][sY] == False and imArray[sX][sY] > threshold:
#             curPoint = curLY[i]
#             flag[sX][sY] = True
#             if curPoint.x > MaxPoint.x:
#                 MaxPoint = curPoint
#             if curPoint.x < MinPoint.x:
#                 MinPoint = curPoint
#             Find = True
#             invistPoint = curPoint
#             invistPoint.pix = imArray[sX][sY]
#             invistPoint.id = id + 1
#             invisted.append(invistPoint)
#             break
while(N<iters):
    curPoint,Find=findPoint(sX,sY)
    if Find==True:
        if curPoint.x > MaxPoint.x:
            MaxPoint = curPoint
        if curPoint.x < MinPoint.x:
            MinPoint = curPoint
        invistPoint = curPoint
        invistPoint.pix = imArray[sX][sY]
        invistPoint.id = id + 1
        invisted.append(invistPoint)

    if Find == False and rap < 500:
        #print("rap:", rap)
        sX, sY = MaxPoint.x, MaxPoint.y
        pointfind = 1
        rap += 1

    elif Find == False and rap >= 500:
        print("ttttttttttrap:", rap)
        point = invisted[random.randint(0, len(invisted)-1)]
        sX, sY = point.x, point.y
        pointfind = 1
        rap += 1

    cost += curPoint.pix
    print(cost)
    minPath[sX][sY] = 1
    N += 1


plt.imshow(minPath, cmap=plt.cm.bone)
plt.imsave("testminPath.jpg", minPath, cmap=plt.cm.bone)
plt.show()
