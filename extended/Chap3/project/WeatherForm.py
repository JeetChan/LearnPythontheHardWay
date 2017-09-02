""" 表单 """
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class WeatherForm(FlaskForm):
    city = StringField('', validators=[DataRequired('城市名称不能为空！')], render_kw={
                       'placeholder': '请输入城市名称', 'class': 'form-control'})
