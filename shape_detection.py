import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cv2.cvtColor( imgArray[x][y], cv2.cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cv2.cvtColor(imgArray[x], cv2.cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    contours,hierarchy = cv2.cv2.findContours(img,cv2.cv2.RETR_EXTERNAL,cv2.cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.cv2.drawContours(imgContours,cnt,-1,(255,0,0),3)
            peri = cv2.cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            
            x,y,w,h = cv2.cv2.boundingRect(approx) #for creating bounding rectangular shapes around  obj 
            if objCor ==3: objectType = "Tri"
            elif objCor == 4: 
                aspRatio = w/float(h)
                if aspRatio >0.95 and aspRatio <1.05: objectType="Square"
                else:objectType= "Rectangle"
            elif objCor >4: objectType ="circles"
            else: objectType = "none"
            cv2.cv2.rectangle(imgContours,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.cv2.putText(imgContours,objectType,
                                                (x+(w//2)-10,y+(h//2)-10),cv2.cv2.FONT_HERSHEY_COMPLEX,0.8,
                                                (0,0,0),2) # Color
         

path = "Resources/shapes.png"
img = cv2.cv2.imread(path)
imgContours = img.copy()
imggray = cv2.cv2.cvtColor(img,cv2.cv2.COLOR_BGR2GRAY)
imgBlur = cv2.cv2.GaussianBlur(imggray, (7,7),1)
imgcanny = cv2.cv2.Canny(imgBlur,50,50)
getContours(imgcanny)


imgBlank = np.zeros_like(img)
imgStack = stackImages(0.6,([img, imggray,imgBlur],
                                        [imgcanny, imgContours,imgBlank],))


cv2.cv2.imshow("Staked",imgStack)

cv2.cv2.waitKey(0)