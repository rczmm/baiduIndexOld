import random
import re
import os
import pandas as pd
import statsmodels.api as sm
import pyecharts.options as opts
from pyecharts.charts import Line, Page
import pymysql
import warnings


def cctv4():
    warnings.filterwarnings("ignore")  # 忽略警告
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='495000', database='test',
                           charset='utf8')  # 连接数据库
    data = pd.read_sql('select * from zhishu', conn)  # select来查询数据

    aaa = [int(i) for i in data['指数']]  # 将数据库中数据进行整合处理

    print(aaa)
    # 采用ARIMA模型来进行预测
    model = sm.tsa.ARIMA(aaa, order=(5, 1, 0))  # 设置一个p, d, q 其中 P为自回归项，q为移动平均项数，d为差分次数
    model_fit = model.fit()
    orecast = model_fit.forecast(steps=5)  # 预测未来5天的数据
    a = str(orecast)
    a1 = str(a.split('    ')).split(r'\n')
    print(a1)
    lst = [0]  # 将数据存放在列表中
    lst2 = [i for i in range(36)]
    for i in aaa:
        lst.append(i)
    for i in a1:
        xe = i.replace("['[", '').replace("]']", '').split(' ')  # 将预测数据处理
        for i7 in xe:
            if len(i7) > 0:
                print(i7)
                lst.append(int(float(i7)))
    conn.close()
    y, x = lst, lst2
    weights = [random.random(0, 1) for _ in range(len(y))]  # 设置每个点的权重
    weighted_average = sum(d * w for d, w in zip(y, weights)) / sum(weights)  # 计算加权平均值

    c = (Line(
        init_opts=opts.InitOpts(width="450px", height="350px", chart_id='wee1'))  # 不添加默认红色 ,theme =ThemeType.MACARONS
         .add_xaxis(x)
         .add_yaxis(
        "预测未来五天的数据",
        y,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(name="预测值", coord=[x[30], y[30]], value=y[30])]  # 这里定义要显示的标签数据
        ),
    )
         .set_global_opts(title_opts=opts.TitleOpts(title=""),
                          xaxis_opts=opts.AxisOpts(
                              name='天数',
                              name_location='middle',
                              name_gap=40,  # 标签与轴线之间的距离，默认为20，最好不要设置20
                              name_textstyle_opts=opts.TextStyleOpts(
                                  font_family='Times New Roman',
                                  font_size=16  # 标签字体大小
                              )),
                          yaxis_opts=opts.AxisOpts(
                              name='搜索次数',
                              name_location='middle',
                              name_gap=40,
                              name_textstyle_opts=opts.TextStyleOpts(
                                  font_family='Times New Roman',
                                  font_size=16
                                  # font_weight='bolder',
                              ),
                              markline_opts=opts.MarkLineOpts(
                                  data=[opts.MarkLineItem(type_='max', name='加权平均值', value=weighted_average)]),
                              linestyle_opts=opts.LineStyleOpts(color='#000', width=1, opacity=0.5, curveness=0.2,
                                                                dash_offset=10)),
                          )

         )
    return c


def main():
    c = cctv4()
    page = Page(layout=Page.DraggablePageLayout)
    page.add(c)
    page.render()
    Page.save_resize_html("render.html", cfg_file=r"json文件/预测.json", dest="tp/shijian1.html")
    a111 = os.path.exists('templates/指数预测1.html')
    if a111:
        os.remove('templates/指数预测1.html')
    with open('tp/shijian1.html', 'r', encoding='utf-8') as f:
        a = f.read()
        # print(a)
        a8 = re.findall('<body >(.*?)</body>', a, re.S)[0]
        with open('templates/指数预测.html', 'r', encoding='utf-8') as f1:
            with open('templates/指数预测1.html', 'a+', encoding='utf-8') as f2:
                for i in f1:
                    f2.write(i)
                    if '<!-- 内容主体区域 -->' in i:
                        f2.write(a8)
