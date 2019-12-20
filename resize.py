# Resize train images. Just run this code if did not resize.

from PIL import Image
import os
import cv2
import argparse

# initiate the parser
parser = argparse.ArgumentParser()

parser.add_argument("--image_input", "-img_i", help="Path to source images")
parser.add_argument("--image_output", "-img_o", help="Path to source images")

args = parser.parse_args()

def resize(img_path: str):
    src_img = src_path + img_path + '.jpg'
    des_img = des_path + img_path + '.jpg'
    if not os.path.exists(src_img):
      with open("resize_issue_list.txt", "a") as myfile:
        myfile.write(src_img + "\n")
      count_fail += 1
      return
  
    img = cv2.imread(src_img, cv2.IMREAD_UNCHANGED)

    width = 800
    height = 450
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    count_success += 1

if __name__ == "__main__":

  if args.image_input and args.image_output:
    src_path = args.image_input
    des_path = args.image_output
    if not os.path.exists(des_path):
      os.mkdir(des_path)
  else:
    print("Pls add path to source/des images folder")
  count_fail = 0
  count_success = 0
  image_paths = glob.glob('{}/*.jpg'.format(src_path))
  for img in image_paths:
    resize(img)
  print("Resized ", count_success, " images.")
  print("Failed ", count_fail, " images.")