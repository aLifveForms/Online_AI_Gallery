# import the necessary packages
# python faceCreatePoints.py -p . -d dots_detector/shape_predictor_68_face_landmarks.dat
from imutils import face_utils
import dlib
import cv2
import argparse
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--imagespath", required=True,
	help="path to input image")
ap.add_argument("-d", "--dat", required=True,
	help="path to dat file 'shape_predictor_68_face_landmarks.dat'")
args = vars(ap.parse_args())

imagespath = args["imagespath"]

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = args["dat"]
# p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

for filePath in sorted(os.listdir(imagespath)):
    if filePath.lower().endswith(".jpg") or filePath.lower().endswith(".jpeg") \
                                         or filePath.lower().endswith(".png"):
        print(filePath+'.txt', "making dots")

        image = cv2.imread(os.path.join(imagespath,filePath))
        (h, w) = image.shape[:2]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # detect faces in the grayscale image
        rects = detector(gray, 0)

        if len(rects) <= 0:
            print("could not find faces/rects")
            continue

        # loop over the face detections
        for (i, rect) in enumerate(rects):
            if i > 0:
                print("has more than one face. skipping extra face",i)
                continue
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            if len(shape) <= 0:
                print("face has no dots, skip")
            else:
                print("num dots", len(shape))
                output = open(os.path.join(imagespath,filePath+'.txt'), 'w')
                # loop over the (x, y)-coordinates for the facial landmarks
                # and draw them on the image
                for (x, y) in shape:
                    # cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
                    # print(x,y)
                    output.write(f'{x} {y}\n')