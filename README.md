# 思路：1.首先将字体文件下载，然后通过fonttool模块将woff文件转换为可读的xml文件。提取出里面所有汉字的unicode，然后通过绘图模块将字体画出。
# 然后使用pytesseract 开源ocr识别图片汉子
# 2.由于ocr识别汉子精准度问题，导致部分汉字不能识别，通过对比发现原字体微微软雅黑，打乱顺序，这样就通过下载正常的微软雅黑字体文件，绘图出所有的汉字，然后同样参数用tyc的字体文件绘图，然后通过图片感知哈希算法，进行hash比较得出对应关系

