from PIL import Image, ImageDraw
import face_recognition
from openMouthAlg import get_lip_height, get_mouth_height, check_mouth_open, check_shows_teeth
import os


path = './data/fake_images'

top_lip = []
bottom_lip = []
count = 0

# List all files in the directory
for filePath in sorted(os.listdir(path)):
    # load the jpg file into a numpy array
    image = face_recognition.load_image_file(os.path.join(path, filePath))

    # find all the facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)

    print("I found {} faces i this pic".format(len(face_landmarks_list)))
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image)

    for face_landmarks in face_landmarks_list:
        # print the location of each facial feature in this image
        facial_features = ['chin',
                           'left_eyebrow',
                           'right_eyebrow',
                           'nose_bridge',
                           'nose_tip',
                           'left_eye',
                           'right_eye',
                           'top_lip',
                           'bottom_lip']

        for facial_feature in facial_features:
            print(" the {} in this face has the following points: {}".format(
                facial_feature, face_landmarks[facial_feature]))
            top_lip = face_landmarks['top_lip']
            bottom_lip = face_landmarks['bottom_lip']

        

    print('top_lip height: %.2f' % get_lip_height(top_lip))
    print('bottom_lip height: %.2f' % get_lip_height(bottom_lip))
    print('mouth height: %.2f' % get_mouth_height(top_lip, bottom_lip))
    print('Is mouth open:', check_mouth_open(top_lip, bottom_lip))
    print('Is showing teeth:', check_shows_teeth(top_lip, bottom_lip, image))

    print('we reached pic number', filePath)
    if check_mouth_open(top_lip, bottom_lip) == True:
        print('count', count)

        pil_image.save(f'./openMouth/pic{count}.png')
        print(count)
        count = count + 1
        if check_shows_teeth(top_lip, bottom_lip, image) == False:
            pil_image.save(f'./openMouthButTeethNotShowing/pic{count}.png')



# file part one
