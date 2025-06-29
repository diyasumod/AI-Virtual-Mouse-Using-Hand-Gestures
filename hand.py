import cv2

img = cv2.imread("2.png")

img_dim = img.shape

print("Dimensions: " , img_dim)

cv2.rectangle(img,(170,60),(400,360),(0,255,0),3)
cv2.putText(img, "Double click", (230,40), cv2.FONT_HERSHEY_DUPLEX, 0.77, (255, 255, 255), 2)
cv2.imwrite("double_click.png",img)

cv2.imshow("Image", img)
cv2.waitKey(0)
