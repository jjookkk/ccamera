import cv2
import sys
import os

os.system("sudo raspistill -o 1.jpg -w 500 -h 500 -br 50")

# Get user supplied values
imagePath = "1.jpg"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("yes! found {0} faces!\n happy happy happy".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print("draw a rectangle hahah")

if os.system("rm -rf detected.jpg"):
    print("erase origin jpg")
else: 
    print("failed")

cv2.imwrite("detected.jpg", image)
cv2.waitKey(0)
