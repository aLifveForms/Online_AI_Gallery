# Issues might occur

### Get fake images file issues:
   
  1. On get fake images file you migh get error :
      "requests.exceptions.InvalidURL: Failed to parse: https://thispersondoesnotexist.com/image"

      ***to solve this***:
      ```python -m pip install --upgrade urllib3```

      or just download requests version 2.21.0

      ```pip uninstall requests # to remove current version
      pip install requests==2.21.0```


### Animate issues:

[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.
Input video not found for image_animate.py

ValueError: ('Cannot warp empty image with dimensions', (470, 0, 3)) Error here was the cutting dimensions x,y,w,h in headbobble_image_animation.py around line 68 were incorrect