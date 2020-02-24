import numpy as np
import os
import pydicom
import matplotlib.pyplot as plt
import math
from Point import Point
import cv2

# pathDicom = "DCM_source"
#
# # 22.dcm
# # sX, sY = (188, 0)
# # 25.dcm
# #sX, sY = (188, 0)
# cost = 0
# iters = 1000
# threshold = 200
#
# # 读取文件夹内图像列表
# listFilesDCM = []
# fileNumber = 6
#
# for diName, subdirList, fileList in os.walk(pathDicom):
#     for filename in fileList:
#         if ".dcm" in filename.lower():
#             print(filename)
#             listFilesDCM.append(os.path.join(diName, filename))
#
# # 获取指定序号的图像内容
# RefDs = pydicom.read_file(listFilesDCM[fileNumber])
# imArray = RefDs.pixel_array
# # plt.imshow(imArray, cmap=plt.cm.bone)
# plt.imsave("oringal",imArray)
# # plt.title("Oringal")
# # plt.show()
#
# # 图像的维度
# ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns))
# # print(ConstPixelDims)
#
# # 获取图像的标记，最小路径
# I = imArray.copy()
# flag = np.empty((256, 360), dtype=bool)
# flag[:, :] = False
# minPath = np.zeros((512, 512))
#
# # plt.figure(figsize=(10,10))
# # plt.imshow(minPath, cmap=plt.cm.bone)
# # plt.title("MinPath")
# # plt.show()
#
# # 获取展开的图像
# newImage = np.zeros((256, 360))
# # plt.imshow(newImage, cmap=plt.cm.bone)
# # plt.title("new Image")
# # plt.show()
#
#
# # 设置阈值
# # I[I<threshold]=0
# for eta in range(0, 360):
#     for l in range(0, 256):
#         x, y = computeTangel(l, eta)
#         newImage[l][eta]=I[x][y]
#         # 如果imshow(origin='lower')没设置，则对图像进行上下翻转l=255-l，更好观察
#         # newImage[255 - l][eta] = I[x][y]
#
# print(max(newImage[:][0]))
# plt.figure()
# plt.imshow(newImage, cmap=plt.cm.gray,origin='lower')
# plt.title("new Image3")
# # plt.imsave("new Image3",newImage)
# # plt.savefig("new Image.png",bbox_inches='tight')
# # cv2.imwrite("newImage22.png",newImage)
# # plt.show()
#
# # l=255-max(newImage[:][0])
# # sX,sY=computeTangel(l,0)
# # print(sX,sY)
#
#
#
#
#
#
#
#
# # 寻找初始点
# for l in range(255,0,-1):
#     if newImage[l][0]>threshold:
#         sX,sY=l,0
#         break
#
#
#
#
# N=0
# id=1
# cost=0
# minPath2=np.zeros((256,360))
# minPath2[sX][0]=1
# flag[sX][sY]=True
# etaMaxPoint=Point(id,sX,sY,newImage[sX,sY])
# vistedPointList=[]
# prePoint=np.empty((256,360),dtype=list)
# prePoint[sX][sY]=(sX,sY)
# while(N<iters):
#     curPoint,Find,tag=findPoint(sX,sY)
#     print("Find:",Find)
#     if Find==True:
#         sX,sY=curPoint.x,curPoint.y
#         id+=1
#         if sY>etaMaxPoint.y:
#             etaMaxPoint.id,etaMaxPoint.x,etaMaxPoint.y=id,sX,sY
#         minPath2[sX][sY]=1
#         vistedPointList.append(curPoint)
#         prePoint[sX][sY]=(sX,sY)
#     elif Find==False and sX==etaMaxPoint.x and sY==etaMaxPoint.y:
#         linYuMax=findLY(sX,sY)[0]
#         sX,sY=linYuMax.x,linYuMax.y
#     else:
#         print("curPint:")
#         curPoint.displayPiont()
#         # if etaMaxPoint.y+1<360:
#         #     sX,sY=etaMaxPoint.x,etaMaxPoint.y+1
#         sX, sY = etaMaxPoint.x, etaMaxPoint.y
#         print("sX,sY:",sX,sY)
#     cost+=newImage[sX][sY]
#     print("cost:",cost)
#     N+=1
#
#     if etaMaxPoint.y==359:
#         break
#
# print("N is:",N)
#
# plt.figure()
# plt.imshow(minPath2,cmap='gray',origin='lower')
# plt.title("minPath2")
# #plt.show()
#
#
#
# l=255-np.argmax(newImage[:][0])
# sX,sY=1,0
# print(sX,sY)
#
#
# # 映射回原图像
# for eta in range(0,360):
#     for l in range(0,256):
#         if minPath2[l][eta]==1:
#             x,y=computeTangel(l,eta)
#             minPath[x][y]=1
#
# plt.figure()
# plt.imshow(minPath,cmap='gray',origin='lower')
# plt.show()
#
#
# # # 绘制点图
# # X=[]
# # Y=[]
# # for eta in range(0,360):
# #     for l in range(0,256):
# #         if minPath2[l][eta]==1:
# #             x,y=computeTangel(l,eta)
# #             X.append(x)
# #             Y.append(y)
#
#
#
# plt.figure(4)
# #plt.figimage(imArray,origin='upper',alpha=1)
# plt.imshow(newImage,cmap='gray',origin='upper',alpha=1)
# plt.imshow(minPath2,cmap='YlGn',origin='upper',alpha=0.4)
# #plt.scatter(Y,X,c='r',s=1,)
# plt.show()
#
#
# plt.figure(5)
# #plt.figimage(imArray,origin='upper',alpha=1)
# plt.imshow(imArray,cmap='gray',origin='upper',alpha=1)
# plt.imshow(minPath,cmap='YlGn',origin='upper',alpha=0.4)
# #plt.scatter(Y,X,c='r',s=1,)
# plt.show()
#
# plt.figure(6)
# plt.imshow(flag)
# plt.show()


