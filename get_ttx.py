import os
from PIL import Image, ImageFont, ImageDraw


ch = '士'
text = u'%s' % (ch)
im = Image.new('RGB', (130, 130), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype(os.path.join('fonts', '/Users/pengzhishen/Downloads/WeiRuanYaHeiTi/WeiRuanYaHei-1.ttf'), 100)
dr.text((12, 10), text, font=font, fill='#000000')
# im.show()
im.save('/Users/pengzhishen/Downloads/image/士.png')
im.close()