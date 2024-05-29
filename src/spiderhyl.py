import json
import re
import sys

import requests
import pymysql


def decrypt_func(key: str, data: str):
    a = key
    i = data
    n = {}
    s = []
    for o in range(len(a) // 2):
        n[a[o]] = a[len(a) // 2 + o]
    for r in range(len(data)):
        s.append(n[i[r]])
    return ''.join(s).split(',')


def get_ptbk(uniqid, headers):
    url = 'http://index.baidu.com/Interface/ptbk?uniqid={}'
    resp = requests.get(url.format(uniqid), headers=headers)

    if resp.status_code != 200:
        print('获取uniqid失败')
        sys.exit(1)
    print(resp.json())
    return resp.json().get('data')

lst = []

def cctv():
    """
    请求函数
    """
    url = ('https://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22%E5%85%BB%E8%80%81%22,'
           '%22wordType%22:1%7D]]&days=30')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.82 Safari/537.36",
        "Host": "index.baidu.com",
        "Referer": "https://index.baidu.com/v2/main/index.html",
        "Cipher-Text": '1678957310295_1678973070798_OMIhFKRPoUQLLQneOiAVA+Uhm6CsO2+eDthnrOONKvN1r37'
                       '/2lIMxBp7qwJuKko5khhNRdDoREGL5qseIVc+fX1wyPDL2CEr3zxnY8Gcsmf3/0t79SKoGVhItnRmEoTX2NjhadRe'
                       '+UypG5B+LdLN5QpBek6AoZbW/WWLQufVsKhWXXVgypp9GpG7rOQNn+jslbW+CzOjhMPbxSfuag3n'
                       '/S2gEpdshSZbpPV62AJQ4rXjeRS9WGibWLcNRFuI/Ssj2vF5FA+BNFt6OH6AwJBRB3'
                       '/n7UdeobasL5dc9xoLHeljtKPqb6MzyLR0WgJDQUGwmI84s3cKpmqbeTRmVcQh'
                       '+Tma2I8ZxS7CPWYaLAcEIPCHKX26kEqUdjO+Xhedcj/J'}
    cookies = {
        'Cookie': 'PSTM=1682491171; BAIDUID=D08A8F03772023E84A7F570864D944A1:FG=1; '
                  'BIDUPSID=0ABB0E3A787AC1C023847A63E0079A44; '
                  'BDUSS'
                  '=xLbllRQ2FWVDh2d1hIfjFncngyZzBVWllyUlhxcjlWdUJFbDhoTGhwZmZDNkZrRVFBQUFBJCQAAAAAAAAAAAEAAACLZV1qQm95ZbH5wejRqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN9-eWTffnlkem; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=D08A8F03772023E84A7F570864D944A1:FG=1; ZFY=SJ:B1bwupZhfzszZKSksZQ:AwJbdT:BEOqwvquZTnvKjzM:C; H_PS_PSSID=38515_36542_38687_38859_38798_38903_38768_38793_38841_38831_38486_38809_38822_38835_38636_38507_26350; BA_HECTOR=ag8kaha08l0k24al8g00ag2d1i8lf4j1o; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=7; delPer=0; BCLID=11010605717629679720; BCLID_BFESS=11010605717629679720; BDSFRCVID=Vz8OJexroG0i0JJfiZDvKCYlArpWxY5TDYrEOwXPsp3LGJLVFqB6EG0Pts1-dEu-S2EwogKKBgOTH4FF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=Vz8OJexroG0i0JJfiZDvKCYlArpWxY5TDYrEOwXPsp3LGJLVFqB6EG0Pts1-dEu-S2EwogKKBgOTH4FF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us5bcr2hcHMPoosIJYDM6kb4FlQMOi3hcQ06rj--nwJxbUotoHXh3tMt_thtOp-Crp3j6G_q5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP23qQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDj-WDjJXeaRabK6aKC5bL6rJabC3eMTsXU6q2bDeQN30JUTZ5D5zKnbc0MTSEtox3n7Zjq0vWq54WbbvLT7johRTWqR4s4jtjxonDh83KNLLKUQtHGAHK43O5hvvER3O3MAMQxKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJ6tOtRAHVIvt-5rDHJTg5DTjhPrM3lCOWMT-MTryKKJVtpckeRTLQbjvLpFjLq5jLbvkJGnRh4oNB-3iV-OxDUvnyxAZQlQGtfQxtNRJQKDE5p5hKf84QJJobUPULxJ9LUkJ3ecdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-D_9ej0K3e; H_BDCLCKID_SF_BFESS=tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us5bcr2hcHMPoosIJYDM6kb4FlQMOi3hcQ06rj--nwJxbUotoHXh3tMt_thtOp-Crp3j6G_q5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP23qQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDj-WDjJXeaRabK6aKC5bL6rJabC3eMTsXU6q2bDeQN30JUTZ5D5zKnbc0MTSEtox3n7Zjq0vWq54WbbvLT7johRTWqR4s4jtjxonDh83KNLLKUQtHGAHK43O5hvvER3O3MAMQxKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJ6tOtRAHVIvt-5rDHJTg5DTjhPrM3lCOWMT-MTryKKJVtpckeRTLQbjvLpFjLq5jLbvkJGnRh4oNB-3iV-OxDUvnyxAZQlQGtfQxtNRJQKDE5p5hKf84QJJobUPULxJ9LUkJ3ecdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-D_9ej0K3e; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04368269733MCjOz5Zy8%2FZ1qm8%2FjVkbC0jl8gyGhavjCNoHQj5j82havzgOj%2Ffbvzw3V%2BxAXPQ3XxcUsUV%2B1EtmpeHUaJPpmNaJQxC%2BO6jEcx%2B%2Bzj2R0K4FNECLFkOHDfTSRYDfdAVuJNXLMaQJUCxP%2B1vwgtYUMR4NFLnC3FXFvJyuZRs1CaXCphGBBcpM5qSMK5xBbT%2BDgzGVjv8%2FElZVACzb0dmIVwyqC7KL2hFHxLcYa6WWP3MS2xl8wLVGVc%2FVsDpRWthNgj46U6e4vb2WqI%2FEB5QJaiMtvUbBjqPIt2S01cJNi4Zmz5HgjRgRzioisymNYbF%2B90808915272370019720652156242203; __cas__rn__=436826973; bdindexid=suo1fou7ukvjna9dj330bc7nc4; __cas__st__212=4cb3883b827a77cb6debec1e11f4cf756963f63245d3423308e00d4f27d4952bc80a3edb2173dbde304901f9; __cas__id__212=45993938; CPID_212=45993938; CPTK_212=1456279933; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1685608763,1685683904,1686302273,1686814512; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1686814595; ab_sr=1.0.1_MDVjYjlhODNkODJlNTI4NWY4MDkzODQ3MDZhNDA5NDNiMzI3NGExYzdmNjQ1NDYxMGE2MzdiN2VjMGZiMGNmOGMxNDA4M2JkNDFkNmNjZWNhZDZmNDIyNTFjYTJlOGE3MzA2YzNhN2U0NzE4OTRjYzZmZmU4NTE2NDkzYjcyZDFhNDA2MGQ1ZTc4OGI0MmY3MDhmZGI2MDAxN2ZjOTUwZg==; BDUSS_BFESS=xLbllRQ2FWVDh2d1hIfjFncngyZzBVWllyUlhxcjlWdUJFbDhoTGhwZmZDNkZrRVFBQUFBJCQAAAAAAAAAAAEAAACLZV1qQm95ZbH5wejRqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN9-eWTffnlkem; RT="z=1&dm=baidu.com&si=1395e6c7-6e29-4580-a4eb-e80857ff3c37&ss=liwtt0lt&sl=7&tt=faq&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1x80"'
    }
    response = requests.get(url, headers=headers, cookies=cookies).text  # 发送请求，返回文本内容
    data = json.loads(response)  # 将内容转为字符串
    print(data)
    uniqid = data['data']['uniqid']
    data = data['data']['userIndexes'][0]['all']['data']  # 提取pc+移动数据
    uid = get_ptbk(uniqid, headers)  # 获取uniqid
    print(uid)
    result = decrypt_func(uid, data)
    result = result.split(',')  # 以逗号做分隔符 生成一个列表
    lst20 = [i for i in range(1, 31)]
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        db='test',
        password='495000',  # 密码
        #
    )
    # 创建游标对象
    cursor = conn.cursor()
    # 先执行删除语句：如果存在表test0614，则删除。这是为了后续调试的方便
    cursor.execute("drop table if exists zhishu")
    cursor.execute("CREATE TABLE zhishu (时间 VARCHAR(255),指数 VARCHAR(255))")  # 传入参数  ,zhiduan VARCHAR(255))
    for time, name in zip(lst20, result):  # 将两个列表压缩成一个列表
        dic = {'时间': time, '指数': name}
        print(dic)
        sql = insert_sql(dic, 'zhishu')
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def insert_sql(res, table):
    """
    将字典处理，传入数据和表名
    :param res:
    :param table:
    :return: 返回一个sql 语句
    """
    # 列的字段
    keys = ', '.join(res.keys())
    # 行字段
    values = list(res.values())
    values = str(values).strip('[]')
    sql = 'INSERT INTO {table}({keys}) VALUES ({values});'.format(table=table, keys=keys, values=values)
    return sql