def computeTangel(l, eta):
    # if eta >= 0 and eta < 90:
    #     eta = eta * math.pi / 180
    #     SX = 255 - l * math.cos(eta)
    #     SY = 255 + l * math.sin(eta)
    # elif eta >= 90 and eta < 180:
    #     eta = eta * math.pi / 180
    #     SX = 255 - l * math.cos(eta)
    #     SY = 255 + l * math.sin(eta)
    # elif eta >= 180 and eta < 270:
    #     eta = eta * math.pi / 180
    #     SX = 255 - l * math.cos(eta)
    #     SY = 255 + l * math.sin(eta)
    # elif eta >= 270 and eta < 360:
    #     eta = eta * math.pi / 180
    #     SX = 255 - l * math.cos(eta)
    #     SY = 255 + l * math.sin(eta)
    # else:
    #     SX = 0
    #     SY = 0
    #     print("some wrong accur!!!")
    # 对四种角度进行总结之后，相同的公式
    eta=eta*math.pi/180
    SX=255-l*math.cos(eta)
    SY=255+l*math.sin(eta)
    return math.ceil(SX), math.ceil(SY)


def computeCoord(l,eta):
    l=255-l
    eta=eta*math.pi/180
    SX=255-l*math.cos(eta)
    SY=255+l*math.sin(eta)
    return math.ceil(SX), math.ceil(SY)


def findLY(sX, sY):
    global imArray,newImage
    lis = []
    LinYu = np.zeros((3, 3))
    LinYu[:, :] = 0
    k = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            LinYu[1 + i, 1 + j] = imArray[sX + i, sY + j]
            if sX + i>=0 and sX+i<256 and sY+j>=0 and sY+j<360 :
                # ll = Point(k, sX + i, sY + j, newImage[sX + i, sY + j])
                ll = Point(k, sX + i, sY + j, newImage[sX + i, sY + j]*temp[1 + i, 1 + j])
            else:
                ll = Point(k, sX, sY, newImage[sX, sY])
            if i!=0 or j!=0:
                lis.append(ll)
                k += 1
    lis.sort(key=lambda ll: ll.pix, reverse=True)

    for i in lis:
        i.displayPiont()
    return lis


def normalLY(lis):

    minpix = min(lis, key=lambda ll: ll.pix).pix
    maxpix = max(lis, key=lambda ll: ll.pix).pix
    mm = maxpix - minpix

    k = 0
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            lis[k].pix = (lis[k].pix - minpix) * 1.0 / mm
            k += 1

    lis.sort(key=lambda ll: ll.pix, reverse=True)
    '''
    for i in range(0,3):
        for j in range(0,3):
            LinYu[i][j]=(LinYu[i][j]-minpix) * 1.0 / mm +temp[i][j]
    '''

    # return lis,LinYu
    return lis

