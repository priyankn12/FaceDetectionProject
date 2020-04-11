import cv2
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret,frame=cap.read()
    if ret==False:
        continue
    faces=face_cascade.detectMultiScale(frame,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("VideoFrame", frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
