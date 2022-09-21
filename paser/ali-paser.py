# -*- coding: utf-8 -*-
# @Time    : 2022/9/21 16:56
# @Author  : Kenny Zhou
# @FileName: ali-paser.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com

# 版权所有 © 艾科瑞特科技
# 艾科瑞特（iCREDIT）-让企业业绩长青
# 预知更多业绩长青，请与我们联系
# 联系电话：0532-88984128
# 联系邮箱：market@itruth.xin

import urllib
# import urllib.request
import base64
import re
from pathlib import Path
import time
import requests
import socket
socket.setdefaulttimeout(15)

# API产品路径
url = 'https://seal.market.alicloudapi.com/ai_market/ai_ocr_universal/gong_zhang/image_extractor/v1'
# 阿里云APPCODE
appcode = '439229df490b4cb2a9641704073aece5'
bodys = {}
querys = ""

if __name__ == "__main__":

	image_path = Path("/Users/kennymccormick/Downloads/招商银行需要的样本(1)/300dpi印鉴卡/BX01.jpg")
	# 参数配置
	if True:
		# 启用BASE64编码方式进行识别
		# 内容数据类型是BASE64编码
		f = open(image_path, 'rb')
		contents = base64.b64encode(f.read())
		f.close()
		bodys['IMAGE'] = contents
		bodys['IMAGE_TYPE'] = '0'
	else:
		# 启用URL方式进行识别
		# 内容数据类型是图像文件URL链接
		bodys[
			'IMAGE'] = 'https://icredit-api-market.oss-cn-hangzhou.aliyuncs.com/%E8%89%BE%E7%A7%91%E7%91%9E%E7%89%B9_%E6%99%BA%E8%83%BD%E5%9B%BE%E5%83%8F%E5%88%86%E6%9E%90_%E6%99%BA%E8%83%BD%E5%85%AC%E7%AB%A0%E8%AF%86%E5%88%AB/%E5%85%AC%E7%AB%A0.jpg'
		bodys['IMAGE_TYPE'] = '1'

	post_data = urllib.parse.urlencode(bodys).encode('utf-8')

	request = urllib.request.Request(url, post_data)
	request.add_header('Authorization', 'APPCODE ' + appcode)
	request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
	response = urllib.request.urlopen(request)
	content = response.read()
	if (content):
		print(content.decode('utf-8'))

