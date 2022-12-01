from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import os
import numpy as np
import pathlib
import argparse

parser = argparse.ArgumentParser(description='Obtaining characters from .ttf')
parser.add_argument('--ttf_path', type=str, default='./FOUR', help='ttf directory')  # ttf 文件路径 
parser.add_argument('--chara', type=str, default='./char.txt', help='characters')  # 需要的字符
parser.add_argument('--save_path', type=str, default='./four_img', help='images directory') # 保存路径
parser.add_argument('--img_size', type=int, default='128', help='The size of generated images')  #图像大小 
parser.add_argument('--chara_size', type=int, default='120', help='The size of generated characters')  # 字体大小
args = parser.parse_args()

file_object = open(args.chara, encoding='utf-8')
try:
    characters = file_object.read()
finally:
    file_object.close()


def draw_single_char(ch, font, canvas_size, x_offset, y_offset):
    img = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((x_offset, y_offset), ch, (0, 0, 0), font=font)
    return img


def draw_example(ch, src_font, canvas_size, x_offset, y_offset):
    src_img = draw_single_char(ch, src_font, canvas_size, x_offset, y_offset)
    example_img = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))
    example_img.paste(src_img, (0, 0))
    return example_img


data_dir = args.ttf_path
data_root = pathlib.Path(data_dir)

all_image_paths = list(data_root.glob('*.TTF*'))
# if you datasets is ttf.please use:
#all_image_paths = list(data_root.glob('*.ttf*'))
all_image_paths = [str(path) for path in all_image_paths]


seq = list()

for (label, item) in zip(range(len(all_image_paths)), all_image_paths):
    print(item)
    src_font = ImageFont.truetype(item, size=args.chara_size)

    for (chara, cnt) in zip(characters, range(len(characters))):
        try:
            img = draw_example(chara, src_font, args.img_size, (args.img_size - args.chara_size) / 2,
                               (args.img_size - args.chara_size) / 2)
            path_full = os.path.join(args.save_path, 'id_%d' % label)
            if not os.path.exists(path_full):
                os.mkdir(path_full)

            img.save(os.path.join(path_full, "%s.png" % (chara)))
        except:
            continue
