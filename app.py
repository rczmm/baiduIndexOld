from flask import Flask, render_template, request, session, flash

from src import main

app = Flask(__name__)


@app.route('/首页.html')  # url后缀加上图片地址 访问图片列表
def t1():
    return render_template('首页.html', msg='跳转成功')


@app.route('/热点话题1.html')  # url后缀加上图片地址 访问图片列表
def t2():
    return render_template('热点话题1.html', msg='跳转成功')


@app.route('/指数预测1.html')  # url后缀加上图片地址 访问图片列表
def t3():
    return render_template('指数预测1.html', msg='跳转成功')


@app.route('/关键词.html')  # url后缀加上图片地址 访问图片列表
def t4():
    return render_template('关键词.html', msg='跳转成功')


@app.route('/年龄1.html')  # url后缀加上图片地址 访问图片列表
def t5():
    return render_template('年龄1.html', msg='跳转成功')


@app.route('/地域分布1.html')  # url后缀加上图片地址 访问图片列表
def t6():
    return render_template('地域分布1.html', msg='跳转成功')


@app.route('/gjc.html')  # url后缀加上图片地址 访问图片列表
def t7():
    return render_template('gjc.html', msg='跳转成功')


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'aim123' and password == '123456':
        session['username'] = username
        return render_template('首页.html', msg='登陆成功')

    else:
        flash('Invalid username or password', 'error')
        return render_template('login.html', msg='登录失败')


if __name__ == '__main__':
    main.run()
    app.run()
