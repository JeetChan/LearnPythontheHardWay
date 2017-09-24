virtualenv -p D:\Program\Python36\python.exe --no-site-packages ENV
pip install git+https://github.com/mitsuhiko/flask-sqlalchemy
pip install Flask-SQLAlchemy -i https://pypi.douban.com/simple
pip install SQLAlchemy -i https://pypi.douban.com/simple

heroku git:remote -a obscure-sierra-78677

heroku create cbcweatherapp --buildpack heroku/python

heroku git:remote -a cbcweatherapp 