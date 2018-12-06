from xml.dom.minidom import parse
import xml.dom.minidom
import os
from PIL import Image, ImageFont, ImageDraw
from fontTools import unichr
from fontTools.ttLib import TTFont
import pytesseract
from pytesseract import image_to_string


import os

from PIL import Image, ImageFont, ImageDraw

text = u'龙'

im = Image.new('RGB', (130, 130), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype(os.path.join('fonts','/Users/pengzhishen/PycharmProjects/tianyancha/font_dic/tyc-num.woff'), 100,index=0)
dr.text((12, 10), text, font=font, fill='#000000')
# im.show()
im.save('%s.png' % ("1"))
im.close()