def LY(sX,sY):
    global prePoint
    x,y=prePoint[sX][sY]
    list1=findLY(x,y)
    list2=findLY(sX,sY)
    # x,y=prePoint[x][y]
    # list3=findLY(x,y)
    list1.extend(list2)
    # list1.extend(list3)
    list1.sort(key=lambda ll: ll.pix, reverse=True)
    return list1


# def findPoint(sX,sY):
#     global imArray,flag,id,newImage,etaMaxPoint,vistedPointList
#     Find = False
#     tag=0
#     curPoint=Point(id,sX,sY,newImage[sX,sY])
#     curLY = findLY(sX, sY)
#     for i in range(0, 8):
#         tag+=1
#         point = curLY[i]
#         sX = point.x
#         sY = point.y
#         if flag[sX][sY] == False and sY>etaMaxPoint.y:
#             curPoint = curLY[i]
#             flag[sX][sY] = True
#             Find=True
#             break
#     if tag==8:
#         print("没找到，选最大值！！！！")
#         #curPoint=curLY[0]
#         curPoint=vistedPointList[-10]
#         curPoint.displayPiont()
#         Find=True
#         flag[sX][sY]=True
#     return curPoint,Find,tag


def findPoint(sX,sY):
    global imArray,flag,id,newImage,etaMaxPoint,vistedPointList
    Find = False
    tag=0
    curPoint=Point(id,sX,sY,newImage[sX,sY])
    curLY = findLY(sX, sY)
    for i in range(0, 8):
        tag+=1
        point = curLY[i]
        X = point.x
        Y = point.y
        if flag[X][Y] == False and newImage[sX][sY]>0 and Y>=etaMaxPoint.y:
        #if flag[sX][sY] == False and newImage[sX][sY]>=threshold and sY>etaMaxPoint.y:
            curPoint = curLY[i]
            flag[X][Y] = True
            Find=True
            break
    # if tag==16:
    #     print("没找到，选最大值！！！！")
    #     #curPoint=curLY[0]
    #     curPoint=vistedPointList[-10]
    #     curPoint.displayPiont()
    #     Find=True
    #     flag[sX][sY]=True
    return curPoint,Find,tag


def findStartPoint():
    global newImage,threshold
    for l in range(255, 0, -1):
        if newImage[l][0] > threshold:
            sX, sY = l, 0
            break
    return sX,sY


def readFile():
    global listFilesDCM,fileNumber,imArray
    RefDs = pydicom.read_file(listFilesDCM[fileNumber])
    imArray = RefDs.pixel_array
    # plt.imshow(imArray, cmap=plt.cm.bone)
    plt.imsave("oringal", imArray)
    # plt.title("Oringal")
    # plt.show()

    # 图像的维度
    ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns))
    # print(ConstPixelDims)

    # 获取图像的标记，最小路径
    I = imArray.copy()

def readOneFile(path):
    global imArray
    RefDs = pydicom.read_file(path)
    imArray = RefDs.pixel_array
    # plt.imshow(imArray, cmap=plt.cm.bone)
    plt.imsave("Sobel_Original.jpg", imArray)
    # plt.title("Oringal")
    # plt.show()

    # 图像的维度
    ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns))
    # print(ConstPixelDims)

    # 获取图像的标记，最小路径
    I = imArray.copy()


