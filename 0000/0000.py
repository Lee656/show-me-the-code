#coding:utf-8
import Image, ImageDraw, ImageFont, sys
'''
相关资料：
1. PIL pyhton图像处理库，64位的库可以在http://www.lfd.uci.edu/~gohlke/pythonlibs/上查找已经编译的
2. 基本的几个PIL中的模块用法，涉及Image, ImageDraw, ImageFont等方法调用
3. 绘制图像位置的确定
'''

def draw_text(im, text, color):
	draw = ImageDraw.Draw(im)
	width, height = im.size
	# font_size设为width和height的10分之1大小
	font_size = min(width, height) / 10
	# 按照font_size大小加入了偏移
	pos = (width - (font_size*0.55)*len(text), 0)
	font = ImageFont.truetype("arial.ttf", font_size)
	draw.text(pos, text, fill=color, font=font)
	del draw

if __name__ == "__main__":
	'''
	Usage: python 0000.py text color input_img.xxx out_img.xxx
	color: red, green, blue, white, black
	'''
	# color 映射表
	color_map = {"red":(255,0,0),"green":(0,255,0),"blue":(0,0,255),"white:":(255,255,255),"black":(0,0,0)}

	if len(sys.argv) != 5:
		print 'Command error!\nUsage: python 0000.py text color input_img.xxx out_img.xxx'
		sys.exit()

	text = sys.argv[1]
	color = color_map['red']
	if sys.argv[2] not in color_map:
		print 'input color not exist, set color default red'
	else:
		color = color_map[sys.argv[2]]
	img_in_file = sys.argv[3]
	img_out_file = sys.argv[4]

	try:
		im = Image.open(img_in_file)
		draw_text(im, text, color)
		im.save(img_out_file,"JPEG")
		print 'Image saved in %s' % img_out_file
	except:
		print 'error happened!'
		sys.exit()