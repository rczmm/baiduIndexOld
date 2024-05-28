import os
import re

import requests
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.charts import Page

def ccc():
    """
    热搜变化
    :return:
    """
    cookies = {
        'BIDUPSID': 'FDAA1B8D24A9AC6C5BE59F179C8B25AF',
        'PSTM': '1697112742',
        'BAIDUID': 'FDAA1B8D24A9AC6CF3DAA2B0C77211F6:FG=1',
        'H_PS_PSSID': '40169_40206_40212_40216_40223_40059_40256_40294_40290_40288_40284_40317_40079',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        'delPer': '0',
        'PSINO': '7',
        'BA_HECTOR': 'ak2k8g0k8k0l8kaka08h810kadkbui1iu84fi1s',
        'BAIDUID_BFESS': 'FDAA1B8D24A9AC6CF3DAA2B0C77211F6:FG=1',
        'ZFY': 'Jptlxi7nn1QsOrlp4OaBVyuiAF7PDQQYIJejKU:AzjE8:C',
        'BCLID': '7883386685317069287',
        'BCLID_BFESS': '7883386685317069287',
        'BDSFRCVID': 'uO_OJexroG3bL6vqT5xIEHtYocpWxY5TDYrELPfiaimDVu-VYfzwEG0Pts1-dEu-S2EwogKKBgOTH4cCdm02THRHfEzLe22a9YLntf8g0M5',
        'BDSFRCVID_BFESS': 'uO_OJexroG3bL6vqT5xIEHtYocpWxY5TDYrELPfiaimDVu-VYfzwEG0Pts1-dEu-S2EwogKKBgOTH4cCdm02THRHfEzLe22a9YLntf8g0M5',
        'H_BDCLCKID_SF': 'tRAOoC8-fIvEDRbN2KTD-tFO5eT22-usbmOd2hcHMPoosIOPX5j-Kq302-r4Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-Kk24v-JjjKfG5rWtbDfn028DKu-n5jHjQ-jH_D3f',
        'H_BDCLCKID_SF_BFESS': 'tRAOoC8-fIvEDRbN2KTD-tFO5eT22-usbmOd2hcHMPoosIOPX5j-Kq302-r4Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-Kk24v-JjjKfG5rWtbDfn028DKu-n5jHjQ-jH_D3f',
        'Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc': '1709097128,1709272302,1709445620',
        'BDUSS': '0d3UU9yM01tVG9QY3FVVTZYNlJjQldGRjBtM1ZNYVdhSnA3a21iVkliN0xud3RtSUFBQUFBJCQAAAAAAQAAAAEAAABVSkJEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMsS5GXLEuRlV',
        'SIGNIN_UC': '70a2711cf1d3d9b1a82d2f87d633bd8a04594582855qeLH%2FZ%2ByTbnLG9BYiD%2BNbvLiVhVJ3T0VIBdWIFS2w0XWesaA7mOaCsGuMZKm%2FoOO4QExVKsr1ckDh1Udq5CumZxu2TPq%2BtVQkQR%2FY38zK%2FfBEHnPYzL9p2dMzJQkK5qZtesby1JQqub6hSYctcAHl673Z3weoWoZMJmw9DEZuensuQlT0KbxndilTF13l%2FUuC6ZFVrBaOV%2FA137PeDkrLhF4Afgt9jchqViEkNGQe4tcEvCG%2B51CkrD%2FY5vu0A90DtyTsnmZdMLaloCEzCLdmVyEdR9yYFdm5nxFk%2F2f6ms%3D40866642697970872329851818245772',
        '__cas__rn__': '459458285',
        '__cas__st__212': 'bc429ed283fc9924b9204410bdacc75e7b2da92f1658aed9b391dbf99335b83a6740ff15241cab78be536f47',
        '__cas__id__212': '48260712',
        'CPTK_212': '1606633426',
        'CPID_212': '48260712',
        'bdindexid': 'rn881aj328qgpe314iassto805',
        'BDRCVFR[feWj1Vr5u3D]': 'I67x6TjHwwYf0',
        'RT': '"z=1&dm=baidu.com&si=602a150b-bb9d-4cb8-8716-accaec9949e8&ss=ltb90jdz&sl=3&tt=3nf&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"',
        'Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc': '1709455063',
        'ab_sr': '1.0.1_YjdhZTNlNGYyNjY0ZDhmNjY3N2I1OGI2ZWVkMmU4MDk5OWQzZmY5NmMzZTdkMTQzMjMyOTQxMTZiN2FhMTQ0Njg4MjU3ZDZkMjE5ZjY4MDFkMjM2NzQwODQ1NjAxOWZiMWQ4NzYyMGI3NzExOGQ5NWZjZDQ1YTY2ZGI4NzhhM2QxYmE4YmVhNDQxNDAwZDE2MTJmNDcwNDVlMGY3N2E2N2NkODNhMTc2MWU3M2M1OTU3ZjdjN2IzYjU0OTk3YzY4M2QwYWEzNDc1YTMwMmE0ZDZjNTcyMTMwYzJjZmYwZDI=',
        'BDUSS_BFESS': '0d3UU9yM01tVG9QY3FVVTZYNlJjQldGRjBtM1ZNYVdhSnA3a21iVkliN0xud3RtSUFBQUFBJCQAAAAAAQAAAAEAAABVSkJEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMsS5GXLEuRlV',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'BIDUPSID=FDAA1B8D24A9AC6C5BE59F179C8B25AF; PSTM=1697112742; BAIDUID=FDAA1B8D24A9AC6CF3DAA2B0C77211F6:FG=1; H_PS_PSSID=40169_40206_40212_40216_40223_40059_40256_40294_40290_40288_40284_40317_40079; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=7; BA_HECTOR=ak2k8g0k8k0l8kaka08h810kadkbui1iu84fi1s; BAIDUID_BFESS=FDAA1B8D24A9AC6CF3DAA2B0C77211F6:FG=1; ZFY=Jptlxi7nn1QsOrlp4OaBVyuiAF7PDQQYIJejKU:AzjE8:C; BCLID=7883386685317069287; BCLID_BFESS=7883386685317069287; BDSFRCVID=uO_OJexroG3bL6vqT5xIEHtYocpWxY5TDYrELPfiaimDVu-VYfzwEG0Pts1-dEu-S2EwogKKBgOTH4cCdm02THRHfEzLe22a9YLntf8g0M5; BDSFRCVID_BFESS=uO_OJexroG3bL6vqT5xIEHtYocpWxY5TDYrELPfiaimDVu-VYfzwEG0Pts1-dEu-S2EwogKKBgOTH4cCdm02THRHfEzLe22a9YLntf8g0M5; H_BDCLCKID_SF=tRAOoC8-fIvEDRbN2KTD-tFO5eT22-usbmOd2hcHMPoosIOPX5j-Kq302-r4Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-Kk24v-JjjKfG5rWtbDfn028DKu-n5jHjQ-jH_D3f; H_BDCLCKID_SF_BFESS=tRAOoC8-fIvEDRbN2KTD-tFO5eT22-usbmOd2hcHMPoosIOPX5j-Kq302-r4Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-Kk24v-JjjKfG5rWtbDfn028DKu-n5jHjQ-jH_D3f; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1709097128,1709272302,1709445620; BDUSS=0d3UU9yM01tVG9QY3FVVTZYNlJjQldGRjBtM1ZNYVdhSnA3a21iVkliN0xud3RtSUFBQUFBJCQAAAAAAQAAAAEAAABVSkJEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMsS5GXLEuRlV; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04594582855qeLH%2FZ%2ByTbnLG9BYiD%2BNbvLiVhVJ3T0VIBdWIFS2w0XWesaA7mOaCsGuMZKm%2FoOO4QExVKsr1ckDh1Udq5CumZxu2TPq%2BtVQkQR%2FY38zK%2FfBEHnPYzL9p2dMzJQkK5qZtesby1JQqub6hSYctcAHl673Z3weoWoZMJmw9DEZuensuQlT0KbxndilTF13l%2FUuC6ZFVrBaOV%2FA137PeDkrLhF4Afgt9jchqViEkNGQe4tcEvCG%2B51CkrD%2FY5vu0A90DtyTsnmZdMLaloCEzCLdmVyEdR9yYFdm5nxFk%2F2f6ms%3D40866642697970872329851818245772; __cas__rn__=459458285; __cas__st__212=bc429ed283fc9924b9204410bdacc75e7b2da92f1658aed9b391dbf99335b83a6740ff15241cab78be536f47; __cas__id__212=48260712; CPTK_212=1606633426; CPID_212=48260712; bdindexid=rn881aj328qgpe314iassto805; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; RT="z=1&dm=baidu.com&si=602a150b-bb9d-4cb8-8716-accaec9949e8&ss=ltb90jdz&sl=3&tt=3nf&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1709455063; ab_sr=1.0.1_YjdhZTNlNGYyNjY0ZDhmNjY3N2I1OGI2ZWVkMmU4MDk5OWQzZmY5NmMzZTdkMTQzMjMyOTQxMTZiN2FhMTQ0Njg4MjU3ZDZkMjE5ZjY4MDFkMjM2NzQwODQ1NjAxOWZiMWQ4NzYyMGI3NzExOGQ5NWZjZDQ1YTY2ZGI4NzhhM2QxYmE4YmVhNDQxNDAwZDE2MTJmNDcwNDVlMGY3N2E2N2NkODNhMTc2MWU3M2M1OTU3ZjdjN2IzYjU0OTk3YzY4M2QwYWEzNDc1YTMwMmE0ZDZjNTcyMTMwYzJjZmYwZDI=; BDUSS_BFESS=0d3UU9yM01tVG9QY3FVVTZYNlJjQldGRjBtM1ZNYVdhSnA3a21iVkliN0xud3RtSUFBQUFBJCQAAAAAAQAAAAEAAABVSkJEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMsS5GXLEuRlV',
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
        'https://index.baidu.com/api/WordGraph/multi?wordlist[]=%E5%85%BB%E8%80%81',
        cookies=cookies,
        headers=headers,
    ).json()
    a = response['data']['wordlist']
    dates = []
    counts = []
    for i in a:
        aa = i['wordGraph']
        for ii in aa:
            a1 = ii['word']
            dic = {}
            dic['相关词'] = a1
            dic['pv'] = ii['pv']
            dates.append(a1)
            counts.append(ii['pv'])
            print(dic)
    x = dates
    y1 = counts
    wwww = (Line(init_opts=opts.InitOpts(width="450px", height="350px",chart_id='ww1'))
        .add_xaxis(x)
        .add_yaxis("热点", y1)
        .set_global_opts(title_opts = opts.TitleOpts(title = ' '))
        #.render("热点话题.html")   # 用于保存绘制的图形，此处可自定义路径
    )
    return  wwww
def mian():
    c = ccc()
    page = Page(layout=Page.DraggablePageLayout)
    page.add(c)
    page.render()
    Page.save_resize_html("render.html", cfg_file=r"json文件/热点.json", dest="tp/热点话题7.html")
    a111 = os.path.exists('templates/热点话题1.html')
    print(a111)
    if a111 != False:
        os.remove('templates/热点话题1.html')
    with open('tp/热点话题7.html', 'r', encoding='utf-8') as f:
        a = f.read()
        # print(a)
        a8 = re.findall('<body >(.*?)</body>', a, re.S)[0]
        with open('templates/热点话题.html', 'r', encoding='utf-8') as f1:
            with open('templates/热点话题1.html', 'a+', encoding='utf-8') as f2:
                for i in f1:
                    f2.write(i)
                    if '<!-- 内容主体区域 -->' in i:
                        f2.write(a8)
