import requests as req
import shutil
import time
import sys
import os

url = 'https://thispersondoesnotexist.com/image'

if len(sys.argv) <= 1:
  print(f"""
  python {sys.argv[0]} <destination_directory> [<number_of_faces>]
  Downloads faces from {url}
  destination_directory   where to save faces
  number_of_faces         how many faces to download 
                          optional, if not provided user is asked
  example:
    mkdir ./src/data/
    python {sys.argv[0]} ./src/data/ 10
  """)
  sys.exit(1)

destination_directory = sys.argv[1]

def save_picture(number):
  r = req.get(url, stream = True)

  if r.status_code == 200:
    r.raw.decode_content = True
    with open(f"{destination_directory}/fake{i}.jpeg",'wb') as f :
      shutil.copyfileobj(r.raw, f)
    print(f"Image sucessfully Downloaded: {destination_directory}/fake{i}.jpeg")
  else:
    print("fail downloading image")


if __name__ == "__main__":
  if len(sys.argv) >= 3:
    n_image = int(sys.argv[2])
  else:
    n_image = int(input("how many fake persons you want? "))
  for i in range(n_image):
    try:
      save_picture(i)
    except:
      pass 
    time.sleep(2)