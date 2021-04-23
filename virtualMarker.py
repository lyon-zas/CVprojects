import cv2
import numpy as np
frameWidth = 540
frameHeight = 380
cap = cv2.cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150) 

mycolors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,75,0,100,255,255],
            [90,48,0,118,255,255] #blue
              ]
mycolorValue = [[51,153,255],
                [255,0,255],
                [0,255,0],
                [255,0,0]]

myPoints =[] #[x ,  y,colorID]

def findColor(img, mycolors,mycolorValue): 
     imgHSV = cv2.cv2.cvtColor(img,cv2.cv2.COLOR_BGR2HSV)
     count = 0
     newPoints=[]
     for color in mycolors:
         lower = np.array(color[0:3])
         upper = np.array(color[3:6],)
         mask = cv2.cv2.inRange(imgHSV,lower,upper)
         x,y = getContours(mask)
         cv2.cv2.circle(imgResult,(x,y),10,mycolorValue[count],cv2.cv2.FILLED)
         if x!=0 and y!=0 :
             newPoints.append([x,y,count])
         count +=1
         #cv2.cv2.imshow(str(color[0]),mask)
     return newPoints
def getContours(img):
    contours,hierarchy = cv2.cv2.findContours(img,cv2.cv2.RETR_EXTERNAL,cv2.cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.cv2.contourArea(cnt)
        if area>500:
            # cv2.cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.cv2.approxPolyDP(cnt,0.02*peri,True)
          
            x,y,w,h = cv2.cv2.boundingRect(approx)
    return x+y//2,y

def drawOnCanvas (myPoints,mycolorValue):
    for point in myPoints:
        cv2.cv2.circle(imgResult,(point[0],point[1]),10,mycolorValue[point[2]],cv2.cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, mycolors,mycolorValue)
    if len(newPoints)!= 0:
        for newp in newPoints:
            myPoints.append(newp)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,mycolorValue)
    cv2.cv2.imshow("video",imgResult)
    if cv2.cv2.waitKey(1) & 0xFF  ==ord('q'):
        break