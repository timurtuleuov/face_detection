import cv2

#классификатор
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('1.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, 1.1, 5)

#рисует квадрат
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x + w,y + h), (0, 0, 255), 4)

cv2.imshow('Image', image)
 

cv2.waitKey()
 

cv2.destroyAllWindows()