import requests
import pyecharts.options as opts
from pyecharts.charts import WordCloud
from pyecharts.charts import Page
import re
import os
cookies = {
    'BIDUPSID': '7995097E5D99D26A2876070E7D57A2D0',
    'PSTM': '1706699410',
    'BAIDUID': '6CB15A3376911009F1FF7388F4B7D212:FG=1',
    'newlogin': '1',
    'BAIDUID_BFESS': '6CB15A3376911009F1FF7388F4B7D212:FG=1',
    'ZFY': '5PJBc4FQ7ZhJWrJUoQEKDHmHS6vkaGE2eG:AZ5ORWg94:C',
    'H_PS_PSSID': '40210_40207_40217_40222_40061_40294_40290_40287_40286_40317_40320_40079',
    'BDORZ': 'FFFB88E999055A3F8A630C64834BD6D0',
    'BDRCVFR[E6DhbwomKun]': '9xWipS8B-FspA7EnHc1QhPEUf',
    'PSINO': '7',
    'Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc': '1709095843,1709271023,1709372773',
    'BDUSS': 'hBR1FjdVdRRDl1V2c3LWhqUGlsQUpCbjhWVHp1fmhiQjFlZjFLaDJMdkxnZ3BtSUFBQUFBJCQAAAAAAAAAAAEAAACLZV1qQm95ZbH5wejRqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMv14mXL9eJlYV',
    'delPer': '0',
    'BDRCVFR[tox4WRQ4-Km]': 'mk3SLVN4HKm',
    'BDRCVFR[-pGxjrCMryR]': 'mk3SLVN4HKm',
    'BCLID': '16202411547715813152',
    'BCLID_BFESS': '16202411547715813152',
    'BDSFRCVID': 'DI-OJeC62iOnT_oqITWAEHtYog4fYDRTH6aom5w8Cwo2m1wmmBH7EG0PIU8g0KuMKJvgogKKBgOTH4cCdm02THRHfE7CF3PCc23mtf8g0f5',
    'BDSFRCVID_BFESS': 'DI-OJeC62iOnT_oqITWAEHtYog4fYDRTH6aom5w8Cwo2m1wmmBH7EG0PIU8g0KuMKJvgogKKBgOTH4cCdm02THRHfE7CF3PCc23mtf8g0f5',
    'H_BDCLCKID_SF': 'tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us-GuJ2hcHMPoosIOPX5j-KfFWDJ34Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-KkjPblJhOmKbueW4bDfn028DKuDT0-jjo3DGDs54TEHDcWL5rJabC3Vx_9XU6qLT5XeJb-QPTI-m5A2I3NWPbZDn3oXUcAhl0njxQy0PTTQI7gWfJ-WljSDJ5oyfonDh842a7MJUntKjvCsR7O5hvvER3O3MAM-UtOhH0HLUvNWIc4_hOItMJTHI_RhJOte-bQ2a_EtT8qJRKfVIIQb-3bKRnpMtJqKPktqxby26nRW4j9aJ5nJDoE8nr2BPnayq0iLto7-pcy5bnhhlb4QpP-HJ7zjJtWLn-eDxFD--rL0e-fKl0MLpTlbb0xynoYyUIBbUnMBMnG52OnaIbJ0bbVhKo2yh51bxQWLPDeQUJ2tJ7LLnLy5KJtMDcnK4-XDTjLeaQP',
    'H_BDCLCKID_SF_BFESS': 'tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us-GuJ2hcHMPoosIOPX5j-KfFWDJ34Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-KkjPblJhOmKbueW4bDfn028DKuDT0-jjo3DGDs54TEHDcWL5rJabC3Vx_9XU6qLT5XeJb-QPTI-m5A2I3NWPbZDn3oXUcAhl0njxQy0PTTQI7gWfJ-WljSDJ5oyfonDh842a7MJUntKjvCsR7O5hvvER3O3MAM-UtOhH0HLUvNWIc4_hOItMJTHI_RhJOte-bQ2a_EtT8qJRKfVIIQb-3bKRnpMtJqKPktqxby26nRW4j9aJ5nJDoE8nr2BPnayq0iLto7-pcy5bnhhlb4QpP-HJ7zjJtWLn-eDxFD--rL0e-fKl0MLpTlbb0xynoYyUIBbUnMBMnG52OnaIbJ0bbVhKo2yh51bxQWLPDeQUJ2tJ7LLnLy5KJtMDcnK4-XDTjLeaQP',
    'SIGNIN_UC': '70a2711cf1d3d9b1a82d2f87d633bd8a045946439998J5mZrUXJUAdfeD%2F%2Bq0wyufOL6EFLoYjrHmC7pTBArfypEVxn%2Fp0t6VJrtHpp9NALtyw7TmGK5ZqNuARyytbka3X%2FtEyyUpgZ4R3RNBYMIkcGqjHowik1hcqgKttDZE3KdfO3rXbKrr1ms5lIsy7I%2F697xK4Zj5V%2BhNRrXodIGoaw7lrb2K27iO4nWCTar9it1EUGvqWRMQX2k6%2Bf7ruGERHZgZCHIzP%2FBAuPovCvq4wIOKljFxnmgIKopyUrQoCDH1shpcb2soNoVTFFcj2IzPoHXo5PZCel%2BtSuNVduXYy0gEObXyfKa%2BFOpWnIdcY36230177515307394365842031532687',
    '__cas__rn__': '459464399',
    '__cas__st__212': 'a1ff905cc3b1124528303b037b026942a74a46662c409f08bb0a3d40204c45fa2cf9bab8a1de0d302a1a388a',
    '__cas__id__212': '45993938',
    'CPTK_212': '2000481705',
    'CPID_212': '45993938',
    'bdindexid': 'h5s9imkendgbikc91db0oi8e60',
    'Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc': '1709461665',
    'ab_sr': '1.0.1_NzRjMTIzOTJlN2M5NjZhZjg1OWU1NDE4ZTc1M2JjODFmYTk2NDBhMjBiYmI1YTI4ZTA1OTY1NTM0YWZiNzY1OTgxMmYzYjkxY2NiMTc1NjU5OGU5MjUzNDQyMzg1YmM4ZjA2ZGM5MDY4NjBiZGRmYTQ2OTlkZTMzODcxMmE1YWQxNGRkNDY1NWMwNmUyNjM1Njk1NzVlODJjODEzZmQ3OGJkODRkNTJlZjM5MTE2MDk3MGExNDUwNDdiNjE2MTZhMWIwNWJkMjA5NGY4M2NiYzE4OWY3OTYzMWM5MjI5YjE=',
    'BDUSS_BFESS': 'hBR1FjdVdRRDl1V2c3LWhqUGlsQUpCbjhWVHp1fmhiQjFlZjFLaDJMdkxnZ3BtSUFBQUFBJCQAAAAAAAAAAAEAAACLZV1qQm95ZbH5wejRqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMv14mXL9eJlYV',
    'RT': '"z=1&dm=baidu.com&si=3327a95d-a655-4753-b71c-c667398c835d&ss=ltbe8gtd&sl=1&tt=mt&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1f0"',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'BIDUPSID=7995097E5D99D26A2876070E7D57A2D0; PSTM=1706699410; BAIDUID=6CB15A3376911009F1FF7388F4B7D212:FG=1; newlogin=1; BAIDUID_BFESS=6CB15A3376911009F1FF7388F4B7D212:FG=1; ZFY=5PJBc4FQ7ZhJWrJUoQEKDHmHS6vkaGE2eG:AZ5ORWg94:C; H_PS_PSSID=40210_40207_40217_40222_40061_40294_40290_40287_40286_40317_40320_40079; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[E6DhbwomKun]=9xWipS8B-FspA7EnHc1QhPEUf; PSINO=7; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1709095843,1709271023,1709372773; BDUSS=hBR1FjdVdRRDl1V2c3LWhqUGlsQUpCbjhWVHp1fmhiQjFlZjFLaDJMdkxnZ3BtSUFBQUFBJCQAAAAAAAAAAAEAAACLZV1qQm95ZbH5wejRqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMv14mXL9eJlYV; delPer=0; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BCLID=16202411547715813152; BCLID_BFESS=16202411547715813152; BDSFRCVID=DI-OJeC62iOnT_oqITWAEHtYog4fYDRTH6aom5w8Cwo2m1wmmBH7EG0PIU8g0KuMKJvgogKKBgOTH4cCdm02THRHfE7CF3PCc23mtf8g0f5; BDSFRCVID_BFESS=DI-OJeC62iOnT_oqITWAEHtYog4fYDRTH6aom5w8Cwo2m1wmmBH7EG0PIU8g0KuMKJvgogKKBgOTH4cCdm02THRHfE7CF3PCc23mtf8g0f5; H_BDCLCKID_SF=tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us-GuJ2hcHMPoosIOPX5j-KfFWDJ34Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-KkjPblJhOmKbueW4bDfn028DKuDT0-jjo3DGDs54TEHDcWL5rJabC3Vx_9XU6qLT5XeJb-QPTI-m5A2I3NWPbZDn3oXUcAhl0njxQy0PTTQI7gWfJ-WljSDJ5oyfonDh842a7MJUntKjvCsR7O5hvvER3O3MAM-UtOhH0HLUvNWIc4_hOItMJTHI_RhJOte-bQ2a_EtT8qJRKfVIIQb-3bKRnpMtJqKPktqxby26nRW4j9aJ5nJDoE8nr2BPnayq0iLto7-pcy5bnhhlb4QpP-HJ7zjJtWLn-eDxFD--rL0e-fKl0MLpTlbb0xynoYyUIBbUnMBMnG52OnaIbJ0bbVhKo2yh51bxQWLPDeQUJ2tJ7LLnLy5KJtMDcnK4-XDTjLeaQP; H_BDCLCKID_SF_BFESS=tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us-GuJ2hcHMPoosIOPX5j-KfFWDJ34Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-KkjPblJhOmKbueW4bDfn028DKuDT0-jjo3DGDs54TEHDcWL5rJabC3Vx_9XU6qLT5XeJb-QPTI-m5A2I3NWPbZDn3oXUcAhl0njxQy0PTTQI7gWfJ-WljSDJ5oyfonDh842a7MJUntKjvCsR7O5hvvER3O3MAM-UtOhH0HLUvNWIc4_hOItMJTHI_RhJOte-bQ2a_EtT8qJRKfVIIQb-3bKRnpMtJqKPktqxby26nRW4j9aJ5nJDoE8nr2BPnayq0iLto7-pcy5bnhhlb4QpP-HJ7zjJtWLn-eDxFD--rL0e-fKl0MLpTlbb0xynoYyUIBbUnMBMnG52OnaIbJ0bbVhKo2yh51bxQWLPDeQUJ2tJ7LLnLy5KJtMDcnK4-XDTjLeaQP; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a045946439998J5mZrUXJUAdfeD%2F%2Bq0wyufOL6EFLoYjrHmC7pTBArfypEVxn%2Fp0t6VJrtHpp9NALtyw7TmGK5ZqNuARyytbka3X%2FtEyyUpgZ4R3RNBYMIkcGqjHowik1hcqgKttDZE3KdfO3rXbKrr1ms5lIsy7I%2F697xK4Zj5V%2BhNRrXodIGoaw7lrb2K27iO4nWCTar9it1EUGvqWRMQX2k6%2Bf7ruGERHZgZCHIzP%2FBAuPovCvq4wIOKljFxnmgIKopyUrQoCDH1shpcb2soNoVTFFcj2IzPoHXo5PZCel%2BtSuNVduXYy0gEObXyfKa%2BFOpWnIdcY36230177515307394365842031532687; __cas__rn__=459464399; __cas__st__212=a1ff905cc3b1124528303b037b026942a74a46662c409f08bb0a3d40204c45fa2cf9bab8a1de0d302a1a388a; __cas__id__212=45993938; CPTK_212=2000481705; CPID_212=45993938; bdindexid=h5s9imkendgbikc91db0oi8e60; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1709461665; ab_sr=1.0.1_NzRjMTIzOTJlN2M5NjZhZjg1OWU1NDE4ZTc1M2JjODFmYTk2NDBhMjBiYmI1YTI4ZTA1OTY1NTM0YWZiNzY1OTgxMmYzYjkxY2NiMTc1NjU5OGU5MjUzNDQyMzg1YmM4ZjA2ZGM5MDY4NjBiZGRmYTQ2OTlkZTMzODcxMmE1YWQxNGRkNDY1NWMwNmUyNjM1Njk1NzVlODJjODEzZmQ3OGJkODRkNTJlZjM5MTE2MDk3MGExNDUwNDdiNjE2MTZhMWIwNWJkMjA5NGY4M2NiYzE4OWY3OTYzMWM5MjI5YjE=; BDUSS_BFESS=hBR1FjdVdRRDl1V2c3LWhqUGlsQUpCbjhWVHp1fmhiQjFlZjFLaDJMdkxnZ3BtSUFBQUFBJCQAAAAAAAAAAAEAAACLZV1qQm95ZbH5wejRqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMv14mXL9eJlYV; RT="z=1&dm=baidu.com&si=3327a95d-a655-4753-b71c-c667398c835d&ss=ltbe8gtd&sl=1&tt=mt&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1f0"',
    'Referer': 'https://index.baidu.com/v2/main/index.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://index.baidu.com/api/WordGraph/multi?wordlist[]=%E5%85%BB%E8%80%81&datelist=20240225',
    cookies=cookies,
    headers=headers,
).json()
a = response['data']['wordlist']
data = []#创建一个全局列表将数据以元组的方法放进去
# 通过for循环来处理数据
for i in a:
    aa = i['wordGraph']#提取下一层的列表
    for ii in aa:
        a1 = ii['word']
        dic = {}
        dic['相关词'] = a1
        dic['pv'] = ii['pv']
        data.append((a1,ii['pv']))#通过列表.append 的方法将数据追加进入
        print(dic)
