import cv2
img = cv2.imread(r'Gan.jpeg', 0)
print(img)
status = cv2.imwrite('ganpati.png',img)
print("Image written to file-system: ", status)
