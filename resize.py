import os
import cv2


# 修改图片大小
def resize(img_path, save_path, size):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (size, size))
    cv2.imwrite(save_path, img)


img_path = '/home/zeng/AttentionGan_gujia/zhengkai_fangsong'
save_path = '/home/zeng/AttentionGan_gujia/zhengkai_fangsong'
for i in os.listdir(img_path):
    if 'testA' in i or 'testB' in i:
        img_box_path = os.path.join(img_path, i)
        img_box_sava = os.path.join(save_path, i)
        for j in os.listdir(img_box_path):
            img_path_img = os.path.join(img_box_path, j)
            img_save_sava = os.path.join(img_box_sava, j)
            resize(img_path_img, img_save_sava, 256)
