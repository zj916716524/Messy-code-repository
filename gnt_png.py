import os
import numpy as np
import struct
from PIL import Image


data_dir = '../gnt'
# train_data_dir = "../data/HWDB1.1trn_gnt"
train_data_dir = os.path.join(data_dir, 'Gnt1.0TrainPart1')#HWDB1.1trn_gnt
gnt_dir = train_data_dir
txt_save_path = '/home/xyz/stroke-level-decomposition/data/decompose-stroke-3755.txt' # 生成的图片列表清单txt文件的保存目录
word1 = []
with open(txt_save_path,'r') as f:
    for line in f.readlines():
        word, _, storkelist = line.split()
        word1.append(word)

def one_file(f):
    header_size = 10
    while True:
        header = np.fromfile(f, dtype='uint8', count=header_size)  # numpy.fromfile()
        if not header.size: break
        sample_size = header[0] + (header[1] << 8) + (header[2] << 16) + (header[3] << 24)
        tagcode = header[5] + (header[4] << 8)
        width = header[6] + (header[7] << 8)
        height = header[8] + (header[9] << 8)
        if header_size + width * height != sample_size:
            break
        image = np.fromfile(f, dtype='uint8', count=width * height).reshape((height, width))
        yield image, tagcode

target_dir = '../gnt/data/HWDB1.0part'
for file_name in os.listdir(gnt_dir):
    if file_name.endswith('.gnt'):
        file_path = os.path.join(gnt_dir, file_name)
        # print(os.path.splitext(file_name))
        train_data_dir = os.path.join(target_dir, os.path.splitext(file_name)[0])
        #print(train_data_dir)
        if not os.path.exists(train_data_dir):
            os.mkdir(train_data_dir)
        with open(file_path, 'rb') as f:
            for image, tagcode in one_file(f):
                try:
                    tagcode_unicode = struct.pack('>H', tagcode).decode('gb2312')
                except:
                    continue
                if tagcode_unicode in word1:
                    im = Image.fromarray(image)
                    im.convert('RGB').save(train_data_dir + '/{}.png'.format(tagcode_unicode))
                # print(tagcode_unicode)

                # q = {v: k for k, v in char_dict.items()}
                # im = Image.fromarray(image)
                # im.convert('RGB').save(train_data_dir + '/{}.png'.format(tagcode_unicode))

