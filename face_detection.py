import cv2 
cap = cv2.cv2.VideoCapture(0)
frameWidth = 40
frameHeight = 80
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150) 


img = cv2.cv2.imread("Resources\PSX_20200106_093245.jpg",)

faceCascade = cv2.cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
imgGray = cv2.cv2.cvtColor(img,cv2.cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
  cv2.cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  cv2.cv2.putText(img,"Face 1",(200,200),cv2.cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)


cv2.cv2.imshow("face", img)
cv2.cv2.waitKey(0)


# while True:
#     success, img = cap.read()
#     faceCascade = cv2.cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
#     imgGray = cv2.cv2.cvtColor(img,cv2.cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(imgGray,1.1,4)
#     faces = faceCascade.detectMultiScale(imgGray,1.1,4)

#     for (x,y,w,h) in faces:
#       cv2.cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#       cv2.cv2.putText(img,"Face 1",(200,200),cv2.cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
#       cv2.cv2.imshow("video",img)
#       if cv2.cv2.waitKey(1) & 0xFF  ==ord('q'):
#         break