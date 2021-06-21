from PIL import Image
import os


path = './openMouthButTeethNotShowing'
count = 0

for image_path in sorted(os.listdir(path)):
      #open images
      image_file = Image.open(os.path.join(path, image_path))


      #chaninging the resolution using quality parameter
      image_file.save(f"./openMouthButTeethNotShowing/lowres{count}.jpeg", quality = 10)
      count += 1