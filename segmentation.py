import cv2
#from skimage import measure
import numpy as np

img = cv2.imread("2.png")
cv2.imshow("Image", img)

[R,C,P]= img.shape
print(R,C,P)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image", gray_image)

(thresh, binary) = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
print(thresh)
cv2.imshow("binary",  binary)

# seperate Red, Green, Blue 

red = np.zeros((R, C, 1),dtype = "uint8")
green = np.zeros((R, C, 1),dtype = "uint8")
blue = np.zeros((R, C, 1),dtype = "uint8")

for i in range(R):
    
    for j in range(C):
        red[i,j] = img[i,j,0]
        green[i,j] = img[i,j,1]
        blue[i,j] = img[i,j,2]
        
cv2.imshow("Blue",  blue)
cv2.imshow("Green", green)
cv2.imshow("Red",  red)

# Convert to Black and White 
bw_image = np.zeros((R, C, 1))

for i in range(R):
    for j in range(C):
        if(gray_image[i,j]<thresh):
            bw_image[i,j]=1
            
cv2.imshow("bW image",bw_image)


#labeledImage = measure.label(bw_image, 2)
#cv2.imshow("labeledImage", labeledImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
