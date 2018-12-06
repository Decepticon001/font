from PIL import Image

def grayscale_Image(image,resize_width=9,resize_heith=8):
    im = Image.open(image)
    smaller_image = im.resize((resize_width,resize_heith))
    grayscale_image = smaller_image.convert('L')
    return grayscale_image

def hash_String(image,resize_width=9,resize_heith=8):
    hash_string = ""
    pixels = list(grayscale_Image(image,resize_width,resize_heith).getdata())
    for row in range(1,len(pixels)+1):
        if row % resize_width :
            if pixels[row-1] > pixels[row]:
                hash_string += '1'
            else:
                hash_string += '0'
    return int(hash_string,2)

def Difference(dhash1, dhash2):
    difference = dhash1 ^ dhash2
    return bin(difference).count('1')




if __name__ == '__main__':
    dhash1 = hash_String('/Users/pengzhishen/PycharmProjects/tianyancha/font_dic/1.png')
    dhash2 = hash_String('/Users/pengzhishen/PycharmProjects/tianyancha/font_dic/2.png')
    d = Difference(dhash1,dhash2)

    print(d)