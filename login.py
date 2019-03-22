#encoding=utf8
from __future__ import unicode_literals,print_function
import os
import re
import urllib
import math
import numpy as np
from zhihu_oauth import ZhihuClient
TOKEN_FILE='token.pkl'
client=ZhihuClient()
if os.path.isfile(TOKEN_FILE):
    client.load_token(TOKEN_FILE)
else:
    client.login_in_terminal('407140599@qq.com','xhdbfs1234567')
    client.save_token(TOKEN_FILE)
id=24400664
question=client.question(id)
print("question: "+question.title)
print("回答数量: ",question.answer_count)
#os.mkdir(question.title+" pics")
path=question.title+" pics"
index=1
arr=[]
for answer in question.answers:
    arr.append(answer.voteup_count)
mean=np.mean(arr)
print(mean)
std=np.std(arr)
print(std)
for answer in question.answers:
    if answer.voteup_count <2000:
        continue
    content=answer.content
    re_compile=re.compile(r'<img src="(https://pic\d\.zhimg\.com/.*?\.(jpg|png))".*?>')
    img_lists=re.findall(re_compile,content)
    if(img_lists):
        for img in img_lists:
            img_url=img[0]
            f=urllib.request.urlopen(img_url)
            data=f.read()
            with open("pic%d.jpg" % index,"wb") as code:
                code.write(data)
            print(u"成功保存第%d张图片" % index)
            index+=1
