import math

def get_average_color_between_lips(top_lip,bottom_lip,image):
    # return the pixes between lips
    top_lip_x = top_lip[9][0]
    top_lip_y = top_lip[9][1]
    bottom_lip_y = bottom_lip[9][1]
    sum = 0
    number_of_pixels = 0
    for current_y in range(top_lip_y,bottom_lip_y+1):
        pixels = image[current_y,top_lip_x]
        r = 0+pixels[0]
        g = 0+pixels[1]
        b = 0+pixels[2]
        # print("pixels", r,g,b)
        gray_pixel = (r+g+b)/3
        # print("gray",gray_pixel)
        sum += gray_pixel
        number_of_pixels += 1
    # print("sum",sum,number_of_pixels)
    if number_of_pixels > 0:
        average = sum/number_of_pixels
    else:
        average = 0
    print("average",average)
    return average
def check_shows_teeth(top_lip,bottom_lip,image):
    average = get_average_color_between_lips(top_lip,bottom_lip,image)
    if average > 70:
        return True
    else:
        return False

def get_lip_height(lip):
    sum = 0
    for i in [2, 3, 4]:
        # distance between two near points up and down
        distance = math.sqrt((lip[i][0] - lip[12-i][0]) ** 2 + \
                             (lip[i][1] - lip[12-i][1]) ** 2)
        sum += distance
    # distance = math.sqrt((lip[2][0] - lip[10][0]) ** 2 + \
    #                      (lip[2][1] - lip[10][1]) ** 2)
    # sum += distance
    # distance = math.sqrt((lip[3][0] - lip[9][0]) ** 3 + \
    #                      (lip[3][1] - lip[9][1]) ** 3)
    # sum += distance
    # distance = math.sqrt((lip[4][0] - lip[8][0]) ** 2 + \
    #                      (lip[4][1] - lip[8][1]) ** 2)
    # sum += distance
    return sum / 3


def get_mouth_height(top_lip, bottom_lip):
    sum = 0
    for i in [8, 9, 10]:
        # distance between two near points uo and down
        distance = math.sqrt((top_lip[i][0] - bottom_lip[18-i][0])**2 +
                             (top_lip[i][1] - bottom_lip[18-i][1])**2)
        sum += distance 
    return sum / 3

def  check_mouth_open(top_lip, bottom_lip):
  top_lip_height = get_lip_height(top_lip)
  bottom_lip_height = get_lip_height(bottom_lip)
  mouth_height = get_mouth_height(top_lip, bottom_lip)

  #if the mouth is open more thab lip height * ratio return true 
  ratio = 0.5
  if mouth_height > min(top_lip_height, bottom_lip_height) * ratio:
    return True
  else:
    return False

# just run this file python3 mouth_open_alg