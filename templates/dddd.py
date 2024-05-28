import re
import os
os.remove('ddd.html')
with open('趋势分析与预测.html','r',encoding='utf-8') as f:
    a = f.read()
    # print(a)
    a8 = re.findall('<body >(.*?)</body>',a,re.S)[0]
    with open('地域分布.html','r',encoding='utf-8') as f1:
        with open('ddd1.html','a+',encoding='utf-8') as f2:
            for i in f1:
                f2.write(i)
                if '<!-- 内容主体区域 -->' in i:
                    f2.write(a8)