import cv2


####################################
img = cv2.cv2.imread('Resources\p1.jpg')
plateCascade = cv2.cv2.CascadeClassifier("Resources\haarcascade_russian_plate_number.xml")
minArea = 200
color = (255,0,255)
count = 0
########################################


def plateNumber(img):
    img = cv2.cv2.imread('Resources\p1.jpg')
    imgGray = cv2.cv2.cvtColor(img,cv2.cv2.COLOR_BGR2GRAY)
    numberPlates = plateCascade.detectMultiScale(imgGray,1.1,4)
    count = 0

    for (x,y,w,h) in numberPlates:
        area = w*h
        if area >minArea:
            cv2.cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
            cv2.cv2.putText(img,"Number Plate",(x,y-5),cv2.cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.cv2.imshow("ROI", imgRoi)
    cv2.cv2.imshow("result",img)

    if cv2.cv2.waitKey(0) & 0xFF  ==ord('s'):
        cv2.cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.cv2.FILLED)
        cv2.cv2.putText(img,"Scan Saved",(150,265),cv2.cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.cv2.imshow("result",img)
        cv2.cv2.waitKey(0)
        count +=1
    return numberPlates
result = plateNumber(img)
cv2.cv2.imshow("test",result)
cv2.cv2.waitKey(0)