def cctv2():
    """
    关键词分析
    :return: 返回用户在搜索数据时相关的关键词
    """
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        db='test',
        password='495000',  # 密码
        #
    )
    # 创建游标对象
    cursor = conn.cursor()
    # 先执行删除语句：如果存在表test0614，则删除。这是为了后续调试的方便
    cursor.execute("drop table if exists xiangguan")
    cursor.execute("CREATE TABLE xiangguan (数据 VARCHAR(255))")  # 传入参数  ,zhiduan VARCHAR(255))
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
        'BCLID': '15903098910969071346',
        'BCLID_BFESS': '15903098910969071346',
        'BDSFRCVID': 'qR4OJexroG3bL6vqIw1PEHtYocpWxY5TDYrELPfiaimDVu-VYfzwEG0Pts1-dEu-S2EwogKKBgOTH4cCdm02THRHfE7CF3PCc23mtf8g0M5',
        'BDSFRCVID_BFESS': 'qR4OJexroG3bL6vqIw1PEHtYocpWxY5TDYrELPfiaimDVu-VYfzwEG0Pts1-dEu-S2EwogKKBgOTH4cCdm02THRHfE7CF3PCc23mtf8g0M5',
        'H_BDCLCKID_SF': 'tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us-GuJ2hcHMPoosIOPX5j-KfFWDJ34Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-KkjPblJhOmKbueW4bDfn028DKu-n5jHj5XjGLH3q',
        'H_BDCLCKID_SF_BFESS': 'tRAOoC8-fIvEDRbN2KTD-tFO5eT22-us-GuJ2hcHMPoosIOPX5j-KfFWDJ34Bn3kaK7j--nwJxbUotoHXh3tMt_thtOp-CrpyCcELh5TtUJMqIDzbMohqqJXQqJyKMni0Dv9-pP2KhOfDDt43M7Cy-KkjPblJhOmKbueW4bDfn028DKu-n5jHj5XjGLH3q',
        'Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc': '1709095843,1709271023,1709372773',
        'BDUSS': 'hBR1FjdVdRRDl1V2c3LWhqUGlsQUpCbjhWVHp1fmhiQjFlZjFLaDJMdkxnZ3BtSUFBQUFBJCQAAAAAAAAAAAEAAACLZV1qQm95ZbH5wejRqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMv14mXL9eJlYV',
        'SIGNIN_UC': '70a2711cf1d3d9b1a82d2f87d633bd8a04593853255RuNQissJE7jPnGJ17zGsQdSlpbkmuYpHyIIIwmD4Opz7M8TnSEWt1rFQjxWKySCqVMIsjYNW0lc0t9IaYApS%2Fy3MAY8v%2Fh4RiS%2BfaM3CHu7N7jbeDl30I%2BHl9H2RgAEdgMHPE0MqF3%2B2Y4dfkraUhn3TcTfeDMEj%2Bx8Mn8tZeM71RfxYpHSN7qxuVZI4Tvs2CMk4dNGAcTw9lphHsfo3H7gdMMJcpkNu5jY%2Fjjb1bhC614UF1D10bNLUQzopsTLgNBPCKQYzKkPFBbgHL1%2FJIpwW92mFKGQoGp89gdV5Pvef5ykfkxBCA8E8nQFJgR3W71330263966223401406981213276774',
        '__cas__rn__': '459385325',
        '__cas__st__212': 'a1ff905cc3b1124528303b037b026942a74a46662c409f08bb0a3d40204c45fa2cf9bab8a1de0d302a1a388a',
        '__cas__id__212': '45993938',
        'CPTK_212': '2000481705',
        'CPID_212': '45993938',
        'bdindexid': 'd0qgu1637cdbu0n5a28il7fnm4',
        'Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc': '1709372806',
        'BA_HECTOR': '01842001a18k85ag8l2184a0bohj291iu5vvi1t',
        'delPer': '0',
        'BDRCVFR[tox4WRQ4-Km]': 'mk3SLVN4HKm',
        'BDRCVFR[-pGxjrCMryR]': 'mk3SLVN4HKm',
        'ab_sr': '1.0.1_YWU5M2ZhZTg1NWNlYjBlMWQ4MTFhM2NmY2Q0NDEzNTM2ZTZkOWY5ZmMyMzU2YzYyZjQ5N2ExMDFmYjFkMDczMjYwMDRlMjY1YmE0Y2UyMTJmZGIwMWJmZDk5ZGJlMzg1YmQ0OTM1MTc3OWM1ZmQyMjFkYjdjMzZmNzBkNzM0ZTQ1NjIyNWZjYTRjZDgyZTI2YWYxOGJjMmNmYmEwZDYzOWQ0ZDJlNTQxY2EwNzM1NDkwY2I3YWMyMDVkZTgxYzk3YjhjODRhYTNlODkzNGYzMWFiNmJlYTU5YTU0ZmI2ZTg=',
        'BDUSS_BFESS': 'hBR1FjdVdRRDl1V2c3LWhqUGlsQUpCbjhWVHp1fmhiQjFlZjFLaDJMdkxnZ3BtSUFBQUFBJCQAAAAAAAAAAAEAAACLZV1qQm95ZbH5wejRqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMv14mXL9eJlYV',
        'RT': '"z=1&dm=baidu.com&si=3327a95d-a655-4753-b71c-c667398c835d&ss=lt9wew2p&sl=g&tt=exp&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=259x5"',
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://index.baidu.com',
        'Referer': 'https://index.baidu.com/v2/main/index.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    json_data = {
        'words': [
            '养老',
        ],
        'source': 'pc_home',
    }
    response = requests.post('https://index.baidu.com/insight/word/sug', cookies=cookies, headers=headers,
                             json=json_data).text
    a = re.findall('"word":"(.*?)",', response)[1::]  # 将数据处理并返回一个列表
    print(a)
    for i in a:
        dd = {'数据': i}
        sql = insert_sql(dd, 'xiangguan')
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def main():
    """
    主函数
    """
    cctv()
    cctv2()
