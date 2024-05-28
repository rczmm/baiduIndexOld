import requests
from pyecharts import options as opts
from pyecharts.charts import Page,Bar
import os
import re
def cctv3():
    """
    请求年龄分布
    :return:
    """
    cookies = {
        'BIDUPSID': 'FDAA1B8D24A9AC6C5BE59F179C8B25AF',
        'PSTM': '1697112742',
        'BAIDUID': 'FDAA1B8D24A9AC6CF3DAA2B0C77211F6:FG=1',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        'BAIDUID_BFESS': 'FDAA1B8D24A9AC6CF3DAA2B0C77211F6:FG=1',
        'ZFY': 'okJ4I2QGveAsdk1phErIZgRJaG:BSx:APZQpxS7EAmIhc:C',
        'H_PS_PSSID': '40169_40206_40212_40216_40223_40059_40256_40294_40290_40288_40284_40317_40079',
        'BDRCVFR[feWj1Vr5u3D]': 'I67x6TjHwwYf0',
        'PSINO': '7',
        'delPer': '0',
        'Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc': '1709097128,1709272302',
        'BDUSS': 'i1GclhTcnNNRmRESTl4ZHlMcGF2dnV-Sldhekpmclo3SXJpcGNxMVM0blAtZ2htSUFBQUFBJCQAAAAAAQAAAAEAAABVSkJEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9t4WXPbeFld',
        'SIGNIN_UC': '70a2711cf1d3d9b1a82d2f87d633bd8a04592849777AyAyhzxRRbO3rIgG35cyPRnHrujH7yjTorJVkj%2BDvl7YIYKULqOUaprSX3842tmzcMTh2tOFXwGSaMUlD8M3yjSuYWVzga78R8aYyk2MfMx58Ae24N8KEQiIXGLcBYdHMu27F0BJejPqNzXF1HWdO4%2BIvaKDNJKDA08AJPTgeLxeKmd8IVavmIifOlCDeAQKVbhIUTBdJWh1FcxbqMuZBVbMCkJjtugW7gPnlimKSkcpAZleEuC25%2F0rJplx9zUpjXj3pjJ9XEoIPQ7IKTXT6zFDGKpCc6Q6j4GtulpKnOw%3D84956617799664577610611753469327',
        '__cas__rn__': '459284977',
        '__cas__st__212': '3e3fbb2fcc8fd8d05cd2dfb452aeaffa935e90ea40721f05023a18365b21c12e1738fa424b08bb0a3e402367',
        '__cas__id__212': '48260712',
        'CPTK_212': '766949107',
        'CPID_212': '48260712',
        'bdindexid': 'nb0im93j2dudrg82u4nkapm3u4',
        'BCLID': '18392871703744064655',
        'BCLID_BFESS': '18392871703744064655',
        'BDSFRCVID': 'l1IOJexroG3bL6vqIqluEHtYocpWxY5TDYrEOwXPsp3LGJLVYfzwEG0Pts1-dEu-S2EwogKKBgOTH4cCdm02jto8fsYfxjCw8H8btf8g0M5',
        'BDSFRCVID_BFESS': 'l1IOJexroG3bL6vqIqluEHtYocpWxY5TDYrEOwXPsp3LGJLVYfzwEG0Pts1-dEu-S2EwogKKBgOTH4cCdm02jto8fsYfxjCw8H8btf8g0M5',
        'H_BDCLCKID_SF': 'tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us3HCJ2hcHMPoosIOPX5j-KfFEKNj4Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt4MROoe-KyWfjOafJffg-O3tbDfn028DKuDj-WDjJXeaRabK6aKC5bL6rJabC3DKjVXU6q2bDeQNbaWT5q-m5DWP5NWPbZDnOx3n7Zjq0vWq54WbbvLT7johRTWqR4oJQu5UonDh83KNLLKUQtHGAHK43O5hvvER3O3MAM-UtOhH0HaJ3yfIcehRQy2qObbhP9-ROte-bQXH_E5bj2qRCj_DjP',
        'H_BDCLCKID_SF_BFESS': 'tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us3HCJ2hcHMPoosIOPX5j-KfFEKNj4Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt4MROoe-KyWfjOafJffg-O3tbDfn028DKuDj-WDjJXeaRabK6aKC5bL6rJabC3DKjVXU6q2bDeQNbaWT5q-m5DWP5NWPbZDnOx3n7Zjq0vWq54WbbvLT7johRTWqR4oJQu5UonDh83KNLLKUQtHGAHK43O5hvvER3O3MAM-UtOhH0HaJ3yfIcehRQy2qObbhP9-ROte-bQXH_E5bj2qRCj_DjP',
        'Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc': '1709283644',
        'ab_sr': '1.0.1_ODkzNTVkZDA3MzZmMjExNWU2ODUxYzYxOGZiOTA5YmRmMjM2NTdmOWIyZjk5NzhkZjkwODEzOTFhOWYxMDM4N2RkNzE5NzVlZGQzNGMyMjgyZmQzMmEyNTE3ZGM2MjU4MDUzOTQ2MWU5YmNlZmMzYmI1MWExM2ZiNDRhNjU0MjExNzc0ZmVlNjBhYTEyYjk5OTc0NGEzYzk5ZjBmNjIxMTYyOTlhODhkMGYwZWY5YzM5YjM5NGRlNjVmNDBiMTZjOWU3NjIzODNhNGM4YTQ2YWIyMDA5ZTMyNTgxYWUzNzY=',
        'RT': '"z=1&dm=baidu.com&si=76d1164c-48e3-4343-b708-7427a9a061c2&ss=lt8f5cso&sl=5&tt=5av&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=92x5"',
        'BDUSS_BFESS': 'i1GclhTcnNNRmRESTl4ZHlMcGF2dnV-Sldhekpmclo3SXJpcGNxMVM0blAtZ2htSUFBQUFBJCQAAAAAAQAAAAEAAABVSkJEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9t4WXPbeFld',
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://index.baidu.com/v2/main/index.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(
        'https://index.baidu.com/api/SocialApi/baseAttributes?wordlist[]=%E5%85%BB%E8%80%81',
        cookies=cookies,
        headers=headers,
    ).json()
    a = response['data']['result']
    lst = []
    for i in a:
        a1 = i['age']
        for u in a1:
            if u['tgi'] == '':
                pass
            else:
                yy = u['rate']
                lst.append(yy)
    a1 = lst[0]
    a2 = lst[1]
    a3 = lst[2]
    a4 = lst[3]
    a5 = lst[4]
    dic = {'0-19': a1, '20-29': a2, '30-39': a3, '40-49': a4, '50+': a5}
    data = ['0-19', '20-29', '30-39', '40-49', '50+']
    lst1 = [a1, a2, a3, a4, a5]
    bar = Bar(init_opts=opts.InitOpts(width="450px", height="350px", chart_id='bar'))
    bar.add_xaxis(data)
    bar.set_global_opts(title_opts=opts.TitleOpts('年龄分布'))
    bar.add_yaxis('年龄分布.html', lst1)
    return bar
def mian():
    """
    主函数
    """
    c = cctv3()
    page = Page(layout=Page.DraggablePageLayout)
    page.add(c)
    page.render()
    Page.save_resize_html("render.html", cfg_file=r"json文件/年龄.json", dest="tp/nianlin1.html")
    a111 = os.path.exists('templates/年龄1.html')
    print(a111)
    if a111:
        os.remove('templates/年龄1.html')
    with open('tp/nianlin1.html', 'r', encoding='utf-8') as f:
        a = f.read()
        a8 = re.findall('<body >(.*?)</body>', a, re.S)[0]
        with open('templates/年龄.html', 'r', encoding='utf-8') as f1:
            with open('templates/年龄1.html', 'a+', encoding='utf-8') as f2:
                for i in f1:
                    f2.write(i)
                    if '<!-- 内容主体区域 -->' in i:
                        f2.write(a8)