def main():
    global listFilesDCM,fileNumber,cost,N
    global flag,minPath,minPath2,newImage,prePoint,etaMaxPoint,imArray,threshold

    # 获取指定序号的图像内容
    readFile()
    I = imArray.copy()

    # 初始化标记数组，最小路径数组
    flag = np.empty((256, 360), dtype=bool)
    flag[:, :] = False
    minPath = np.zeros((512, 512))


    # 获取展开的图像
    newImage = np.zeros((256, 360))

    # 设置阈值
    #I[I<threshold]=0
    for eta in range(0, 360):
        for l in range(0, 256):
            x, y = computeTangel(l, eta)
            newImage[l][eta] = I[x][y]
            # 如果imshow(origin='lower')没设置，则对图像进行上下翻转l=255-l，更好观察
            # newImage[255 - l][eta] = I[x][y]



    # 寻找初始点
    sX,sY=findStartPoint()

    N = 0
    id = 1
    cost = 0
    minPath2 = np.zeros((256, 360))
    minPath2[sX][0] = 1
    flag[sX][sY] = True
    etaMaxPoint = Point(id, sX, sY, newImage[sX, sY])
    vistedPointList = []
    prePoint = np.empty((256, 360), dtype=list)
    prePoint[sX][sY] = (sX, sY)

    while (N < iters):
        curPoint, Find, tag = findPoint(sX, sY)
        print("Find:", Find)
        if Find == True:
            sX, sY = curPoint.x, curPoint.y
            id += 1
            if sY > etaMaxPoint.y:
                etaMaxPoint.id, etaMaxPoint.x, etaMaxPoint.y = id, sX, sY
            minPath2[sX][sY] = 1
            vistedPointList.append(curPoint)
            prePoint[sX][sY] = (sX, sY)
        elif Find == False and sX == etaMaxPoint.x and sY == etaMaxPoint.y:
            linYuMax = findLY(sX, sY)[0]
            sX, sY = linYuMax.x, linYuMax.y
        else:
            print("curPint:")
            curPoint.displayPiont()
            # if etaMaxPoint.y+1<360:
            #     sX,sY=etaMaxPoint.x,etaMaxPoint.y+1
            sX, sY = etaMaxPoint.x, etaMaxPoint.y
            print("sX,sY:", sX, sY)
        cost += newImage[sX][sY]
        print("cost:", cost)
        N += 1

        if etaMaxPoint.y == 359:
            break

    print("N is:", N)


def result():
    global listFilesDCM,fileNumber,cost,N,threshold
    global flag,minPath,minPath2,newImage,prePoint,etaMaxPoint,imArray,minPath3

    # 获取指定序号的图像内容
#    readFile()
    I = imArray.copy()

    # 初始化标记数组，最小路径数组
    flag = np.empty((256, 360), dtype=bool)
    flag[:, :] = False
    minPath = np.zeros((512, 512))

    # 获取展开的图像
    newImage = np.zeros((256, 360))

    # 设置阈值
    #I[I<threshold]=0
    for eta in range(0, 360):
        for l in range(0, 256):
            x, y = computeTangel(l, eta)
            newImage[l][eta] = I[x][y]
            # 如果imshow(origin='lower')没设置，则对图像进行上下翻转l=255-l，更好观察
            # newImage[255 - l][eta] = I[x][y]

    minPath3 = np.zeros((256, 360))

    for eta in range(0, 360):
        for l in range(255,0,-1):
            if newImage[l][eta]>0:
                minPath3[l][eta]=1
                break




def display():
    global minPath,minPath2,newImage,imArray,fileNumber,listFilesDCM,filename

    # 映射回原图像
    for eta in range(0, 360):
        for l in range(0, 256):
            if minPath2[l][eta] == 1:
                x, y = computeTangel(l, eta)
                minPath[x][y] = 1

    # minPath是映射回原图像的结果
    # minPath2[l][eta]是展开图像的结果

    plt.figure(1)
    plt.imshow(imArray, cmap=plt.cm.gray, origin='lower')
    plt.title(str(fileNumber)+"  Oringal DICOM")
    # plt.imsave("new Image3",newImage)
    plt.savefig("H:/PROJECTS/DICOM/Weight/" + str(fileNumber) + " Original DICOM.png", bbox_inches='tight')
    # cv2.imwrite("newImage22.png",newImage)
    # plt.show()

    plt.figure(2)
    plt.imshow(newImage, cmap=plt.cm.gray, origin='lower')
    plt.title(str(fileNumber)+"  Unflod DICOM")
    plt.savefig("H:/PROJECTS/DICOM\Weight/" + str(fileNumber) + " Unflod DICOM.png", bbox_inches='tight')


    plt.figure(3)
    plt.title(str(fileNumber)+"  path of unflod")
    plt.imshow(minPath2, cmap='gray', origin='lower')
    plt.savefig("H:/PROJECTS/DICOM/Weight/"+str(fileNumber) + "Unflod_path.png", bbox_inches='tight')


    plt.figure(4)
    plt.title(str(fileNumber)+"  path of oringal")
    plt.imshow(minPath, cmap='gray', origin='lower')
    plt.savefig("H:/PROJECTS/DICOM/Weight/" + str(fileNumber) + "Original_path.png", bbox_inches='tight')




    plt.figure(5)
    # plt.figimage(imArray,origin='upper',alpha=1)
    plt.title(str(fileNumber)+"  Oringal + Unflod")
    plt.imshow(newImage, cmap='gray', origin='upper', alpha=1)
    plt.imshow(minPath2, cmap='YlGn', origin='upper', alpha=0.4)
    plt.savefig("H:/PROJECTS/DICOM/Weight/"+str(fileNumber)+ "Unflod+Path.png", bbox_inches='tight')
    # plt.scatter(Y,X,c='r',s=1,)


    plt.figure(6)
    # plt.figimage(imArray,origin='upper',alpha=1)
    plt.imshow(imArray, cmap='gray', origin='upper', alpha=1)
    plt.imshow(minPath, cmap='YlGn', origin='upper', alpha=0.4)
    plt.title(str(fileNumber)+"  Oringal + Path")
    # plt.scatter(Y,X,c='r',s=1,)
    plt.savefig("H:/PROJECTS/DICOM/Weight/"+str(fileNumber)+"Oringal+Path.png",bbox_inches='tight')
    plt.show()



