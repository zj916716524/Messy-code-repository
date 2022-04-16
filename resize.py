import os
import cv2


# resize image
def resize(img_path, save_path, size):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (size, size))
    cv2.imwrite(save_path, img)

img_path = ''
save_path = ''
for i in os.listdir(img_path):
    img_box_path = os.path.join(img_path, i)
    img_box_sava = os.path.join(save_path, i)
    for j in os.listdir(img_box_path):
        img_path_img = os.path.join(img_box_path, j)
        img_save_sava = os.path.join(img_box_sava, j)
        # 256 is image size
        resize(img_path_img, img_save_sava, 256)
