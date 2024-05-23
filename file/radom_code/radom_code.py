import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 生成随机验证码的图片
# 配置图片的宽带和高度
width, height = 120, 30
# 选择字体，字体大小
font_file = 'Monaco.ttf'
font_size = 35
char_length = 4  # 验证码个数
code = []
# 创建一个指定大小的白色背景图片
img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')


def random_letter():
    """生成A-Z之间的随机大写字母"""
    return chr(random.randint(65, 90))


def random_color():
    """生成随机RGB颜色(xxx,xxx,xxx)"""
    return random.randint(0, 255), random.randint(10, 255), random.randint(64, 255)


# 写文字,每个都字都随机颜色，从左到右排列
font = ImageFont.truetype(font_file, font_size)

for i in range(char_length):
    char = random_letter()
    code.append(char)
    h = random.randint(0, 4)
    draw.text([i * width / char_length, h], char, font=font, fill=random_color())

# 写干扰点，坐标在背景大小范围内随机
for i in range(40):
    draw.point([random.randint(0, width), random.randint(0, height)], fill=random_color())

# 画干扰线,线的条数取决于验证码位数
for i in range(char_length):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    draw.line((x1, y1, x2, y2), fill=random_color())

print(''.join(code))  # 验证码的值

# 对图像进行模糊处理
img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img.show()
# img.save('abc.png', 'png')