def cctv():
    #构造可视化
    a = (
        WordCloud(init_opts=opts.InitOpts(width="450px", height="350px",chart_id='gjcdid1'))
        .add(series_name="关键词", data_pair=data, word_size_range=[25, 66])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="关键词", title_textstyle_opts=opts.TextStyleOpts(font_size=30)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        #.render("basic_wordcloud.html")
    )
    #将ID返回
    return a
def mian():
    c = cctv()
    page = Page(layout=Page.DraggablePageLayout)
    page.add(c)
    page.render()
    Page.save_resize_html("render.html", cfg_file=r"json文件/gjc7.json", dest="templates/gjc.html")#将布局导入到一个新的文件中
    a111 = os.path.exists('templates/关键词1.html')
    print(a111)
    if a111 != False:
        os.remove('templates/关键词1.html')
    with open('templates/gjc.html', 'r', encoding='utf-8') as f:
        a = f.read()
        # print(a)
        a8 = re.findall('<body >(.*?)</body>', a, re.S)[0]
        with open('templates/关键词.html', 'r', encoding='utf-8') as f1:
            with open('templates/关键词1.html', 'a+', encoding='utf-8') as f2:
                for i in f1:
                    f2.write(i)
                    if '<!-- 内容主体区域 -->' in i:
                        f2.write(a8)