def display2():
    global minPath3
    global minPath,minPath2,newImage,imArray,fileNumber,listFilesDCM,filename

    minPath = np.zeros((512, 512))
    # 映射回原图像
    for eta in range(0, 360):
        for l in range(0, 256):
            if minPath3[l][eta] == 1:
                x, y = computeTangel(l, eta)
                minPath[x][y] = 1


    plt.figure(5)
    # plt.figimage(imArray,origin='upper',alpha=1)
    plt.title(str(fileNumber)+"  Oringal + Unflod")
    plt.imshow(newImage, cmap='gray', origin='upper', alpha=1)
    plt.imshow(minPath3, cmap='orRd', origin='upper', alpha=0.4)
    plt.savefig("H:/PROJECTS/DICOM/Oringal+Path/Threshold/"+str(fileNumber)+ "Oringal+Unflod.png", bbox_inches='tight')
    # plt.scatter(Y,X,c='r',s=1,)


    plt.figure(6)
    # plt.figimage(imArray,origin='upper',alpha=1)
    plt.imshow(imArray, cmap='gray', origin='upper', alpha=1)
    plt.imshow(minPath, cmap='YlGn', origin='upper', alpha=0.4)
    plt.title(str(fileNumber)+"  Oringal + Path")
    # plt.scatter(Y,X,c='r',s=1,)
    plt.savefig("H:/PROJECTS/DICOM/Oringal+Path/Threshold/"+str(fileNumber)+"Oringal+Path.png",bbox_inches='tight')
    plt.show()





# 全局变量的定义
temp = np.array([[1, 1, 2], [1, 0, 1], [1, 1, 2]], dtype=float)


pathDicom = "DCM_source"
cost = 0
iters = 1000
threshold = 100
# 读取文件夹内图像列表
listFilesDCM = []
fileNumber = 6

def readFileList(pathDicom):
    global listFilesDCM
    for diName, subdirList, fileList in os.walk(pathDicom):
        for filename in fileList:
            if ".dcm" in filename.lower():
                print(filename)
                listFilesDCM.append(os.path.join(diName, filename))



imArray=np.zeros((512,512))
flag = np.empty((256, 360), dtype=bool)
flag[:, :] = False
# minPath是原图上的路径
# minPath2展开图上的路径
minPath = np.zeros((512, 512))
minPath2=np.zeros((256,360))
newImage = np.zeros((256, 360))
N=0
id=1
cost=0
etaMaxPoint=Point(id,0,0,0)
vistedPointList=[]
prePoint=np.empty((256,360),dtype=list)

minPath3=np.zeros((256,360))


if __name__=="__main__":
    readFileList(pathDicom)
    for fileNumber in range(0,17):
    # path="Orginal1.jpg"
    # fileNumber=0
    # imArray=cv2.imread(path,0)
    #result()
        main()
        display()