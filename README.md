# Online_AI_Gallery    ??LOGO

[![License](https://poser.pugx.org/aimeos/aimeos-typo3/license.svg)](https://github.com/karmelyoei/Online_AI_Gallery/blob/main/LICENSE)

***Online AI Gallery*** is a show that represents images that have been reshaped and edited through multiple Artificial intelligence frameworks in order to generate awesome artifacts.You can use this project, which is a compilation of multiple Artificial intelligence frameworks for image processing and can adapt, extend, overwrite, and customize anything to your needs


## Objectives:

1. Get around 300 fake images downloaded from a library called This Person doesnt not Exist API
2. Find faces that might be duplicated
3. Face Recognition. 
4. Composite all face to generate one average face.
5. Build a 3D modle of the average face.
6. Animate the average face in a way that will moves and talks according to a recorded video or real-time.
7. Cloning Voice to use it in our recorded video for presenation purposes.
8. Build different layouts for presentation.


:star: Star us on GitHub — it motivates us a lot!


# Table Of Content

- [Online_AI_Gallery    ??LOGO](#online_ai_gallery----logo)
  - [Objectives:](#objectives)
- [Table Of Content](#table-of-content)
- [Installation](#installation)
- [Images](#images)
    - [Download Fake Images](#download-fake-images)
    - [Composite Faces Library](#composite-faces-library)


# Installation

First clone this repo then please follow each section's requirement to get your  results.

```
git clone https://github.com/karmelyoei/Online_AI_Gallery.git 
```


# Images

This section is about manipulating images. removing the faces from an image, removing any duplicate images, face recognition, combining all faces to form one average face, and animating this average face in real-time or recorded video.

### Download Fake Images
Compiste faces will be created by processing a series of photos, to obtain these photos, we will utilize a library called [This person does not exist API](https://pypi.org/project/thispersondoesnotexist/) to retrieve a large number of bogus images. Take the following actions:

1. create a folder inside the src folder name it fake_images.
   
```p
mkdir -p src/data/fake_images
```

2. run file names getFakeFaces.py
   
```p
python faces/getFakeFaces.py  src/data/fake_images 100
```
![example](doc/fakeFaces.jpg)



### Composite Faces Library

After obtaining a slew of fake photographs from the first phase, we can use our face composite file to create an average face from these images. 

For the composite face, we go through three steps: first, we detect the facial feature, then we normalize the images to the same reference frame (600* 600), and last, we align the faces together.

Perform the following actions:

1. Download the shape predictor from this website [shape_predictor_68_face_landmarks.dat](https://github.com/davisking/dlib-models.) and save it under the folder name src/detectors/dots_detector/
  
2. Create virual environment : ```pip install virtualenv```
   
3. Build virtual environment: ```virtualenv env```

4. Activate virtual environment
For windows: ```env/Script/activate```
For Linux : ```source env/bin/activate ```

5. Install the requirements for this step:```pip install dlib numpy opencv-python imutils```
   
6. Run this command to build the dot files for each image: ```python src/faceCreatePoints.py \ --dat src/detectors/dots_detector shape_predictor_68_face_landmarks.dat \
  --imagespath src/data/fake_images```

7. Run the faceComposite file:```python src/faceComposite.py --path src/data/fake_images```
8. You will find the results inside folder ```./src/data/fake_images/composite```
   
 <div style="text-align:center"><img src="doc/face_composite.small.png" /></div>

