import cv2
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
frame1 = cv2.resize(frame,(4   ,4))[..., :3]

print(frame1)
# out1.write(img_as_ubyte(joinedFrame))
cv2.imwrite('testcam.png',frame1)

cap.release()
# out1.release()