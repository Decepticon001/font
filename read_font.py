from xml.dom.minidom import parse
import xml.dom.minidom
import os
from PIL import Image, ImageFont, ImageDraw
from fontTools import unichr
from fontTools.ttLib import TTFont
import pytesseract
from pytesseract import image_to_string


def get_xml():
    font = TTFont('tyc-num.woff')
    font.saveXML("font.xml")

def get_image():
    DOMTree = xml.dom.minidom.parse('font.xml')
    collection = DOMTree.documentElement

    codes = collection.getElementsByTagName("cmap_format_12")[0]
    codes1 = codes.getElementsByTagName('map')
    # print(codes1)
    for code in codes1:
       if code.hasAttribute("code"):
          ss = int(str(code.getAttribute("code")),16)
          char = unichr(ss)
          # print(char)
          text = u'%s' % (char)
          im = Image.new('RGB', (130, 130), (255, 255, 255))
          dr = ImageDraw.Draw(im)
          font = ImageFont.truetype(os.path.join('fonts','/Users/pengzhishen/PycharmProjects/tianyancha/font_dic/tyc-num.woff'), 100)
          dr.text((12, 10), text, font=font, fill='#000000')
          # im.show()
          im.save('../images/%s.png' % (char))
          im.close()

def to_str():
    DOMTree = xml.dom.minidom.parse('font.xml')
    collection = DOMTree.documentElement
    codes = collection.getElementsByTagName("cmap_format_12")[0]
    codes1 = codes.getElementsByTagName('map')
    # print(codes1)
    for code in codes1:
        if code.hasAttribute("code"):
            ss = int(str(code.getAttribute("code")), 16)
            char = unichr(ss)
            print(char)
            try:
                a = image_to_string('/Users/pengzhishen/Downloads/image/%s.png'%char, lang='chi_sim')
                print("result:%s"%a)
            except Exception as e:
                print(e)

if  __name__ == '__main__':
    to_str()