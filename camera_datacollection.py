import cv2

cam = cv2.VideoCapture(0)
a=1

while True:

    ret, img = cam.read()
    
    cv2.imshow("Frame", img)
    key = cv2.waitKey(1)
    print(key)
    if(key == ord('q')):
        file_name=str(a)+'.png'

        cv2.imwrite(file_name,img)
      
        a=a+1
    if(key==ord('e')):
        break
cam.release()
cv2.destroyAllWindows()
