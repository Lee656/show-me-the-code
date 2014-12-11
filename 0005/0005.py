# coding:utf-8
# 将目录的照片尺寸变成不大于iphone5分比率的大小
'''
1. iPhon5 分辨率 1136*640 iPhone 960*640
2. 使用PIL进行图片处理
3. 读入图片进行尺寸判断，接着进行比例放缩
'''

import sys,os,Image

# iPhone5和iPhone4的尺寸
I5_SIZE = (1136, 640)
I4_SIZE = (960, 640)

# 修改尺寸
def change_size(im):
    w, h = im.size
    scale = max(float(w)/I5_SIZE[0], float(h)/I5_SIZE[1])
    print 'input image size: (%d, %d)' % (w, h)
    # 计算缩放比例
    if scale > 1:
        print 'size does not fit, start resize'
        w, h = int(w/scale), int(h/scale)
        im = im.resize((w, h), Image.ANTIALIAS)
    else:
        # 无需缩放
        print 'no resize, size is ok'
    return im

def save_image(im, file_name):
    # 判断当前路径下result文件夹是否存在
    if not os.path.exists('result'):
        os.mkdir('result')

    # 保存图片
    out_file_name = 'result/'+file_name
    im.save(out_file_name, 'JPEG')
    print 'result image save in %s' % out_file_name

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Command error!\nUsage: python 0005.py image_file'
        sys.exit(1)
    try:
        img_in_file = sys.argv[1]
        im = Image.open(img_in_file)
        im = change_size(im)
        img_filename = img_in_file.split('/')[-1]
        save_image(im, img_filename)
    except:
        print 'error!'
