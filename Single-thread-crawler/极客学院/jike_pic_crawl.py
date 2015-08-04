#-*-coding:utf8-*-  保存文件名
import re
import requests

#读取源代码

html = requests.get('http://www.jikexueyuan.com/course/')

#匹配图片网址
pic_url = re.findall('<img src="(.*?)" class="lessonimg"',html.text,re.S)

i = 0
for each in pic_url:
	print 'now downoading:' + each
	pic = requests.get(each)
	fp = open('d:\\python_ML\\pic\\' + str(i) + '.jpg','wb')
	fp.write(pic.content)
	fp.close()
	i +=1





