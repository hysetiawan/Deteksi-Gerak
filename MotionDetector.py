import cv2

face_cascade = cv2.CascadeClassifier('E:\Bermain di pycharm\Coba-coba\haarcascade_frontalface_default.xml') #Kita definisikan pengenal wajahnya
 
cap = cv2.VideoCapture(0) #Ini tuh untuk mendefinisikan instance object untuk kamera
 
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
         
        
    cv2.imshow('deteksi wajah',img)
    k = cv2.waitKey(30)
    if k == 27:
        break
 
cap.release()
cv2.destroyAllWindows()