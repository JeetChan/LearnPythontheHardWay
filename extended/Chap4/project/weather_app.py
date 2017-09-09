""" 
输入城市名，获取该城市最新天气情况
点击「帮助」，获取帮助信息
点击「历史」，获取历史查询信息
"""
from flask import Flask
from flask import jsonify
from flask import render_template

from flask import session
from flask_bootstrap import Bootstrap
from WeatherForm import WeatherForm
import weather_servers
from collections import deque
import json
import pickle
from urllib.error import HTTPError


app = Flask(__name__)
bootstrap = Bootstrap(app)
# 加载本地资源
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config.from_object('config')


@app.route('/')
def index():
    form = WeatherForm()
    return render_template('index.html', title_name='天气查询', form=form)


@app.route('/search', methods=('GET', 'POST'))
def search_weather():

    form = WeatherForm()
    if form.validate_on_submit():
        try:
            weather_data = weather_servers.format_weather(form.city.data)

            d = deque([], maxlen=5)

            if 'history' in session:
                history = pickle.loads(session['history'])
                history.append(weather_data)
                session['history'] = pickle.dumps(history)
            else:
                d.append(weather_data)
                session['history'] = pickle.dumps(d)

            return jsonify(render_template('weather_data.html', weather_data=weather_data))
        except HTTPError as ex:
            data = {'message': ex.msg}
            return jsonify(render_template('weather_data.html', error=data))

    data = {'message': form.errors['city'][0]}

    return jsonify(render_template('weather_data.html',  data=data))


@app.route('/history', methods=('GET', 'POST'))
def search_history():

    if 'history' in session:
        history = pickle.loads(session['history'])
        return jsonify(render_template('history_data.html', weather_datas=list(history)))
    else:
        return jsonify(render_template('history_data.html', data={'message': '还没有历史查询记录！'}))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
