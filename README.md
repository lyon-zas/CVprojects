# MY OPENCV PRJECTS IN PYTHON
computer vision projects
# Brief Introduction/output To Each
## 1 Text recognition(OCR) 
OCR simply means optical character recognition(text recognition). This project make use of Tesseract an open source text recognition (OCR) Engine ,Python-tesseract which is an optical character recognition (OCR) tool for python.
That is, it will recognize and “read” the text embedded in images.Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine and openCV. 
This project uses of this tools to recognise text, print them in the terminal, create bounding boxes on each word
![alt Output](https://user-images.githubusercontent.com/67665701/115891316-dcdf7080-a44d-11eb-94b3-6e73e2038d88.png)

## 2 Face detection 
This make use of openCV and haarcascade_frontalface(pre-trained face module) to dectect faces in an image, put bounding boxes around and label them.
![alt Output](https://user-images.githubusercontent.com/67665701/115896940-d94ee800-a453-11eb-82e8-6c5d024b3595.png)

## 3  Number Plate Detection 
This is quiet similar to the face detection but uses a haarcascade_russian_plate(a russian plate trained module) to dectect plate numbers  in an image, put bounding boxes around, label them and save them.
![alt Output](https://user-images.githubusercontent.com/67665701/115896978-e23fb980-a453-11eb-807c-1c8bda0d9dfa.png)

## 4 Shape/object Detection And Classifiction
This algorithim is designed to detect shapes from an image converting it to grayscale,finding the contours and pixel areas thereby classifying them based on arc angles(Triangle, square,circle,rectangle) and finally creating bounding boxes around each.
![alt Output](https://user-images.githubusercontent.com/67665701/115897108-fe435b00-a453-11eb-8613-35f24b15226a.png)

## 5 Color Detection/Virtual Marker
the colors are detected by picking each colors (hue min,hue max,saturation min,saturation max,val min and val max) values.A color list was set for each detection and a drawOnCanvas funtion was used to draw the respective colors
![alt Output](https://user-images.githubusercontent.com/67665701/115897020-ea97f480-a453-11eb-9c7d-4c69a684ca51.png)
