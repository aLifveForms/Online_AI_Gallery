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

- [Home](#Online_AI_Gallery)
- [Images](#Images)
  - [Download Fake Images](#Download-Fake-Images)
  - [Composite Faces Library](#Composite-Faces-Library)
  - [3D Face](#face-3d)
- [Voice](#voice)
  - [Voice clone](#voice-clone)
  - [Voice machine generated](#voice-machine-generated)
  - [Song](#song)
- [Animate](#animate)
  - [Face bobbling](#face-bobbling)
  - [Lip sync](#lip-sync)
- [Display](#display)
- [Trouble shooting](#trouble-shooting)
- [License](LICENSE)
- [Team members](#team-members)

# Images

This section is about manipulating images. removing the faces from an image, removing any duplicate images, face recognition, combining all faces to form one average face, and animating this average face in real-time or recorded video.

### Download Fake Images
Compiste faces will be created by processing a series of photos, to obtain these photos, we will utilize a library called [This person does not exist API](https://pypi.org/project/thispersondoesnotexist/) to retrieve a large number of bogus images. Take the following actions:

1. create a folder inside the src folder name it fake Images.
   
```p
mkdir -p src/data/fakeImages
```

2. run file names getFakeFaces.py
   
```p
python faces/getFakeFaces.py  src/data/fakeImages 100
```
![example](doc/fakeFaces.jpg)



### Composite Faces Library