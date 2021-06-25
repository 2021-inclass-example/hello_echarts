from flask import Flask, render_template

from pyecharts.charts import Bar
import pyecharts

app = Flask(__name__)


@app.route('/')
def index():
    page_contnet = """<html>
    <header>
        <title>Hello Echarts</title>
    </header>

    <body>
        <p>
            <a href='/1'>查看 1</a>
        </p>

        <p>
            <a href='/10'>查看 10</a>
        </p>

        <p>
            <a href='/100'>查看 100</a>
        </p>

        <p>
            <a href='/1000'>查看 1000</a>
        </p>

        <p>
            <a href='/10000'>查看 10000</a>
        </p>
    </body>
</html>
"""
    return page_contnet


@app.route('/<number>')
def hello(number):
    bar = Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [5, 20, 36, 10, 75, number])
    bar.render('templates/index.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
